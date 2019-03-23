#!/bin/sh

sh -c "pipenv install --deploy"
sh -c "pytest"
