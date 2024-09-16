from typing import Annotated

from litestar import Controller, get, Router, post
from litestar.datastructures import State
from litestar.enums import RequestEncodingType
from litestar.exceptions import HTTPException
from litestar.params import Body
from litestar.response import Template, Redirect

from masterofgames.entities import IndexInput
from masterofgames.services import AchievementService, ProfileService


class ProfileViewController(Controller):
    tags = ["View"]

    @get()
    async def index(self) -> Template:
        return Template(template_name="index.html")

    @post(status_code=301)
    async def redirect(
        self, state: State, data: Annotated[IndexInput, Body(media_type=RequestEncodingType.URL_ENCODED)]
    ) -> Redirect:
        service = ProfileService()
        user_id = data.name
        if not user_id.isdigit():
            user_id = await service.get_user_id(state.client, user_id, state.api_key)
        return Redirect(path=f"/{user_id}")

    @get(path="{name:str}")
    async def profile(self, state: State, name: str) -> Template:
        service = ProfileService()

        user_id = name
        if not name.isdigit():
            user_id = await service.get_user_id(state.client, name, state.api_key)
        try:
            return Template(
                template_name="profile.html",
                context={"profile": await service.get_profile(state.client, user_id, state.api_key)},
            )
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Cannot or will not process the request due to something that is perceived to be a client error.",
            )
        except RuntimeError:
            raise HTTPException(status_code=404, detail="Cannot find the requested resource.")

    @get(path="{user_id:str}/{game_id:str}")
    async def achievements(self, state: State, user_id: str, game_id: str) -> Template:
        service = AchievementService()
        try:
            return Template(
                template_name="achievements.html",
                context={"details": await service.get_achievements(state.client, user_id, game_id, state.api_key)},
            )
        except ValueError as error:
            print(error)
            raise HTTPException(
                status_code=400,
                detail="Cannot or will not process the request due to something that is perceived to be a client error.",
            )
        except RuntimeError:
            raise HTTPException(status_code=404, detail="Cannot find the requested resource.")


@get(path="healthcheck", cache=False, tags=["Misc"])
async def health_check() -> str:
    return "OK"


view_router = Router(path="", route_handlers=[ProfileViewController, health_check])
