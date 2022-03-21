class Column:
    def __init__(self, height):
        self._height = height
        self._tokens = [None] * height

    def get_tokens(self):
        return self._tokens

    def get_token(self, index):
        return self._tokens[index]

    def drop_token(self, token_colour):
        for row in range(self._height - 1, -1, -1):
            if self._tokens[row] is None:
                self._tokens[row] = token_colour
                return True
        return False
