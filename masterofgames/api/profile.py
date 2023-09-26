from flask import Blueprint, render_template, abort

from masterofgames.crud.profile import ProfileService

blueprint = Blueprint("profile", __name__)


@blueprint.route("/<name>", methods=["GET"])
async def profile(name: str) -> any:
    service = ProfileService()

    user_id = name
    if not name.isdigit():
        user_id = await service.get_user_id(name)

    try:
        return render_template("profile.html", profile=await service.get_profile(user_id))
    except ValueError as error:
        abort(400)
    except RuntimeError as error:
        abort(404)
