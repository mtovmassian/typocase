from typing import List
from enum import Enum


class SpecChars(Enum):
    WHITE_SPACE = " "
    UNDER_SCORE = "_"
    DASH = "-"
    SLASH = "/"
    DOT = "."


class StringCompounds:

    WHITE_SPACE = SpecChars.WHITE_SPACE.value

    def __init__(self, string: str):
        self.string = string

    def extract_compounds(self) -> List[str]:
        compounds = self.extract_compounds_specchar_sep()
        if len(compounds) == 1:
            compounds = self.extract_compounds_uppercase_sep()

        return compounds

    def extract_compounds_uppercase_sep(self) -> List[str]:
        compounds = "".join([
            char if char.islower() else f"{self.WHITE_SPACE}{char}"
            for char in self.string if char.isalnum()
        ]).split(self.WHITE_SPACE)

        return self.trim_compounds(compounds)

    def extract_compounds_specchar_sep(self) -> List[str]:
        compounds = "".join([
            char if char.isalnum() else self.WHITE_SPACE
            for char in self.string
        ]).split(self.WHITE_SPACE)

        return self.trim_compounds(compounds)

    @staticmethod
    def trim_compounds(compounds: List[str]) -> List[str]:
        """Remove empty compounds and pass other compounds to lowercase

        Args:
            compounds: List of compounds

        Returns:
            List of compounds
        """
        return [comp.lower() for comp in compounds if comp]


class TypoCase:

    def __init__(self, string: str):
        self.string = string
        self.compounds = StringCompounds(
            self.string
        ).extract_compounds()

        print(self.compounds)

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


if __name__ == "__main__":
    tc = TypoCase("martin.tovmassian@protonmail.com")
    print(tc.dot_case())
