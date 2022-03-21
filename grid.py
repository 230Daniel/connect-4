from column import Column


class Grid:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._columns = []
        for i in range(self._width):
            self._columns.append(Column(height))

    def get_display(self):
        output = f" {' '.join(str(x) for x in range(1, self._width + 1))}\n"
        output += "╔" + "═" * (self._width * 2 - 1) + "╗"
        for i in range(self._height):
            output += "\n║"
            for j in range(self._width):
                if j == self._width - 1:
                    spacer = ""
                else:
                    spacer = " "
                token = self._columns[j].get_token(i)
                if token is None:
                    token = " "
                output += token + spacer
            output += "║"
        output += "\n╚" + "═" * (self._width * 2 - 1) + "╝"
        return output

    def drop_token(self, column: object, token_colour: object) -> object:
        return self._columns[column].drop_token(token_colour)
