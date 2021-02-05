from flask import Blueprint, render_template, request, redirect, url_for

blueprint = Blueprint('homepage', __name__)


@blueprint.route("/", methods=["GET"])
def index() -> any:
    return render_template("index.html")


@blueprint.route("/", methods=["POST"])
def index2() -> any:
    return redirect(url_for("profile.profile", name=request.form["name"]))
