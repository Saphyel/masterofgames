from flask import Blueprint, render_template, abort

from crud.achievement import AchievementService

blueprint = Blueprint("achievements", __name__)


@blueprint.route("/<user_id>/<game_id>", methods=["GET"])
def achievements(user_id: str, game_id: str) -> any:
    service = AchievementService()

    try:
        return render_template("achievements.html", details=service.get_achievements(user_id, game_id))
    except ValueError as error:
        abort(400)
    except RuntimeError as error:
        abort(404)
