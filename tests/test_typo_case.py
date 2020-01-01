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


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "AbcDefGhi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "AbcDefGhi"),
        # from pascal case string
        ("AbcDefGhi", "AbcDefGhi"),
        # from camel case string
        ("abcDefGhi", "AbcDefGhi"),
        # from snake case string
        ("abc_def_ghi", "AbcDefGhi"),
        # from constant case string
        ("ABC_DEF_GHI", "AbcDefGhi"),
        # from kebab case string
        ("abc-def-ghi", "AbcDefGhi"),
        # from path case string
        ("abc/def/ghi", "AbcDefGhi"),
        # from dot case string
        ("abc.def.ghi", "AbcDefGhi"),
    ],
)
def test_pascal_case(input_string, expected_string):
    assert (TypoCase(input_string).pascal_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "abcDefGhi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "abcDefGhi"),
        # from pascal case string
        ("AbcDefGhi", "abcDefGhi"),
        # from camel case string
        ("abcDefGhi", "abcDefGhi"),
        # from snake case string
        ("abc_def_ghi", "abcDefGhi"),
        # from constant case string
        ("ABC_DEF_GHI", "abcDefGhi"),
        # from kebab case string
        ("abc-def-ghi", "abcDefGhi"),
        # from path case string
        ("abc/def/ghi", "abcDefGhi"),
        # from dot case string
        ("abc.def.ghi", "abcDefGhi"),
    ],
)
def test_camel_case(input_string, expected_string):
    assert (TypoCase(input_string).camel_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "abc_def_ghi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "abc_def_ghi"),
        # from pascal case string
        ("AbcDefGhi", "abc_def_ghi"),
        # from camel case string
        ("abcDefGhi", "abc_def_ghi"),
        # from snake case string
        ("abc_def_ghi", "abc_def_ghi"),
        # from constant case string
        ("ABC_DEF_GHI", "abc_def_ghi"),
        # from kebab case string
        ("abc-def-ghi", "abc_def_ghi"),
        # from path case string
        ("abc/def/ghi", "abc_def_ghi"),
        # from dot case string
        ("abc.def.ghi", "abc_def_ghi"),
    ],
)
def test_snake_case(input_string, expected_string):
    assert (TypoCase(input_string).snake_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "ABC_DEF_GHI"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "ABC_DEF_GHI"),
        # from pascal case string
        ("AbcDefGhi", "ABC_DEF_GHI"),
        # from camel case string
        ("abcDefGhi", "ABC_DEF_GHI"),
        # from snake case string
        ("abc_def_ghi", "ABC_DEF_GHI"),
        # from constant case string
        ("ABC_DEF_GHI", "ABC_DEF_GHI"),
        # from kebab case string
        ("abc-def-ghi", "ABC_DEF_GHI"),
        # from path case string
        ("abc/def/ghi", "ABC_DEF_GHI"),
        # from dot case string
        ("abc.def.ghi", "ABC_DEF_GHI"),
    ],
)
def test_constant_case(input_string, expected_string):
    assert (TypoCase(input_string).constant_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "abc-def-ghi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "abc-def-ghi"),
        # from pascal case string
        ("AbcDefGhi", "abc-def-ghi"),
        # from camel case string
        ("abcDefGhi", "abc-def-ghi"),
        # from snake case string
        ("abc_def_ghi", "abc-def-ghi"),
        # from constant case string
        ("ABC_DEF_GHI", "abc-def-ghi"),
        # from kebab case string
        ("abc-def-ghi", "abc-def-ghi"),
        # from path case string
        ("abc/def/ghi", "abc-def-ghi"),
        # from dot case string
        ("abc.def.ghi", "abc-def-ghi"),
    ],
)
def test_kebab_case(input_string, expected_string):
    assert (TypoCase(input_string).kebab_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "abc/def/ghi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "abc/def/ghi"),
        # from pascal case string
        ("AbcDefGhi", "abc/def/ghi"),
        # from camel case string
        ("abcDefGhi", "abc/def/ghi"),
        # from snake case string
        ("abc_def_ghi", "abc/def/ghi"),
        # from constant case string
        ("ABC_DEF_GHI", "abc/def/ghi"),
        # from kebab case string
        ("abc-def-ghi", "abc/def/ghi"),
        # from path case string
        ("abc/def/ghi", "abc/def/ghi"),
        # from dot case string
        ("abc.def.ghi", "abc/def/ghi"),
    ],
)
def test_path_case(input_string, expected_string):
    assert (TypoCase(input_string).path_case()) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # from empty string
        ("", ""),
        # from normal case string
        ("abc def ghi", "abc.def.ghi"),
        # from erratic spec chars separated string
        ("  aBc_/_DeF,gHI; ", "abc.def.ghi"),
        # from pascal case string
        ("AbcDefGhi", "abc.def.ghi"),
        # from camel case string
        ("abcDefGhi", "abc.def.ghi"),
        # from snake case string
        ("abc_def_ghi", "abc.def.ghi"),
        # from constant case string
        ("ABC_DEF_GHI", "abc.def.ghi"),
        # from kebab case string
        ("abc-def-ghi", "abc.def.ghi"),
        # from path case string
        ("abc/def/ghi", "abc.def.ghi"),
        # from dot case string
        ("abc.def.ghi", "abc.def.ghi"),
    ],
)
def test_dot_case(input_string, expected_string):
    assert (TypoCase(input_string).dot_case()) == expected_string
