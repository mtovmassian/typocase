from typocase.string_compounds import StringCompounds
from typocase.models import SpecChars


class TypoCase:

    def __init__(self, string: str):
        self.string = string
        self.compounds = StringCompounds(
            self.string
        ).extract_compounds()

    def join_compounds(self, sep: SpecChars) -> str:
        return f"{sep.value}".join(self.compounds)

    def pascal_case(self) -> str:
        return "".join([
            comp[0].upper() + comp[1:]
            for comp in self.compounds
        ])

    def camel_case(self) -> str:
        pascal_case = self.pascal()

        return pascal_case[0].lower() + pascal_case[1:]

    def snake_case(self) -> str:
        return self.join_compounds(SpecChars.UNDER_SCORE)

    def kebab_case(self) -> str:
        return self.join_compounds(SpecChars.DASH)

    def path_case(self):
        return self.join_compounds(SpecChars.SLASH)

    def dot_case(self):
        return self.join_compounds(SpecChars.DOT)

    def constant_case(self):
        return self.snake_case().upper()
