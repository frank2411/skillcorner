import json


class LineHelper:
    def __init__(self, line_number: int, line: str) -> None:
        self.line_number = line_number
        self.line = line
        self.is_even = True if (line_number % 2) == 0 else False

    def calculate_line(self) -> None:
        """Call fist method and then return some results in some condition is True.
        otherwise run other methods in cascade (next step simulation)
        """

        # Call fist method and then return some results in case
        # otherwise other methods in cascade (steps simulation)
        if self.line_number > 0:
            self.is_multiple_of()
        else:
            self.check_and_clean_dollar_sign()

    def is_multiple_of(self, module: int = 5) -> None:
        """Fist method in the chain. Check if current line number is multiple of `module`

        Args:
        module: The number to check if line number is multiple of.
        """

        if self.line_number % module == 0:
            self.line = "Multiple de 5"
            return

        self.check_and_clean_dollar_sign()

    def check_and_clean_dollar_sign(self) -> None:
        """Second method in the chain. Check if a dollar `$` character is found in the line.
        If found, replace all spaces ` ` with `_`
        """

        if "$" in self.line:
            self.line = self.line.replace(" ", "_")
            return

        self.check_ending_dot()

    def check_ending_dot(self):
        """Third method in the chain. Check if a dot `.` character is found at the end of the line.
        If found, return line value as it is.
        """

        copied_line = self.line
        copied_line = copied_line.replace("\r", "")
        copied_line = copied_line.replace("\n", "")

        if copied_line.endswith("."):
            return

        self.check_json_format()

    def check_json_format(self):
        """Fourth method in the chain. Check if a curly bracket `{` character is found at the start of the line.
        If found, deserialize line value in JSON format, add `pair` key to the deserialized data and, lastly, re-serialize
        the changed data and set it as the new value of line.

        If the `{` character is not found, we will return a default value since, no condition before was met.
        """

        # At this point no condition is True so, nothing to see there :)
        if not self.line.startswith("{"):
            self.line = "Rien à afficher"
            return

        data = json.loads(self.line)
        data["pair"] = self.is_even
        self.line = json.dumps(data)
