__strict__ = True

import gzip
import logging
import sys
from typing import Any

from flask import Flask, render_template, request
from werkzeug.sansio.response import Response

from api import homepage, profile, achievements

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

app = Flask(__name__)
app.register_blueprint(homepage.blueprint)
app.register_blueprint(profile.blueprint)
app.register_blueprint(achievements.blueprint)


@app.errorhandler(400)
def bad_request_error(error) -> Any:
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html", error=error), 400


@app.errorhandler(404)
def not_found_error(error) -> Any:
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html", error=error), 404


@app.errorhandler(Exception)
def unhandled_exception(error) -> Any:
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html"), 500


@app.before_request
def add_request_log() -> None:
    if "/static/" not in request.path:
        app.logger.debug("Matched route.", extra={"channel": "request", "path": request.path})


@app.after_request
def add_compression(response: Response) -> Response:
    if request.path.startswith("/static/"):
        return response
    response.data = gzip.compress(response.data, 5)  # type: ignore
    response.headers["Content-Encoding"] = "gzip"
    response.headers["Content-length"] = len(response.data)  # type: ignore
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
