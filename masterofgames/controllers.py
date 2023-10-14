from typing import Annotated

from litestar import Controller, get, Router, post, Request
from litestar.enums import RequestEncodingType
from litestar.exceptions import HTTPException
from litestar.params import Body
from litestar.response import Template, Redirect

from masterofgames.services import AchievementService, ProfileService
from masterofgames.entities import IndexInput


class ProfileViewController(Controller):
    tags = ["View"]

    @get()
    async def index(self) -> Template:
        return Template(template_name="index.html")

    @post(status_code=301)
    async def redirect(self, data: Annotated[IndexInput, Body(media_type=RequestEncodingType.URL_ENCODED)]) -> Redirect:
        print(data)
        return Redirect(path=f"/{data.name}")

    @get(path="{name:str}")
    async def profile(self, name: str) -> Template:
        service = ProfileService()

        user_id = name
        if not name.isdigit():
            user_id = await service.get_user_id(name)
        try:
            return Template(template_name="profile.html", context={"profile": await service.get_profile(user_id)})
        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail="Cannot or will not process the request due to something that is perceived to be a client error.",
            )
        except RuntimeError as error:
            raise HTTPException(status_code=404, detail="Cannot find the requested resource.")

    @get(path="{user_id:str}/{game_id:str}")
    async def achievements(self, user_id: str, game_id: str) -> Template:
        service = AchievementService()
        try:
            return Template(
                template_name="achievements.html", context={"details": await service.get_achievements(user_id, game_id)}
            )
        except ValueError as error:
            print(error)
            raise HTTPException(
                status_code=400,
                detail="Cannot or will not process the request due to something that is perceived to be a client error.",
            )
        except RuntimeError as error:
            raise HTTPException(status_code=404, detail="Cannot find the requested resource.")


@get(path="healthcheck", cache=False, tags=["Misc"])
async def health_check() -> str:
    return "OK"


view_router = Router(
    path="",
    route_handlers=[ProfileViewController, health_check],
    # dependencies={"repository": Provide(task_repository, sync_to_thread=False)},
)
