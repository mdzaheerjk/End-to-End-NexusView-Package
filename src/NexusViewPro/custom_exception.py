class InvalidURLException(Exception):
    """Exception raised for invalid URLs."""
    def __init__(self, message="The provided URL is invalid."):
        self.message = message
        super().__init__(self.message)