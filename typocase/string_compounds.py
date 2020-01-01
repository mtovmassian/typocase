from typing import List

from typocase.models import SpecChars


class StringCompounds:
    """Retrieve substrings from string
    with special chars or uppercase letters as separators.

    Args:
        self: StringCompounds instance
        string: string from which compounds need to be extracted.
    """

    WHITE_SPACE = SpecChars.WHITE_SPACE.value

    def __init__(self, string: str):
        self.string = string if string else ""

    def __repr__(self):
        return f'{self.__class__.__name__}(string="{self.string}")'

    def extract(self) -> List[str]:
        """Try to extract compounds based on special chars as separators.
        If no result,
        try to extract compounds based on uppercase letters as separators.

        Args:
            self: StringCompounds instance

        Returns:
            List of compounds
        """
        compounds = self.split_on_special_chars()
        if len(compounds) == 1:
            compounds = self.split_on_uppercase_letters()

        return compounds

    def split_on_uppercase_letters(self) -> List[str]:
        """Splits instance string based on uppercase letters detection.

        Args:
            self: StringCompounds instance

        Returns:
            Trimmed list of compounds
        """
        compounds = "".join(
            [
                char if char.islower() else f"{self.WHITE_SPACE}{char}"
                for char in self.string
                if char.isalnum()
            ]
        ).split(self.WHITE_SPACE)

        return self.trim(compounds)

    def split_on_special_chars(self) -> List[str]:
        """Splits instance string based on special characters detection.

        Args:
            self: StringCompounds instance

        Returns:
            Trimmed list of compounds
        """
        compounds = "".join(
            [char if char.isalnum() else self.WHITE_SPACE for char in self.string]
        ).split(self.WHITE_SPACE)

        return self.trim(compounds)

    @staticmethod
    def trim(compounds: List[str]) -> List[str]:
        """Remove empty strings and switch other strings to lowercase.

        Args:
            compounds: List of compounds

        Returns:
            List of compounds
        """
        return [comp.lower() for comp in compounds if comp]
