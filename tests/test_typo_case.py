import pytest

from typocase.typo_case import TypoCase
from typocase.models import SpecChars


@pytest.mark.parametrize(
    "input_string, special_char, expected_string", [
        ("", SpecChars.DOT, ""),
        ("abc def ghi", SpecChars.DOT, "abc.def.ghi"),
        ("abc def ghi", SpecChars.DASH, "abc-def-ghi"),
        ("abc def ghi", SpecChars.SLASH, "abc/def/ghi"),
        ("abc def ghi", SpecChars.UNDER_SCORE, "abc_def_ghi"),
        ("abc def ghi", SpecChars.WHITE_SPACE, "abc def ghi")
    ]
)
def test_join_comps_by_special_char(
    input_string, special_char, expected_string
):
    assert (
        TypoCase(input_string).join_comps_by_special_char(special_char)
    ) == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", ""),
        # Null string
        (None, ""),
        # special char separator
        ("abc_def_ghi", "AbcDefGhi"),
        ("abc/def/ghi", "AbcDefGhi"),
        ("abc@def.ghi", "AbcDefGhi"),
        # multi special chars separator
        ("abc_|_def__@__ghi", "AbcDefGhi"),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", "AbcDefGhi"),
        # no special chars
        ("abcdefghi", "abcdefghi"),
        # uppercase letter separator
        ("AbcDefGhi", "AbcDefGhi"),
        ("abcDefGhi", "AbcDefGhi"),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", "AbcDefGhi"),
        # only uppercase letters
        ("ABCDEFGHI", "ABCDEFGHI"),
        # uppercase letter separator & special char separator
        ("ABC_DEF_GHI", "AbcDefGhi"),
        ("A_b_c_D_e_f_G_h_i", "ABCDEFGHI"),
    ]
)
def test_pascal_case(
    input_string, expected_string
):
    assert TypoCase(input_string).pascal_case() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", ""),
        # Null string
        (None, ""),
        # special char separator
        ("abc_def_ghi", "abcDefGhi"),
        ("abc/def/ghi", "abcDefGhi"),
        ("abc@def.ghi", "abcDefGhi"),
        # multi special chars separator
        ("abc_|_def__@__ghi", "abcDefGhi"),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", "abcDefGhi"),
        # no special chars
        ("abcdefghi", "abcdefghi"),
        # uppercase letter separator
        ("AbcDefGhi", "abcDefGhi"),
        ("abcDefGhi", "abcDefGhi"),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", "abcDefGhi"),
        # only uppercase letters
        ("ABCDEFGHI", "aBCDEFGHI"),
        # uppercase letter separator & special char separator
        ("ABC_DEF_GHI", "abcDefGhi"),
        ("A_b_c_D_e_f_G_h_i", "aBCDEFGHI"),
    ]
)
def test_camel_case(
    input_string, expected_string
):
    assert TypoCase(input_string).camel_case() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", ""),
        # Null string
        (None, ""),
        # special char separator
        ("abc_def_ghi", "abc_def_ghi"),
        ("abc/def/ghi", "abc_def_ghi"),
        ("abc@def.ghi", "abc_def_ghi"),
        # multi special chars separator
        ("abc_|_def__@__ghi", "abc_def_ghi"),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", "abc_def_ghi"),
        # no special chars
        ("abcdefghi", "abcdefghi"),
        # uppercase letter separator
        ("AbcDefGhi", "abc_def_ghi"),
        ("abcDefGhi", "abc_def_ghi"),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", "abc_def_ghi"),
        # only uppercase letters
        ("ABCDEFGHI", "a_b_c_d_e_f_g_h_i"),
        # uppercase letter separator & special char separator
        ("ABC_DEF_GHI", "abc_def_ghi"),
        ("A_b_c_D_e_f_G_h_i", "a_b_c_d_e_f_g_h_i"),
    ]
)
def test_snake_case(
    input_string, expected_string
):
    assert TypoCase(input_string).snake_case() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", ""),
        # Null string
        (None, ""),
        # special char separator
        ("abc_def_ghi", "ABC_DEF_GHI"),
        ("abc/def/ghi", "ABC_DEF_GHI"),
        ("abc@def.ghi", "ABC_DEF_GHI"),
        # multi special chars separator
        ("abc_|_def__@__ghi", "ABC_DEF_GHI"),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", "ABC_DEF_GHI"),
        # no special chars
        ("abcdefghi", "abcdefghi"),
        # uppercase letter separator
        ("AbcDefGhi", "ABC_DEF_GHI"),
        ("abcDefGhi", "ABC_DEF_GHI"),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", "ABC_DEF_GHI"),
        # only uppercase letters
        ("ABCDEFGHI", "A_B_C_D_E_F_G_H_I"),
        # uppercase letter separator & special char separator
        ("ABC_DEF_GHI", "ABC_DEF_GHI"),
        ("A_b_c_D_e_f_G_h_i", "A_B_C_D_E_F_G_H_I"),
    ]
)
def test_constant_case(
    input_string, expected_string
):
    assert TypoCase(input_string).constant_case() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", ""),
        # Null string
        (None, ""),
        # special char separator
        ("abc_def_ghi", "abc-def-ghi"),
        ("abc/def/ghi", "abc-def-ghi"),
        ("abc@def.ghi", "abc-def-ghi"),
        # multi special chars separator
        ("abc_|_def__@__ghi", "abc-def-ghi"),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", "abc-def-ghi"),
        # no special chars
        ("abcdefghi", "abcdefghi"),
        # uppercase letter separator
        ("AbcDefGhi", "abc-def-ghi"),
        ("abcDefGhi", "abc-def-ghi"),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", "abc-def-ghi"),
        # only uppercase letters
        ("ABCDEFGHI", "a-b-c-d-e-f-g-h-i"),
        # uppercase letter separator & special char separator
        ("ABC_DEF_GHI", "abc-def-ghi"),
        ("A_b_c_D_e_f_G_h_i", "a-b-c-d-e-f-g-h-i"),
    ]
)
def test_kebab_case(
    input_string, expected_string
):
    assert TypoCase(input_string).kebab_case() == expected_string
