import os
from flask import Flask, render_template, request, redirect, url_for

from steam_api import SteamAPI, UserRepository, PlayerRepository, StatsRepository
from transformer import ProfileTransformer, GameTransformer, AchievementTransformer

app = Flask(__name__)
api = SteamAPI()
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/", methods=['GET'])
def index() -> any:
    app.logger.info('Matched route "index" url: '+request.url)
    return render_template('index.html')


@app.route("/", methods=['POST'])
def index2() -> any:
    return redirect(url_for('games', name=request.form['name']))


@app.route("/<name>", methods=['GET'])
def games(name: str) -> any:
    app.logger.info('Matched route "games" url: '+request.url)
    user_id = name
    user = UserRepository(api)
    if not name.isdigit():
        user_id = user.find_user_id(name)

    return render_template('profile.html', profile=ProfileTransformer.transform(user.get_summary(user_id)),
                           game_list=GameTransformer.transform(PlayerRepository(api).find_games(user_id)))


@app.route("/<user_id>/<game_id>", methods=['GET'])
def achievements(user_id: str, game_id: str) -> any:
    app.logger.info('Matched route "achievements" url: ' + request.url)
    stats = StatsRepository(api)
    game_details = stats.game_details(game_id)
    player_progress = stats.player_progress(user_id, game_id)

    return render_template('achievements.html', title=game_details['gameName'],
                           achievements=AchievementTransformer.transform(
                               game_details['availableGameStats']['achievements'], player_progress))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
