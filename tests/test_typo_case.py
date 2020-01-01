import pytest
from typocase.models import SpecChars
from typocase.typo_case import TypoCase


@pytest.mark.parametrize(
    "input_string, special_char, expected_string",
    [
        ("", SpecChars.DOT, ""),
        ("abc def ghi", SpecChars.DOT, "abc.def.ghi"),
        ("abc def ghi", SpecChars.DASH, "abc-def-ghi"),
        ("abc def ghi", SpecChars.SLASH, "abc/def/ghi"),
        ("abc def ghi", SpecChars.UNDER_SCORE, "abc_def_ghi"),
        ("abc def ghi", SpecChars.WHITE_SPACE, "abc def ghi"),
    ],
)
def test_join_comps_by_special_char(input_string, special_char, expected_string):
    assert (
        TypoCase(input_string).join_comps_by_special_char(special_char)
    ) == expected_string
