"""
Contains several custom exceptions
"""

class NotValidExtension(Exception):
    def __init__(self, file_name, message = 'Found an invalid extension'):
        self.file_name = file_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_name} :: {self.message}'

class NotValidMimeType(Exception):
    def __init__(self, file_name, message = 'Found an invalid mime type'):
        self.file_name = file_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.file_name} :: {self.message}'
