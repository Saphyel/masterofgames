workflow "Deployment" {
  on = "push"
  resolves = "Heroku deployment"
}

action "Run unit test" {
  uses = "./action-test"
}

action "Heroku login" {
  uses = "actions/heroku@master"
  needs = ["Run unit test"]
  args = "container:login"
  secrets = ["HEROKU_API_KEY"]
}

action "Heroku push" {
  uses = "actions/heroku@master"
  needs = "login"
  args = "container:push -a gentle-escarpment-23841 web"
  secrets = ["HEROKU_API_KEY"]
}

action "Heroku release" {
  uses = "actions/heroku@master"
  needs = "push"
  args = "container:release -a gentle-escarpment-23841 web"
  secrets = ["HEROKU_API_KEY"]
}
