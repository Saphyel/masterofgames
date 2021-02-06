__strict__ = True

import logging
import sys

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request

from api import homepage, profile, achievements

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


@app.errorhandler(400)
def bad_request_error(error):
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html", error=error), 400


@app.errorhandler(404)
def not_found_error(error):
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html", error=error), 404


@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error("URL: " + request.url + " " + error.__str__())
    return render_template("error.html"), 500


@app.before_request
def add_request_log():
    app.logger.debug("Matched route.", extra={"channel": "request"})


app.register_blueprint(homepage.blueprint)
app.register_blueprint(profile.blueprint)
app.register_blueprint(achievements.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
