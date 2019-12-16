from typocase.string_compounds import StringCompounds
from typocase.models import SpecChars


class TypoCase:
    def __init__(self, string: str):
        self.string = string if string else ""
        self.compounds = StringCompounds(self.string).extract()

    def join_comps_by_special_char(self, specchar: SpecChars) -> str:
        return f"{specchar.value}".join(self.compounds)

    def pascal_case(self) -> str:
        compounds_len = len(self.compounds)
        return "".join(
            [
                comp[0].upper() + comp[1:].lower() if compounds_len > 1 else comp
                for comp in self.compounds
            ]
        )

    def camel_case(self) -> str:
        pascal_case = self.pascal_case()
        if len(pascal_case) == 0:
            return pascal_case
        return pascal_case[0].lower() + pascal_case[1:]

    def snake_case(self) -> str:
        return self.join_comps_by_special_char(SpecChars.UNDER_SCORE).lower()

    def constant_case(self) -> str:
        if len(self.compounds) == 1:
            return self.snake_case()
        return self.snake_case().upper()

    def kebab_case(self) -> str:
        return self.join_comps_by_special_char(SpecChars.DASH).lower()
