__strict__ = True

import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

from service import ProfileService, AchievementService
from repository import SteamClient, UserRepository, PlayerRepository, StatsRepository

for file in os.listdir("./"):
    if file.startswith(".env"):
        load_dotenv(file)

app = Flask(__name__)
client = SteamClient(os.environ.get('STEAM_API_KEY'))


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error=error), 404


@app.route("/", methods=['GET'])
def index() -> any:
    return render_template('index.html')


@app.route("/", methods=['POST'])
def index2() -> any:
    return redirect(url_for('games', name=request.form['name']))


@app.route("/<name>", methods=['GET'])
def games(name: str) -> any:
    user_id = name
    service = ProfileService(UserRepository(client), PlayerRepository(client))
    if not name.isdigit():
        user_id = service.get_user_id(name)

    try:
        return render_template('profile.html', profile=service.get_profile(user_id))
    except ValueError as error:
        app.logger.error('URL: ' + request.url + ' ' + error.__str__())
        return not_found_error(error)
    except RuntimeError as error:
        app.logger.error('URL: ' + request.url + ' ' + error.__str__())
        return not_found_error(error)


@app.route("/<user_id>/<game_id>", methods=['GET'])
def achievements(user_id: str, game_id: str) -> any:
    service = AchievementService(StatsRepository(client))

    try:
        return render_template('achievements.html', details=service.get_achievements(user_id, game_id))
    except ValueError as error:
        app.logger.error('URL: ' + request.url + ' ' + error.__str__())
        return not_found_error(error)
    except RuntimeError as error:
        app.logger.error('URL: ' + request.url + ' ' + error.__str__())
        return not_found_error(error)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
