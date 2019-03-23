workflow "Run tests" {
  on = "push"
  resolves = ["Run unit test"]
}

action "Run unit test" {
  uses = "./action-test"
}
