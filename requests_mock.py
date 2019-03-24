class MockResponse:
    def __init__(self, valid: bool, result: dict):
        self._valid = valid
        self._content = result

    @property
    def ok(self) -> bool:
        return self._valid

    @property
    def text(self) -> str:
        return 'error'

    def json(self):
        return self._content
