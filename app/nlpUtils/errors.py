class CustomError(Exception):
    def __init__(self, message=None):
        self.message = message or "An error occurred"
        super().__init__(self.message)
