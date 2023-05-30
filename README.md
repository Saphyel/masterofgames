# Master of Games
This app aims to help people to complete their games returning a youtube search for every missing achievement given a game.

## Prerequisites
* Docker
* Steam API Key (https://steamcommunity.com/dev)

## Start the project
Create a .env file with your secrets and execute

    docker build -t masterofgames .

## Run the project

### Windows Command Prompt

    docker run --rm --env-file .env -v %cd%:/app -p 8081:80 -it masterofgames

### Everything else

    docker run --rm --env-file .env -v ${PWD}:/app -p 8081:80 -it masterofgames gunicorn --reload --bind 0.0.0.0:80 manage:app

## Test the project
You'll need to install inside the container the dev dependencies and run pytest

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
