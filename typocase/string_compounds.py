from typing import List


from typocase.models import SpecChars


class StringCompounds:

    WHITE_SPACE = SpecChars.WHITE_SPACE.value

    def __init__(self, string: str):
        self.string = string if string else ""

    def extract(self) -> List[str]:
        compounds = self.extract_by_specchar_sep()
        if len(compounds) == 1:
            compounds = self.extract_by_uppercase_sep()

        return compounds

    def extract_by_uppercase_sep(self) -> List[str]:
        compounds = "".join([
            char if char.islower() else f"{self.WHITE_SPACE}{char}"
            for char in self.string if char.isalnum()
        ]).split(self.WHITE_SPACE)

        return self.trim(compounds)

    def extract_by_specchar_sep(self) -> List[str]:
        compounds = "".join([
            char if char.isalnum() else self.WHITE_SPACE
            for char in self.string
        ]).split(self.WHITE_SPACE)

        return self.trim(compounds)

    @staticmethod
    def trim(compounds: List[str]) -> List[str]:
        """Remove empty compounds and pass other to lowercase

        Args:
            compounds: List of compounds

        Returns:
            List of compounds
        """
        return [comp.lower() for comp in compounds if comp]
