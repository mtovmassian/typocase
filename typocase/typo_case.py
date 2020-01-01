from typocase.models import SpecChars
from typocase.string_compounds import StringCompounds


class TypoCase:
    def __init__(self, string: str):
        self.string = string
        self.compounds = StringCompounds(self.string).extract()

    def join_comps_by_special_char(self, specchar: SpecChars) -> str:
        return f"{specchar.value}".join(self.compounds)

    def pascal_case(self) -> str:
        return "".join([comp[0].upper() + comp[1:] for comp in self.compounds])

    def camel_case(self) -> str:
        pascal_case = self.pascal_case()
        if len(pascal_case) == 0:
            return pascal_case

        return pascal_case[0].lower() + pascal_case[1:]

    def snake_case(self) -> str:
        return self.join_comps_by_special_char(SpecChars.UNDER_SCORE)

    def constant_case(self):
        return self.snake_case().upper()

    def kebab_case(self) -> str:
        return self.join_comps_by_special_char(SpecChars.DASH)

    def path_case(self):
        return self.join_comps_by_special_char(SpecChars.SLASH)

    def dot_case(self):
        return self.join_comps_by_special_char(SpecChars.DOT)
