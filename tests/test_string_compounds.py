import pytest
from typocase.string_compounds import StringCompounds as SComps


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # empty string
        ("", []),
        # null string
        (None, []),
        # special char separator
        ("abc_def_ghi", ["abc", "def", "ghi"]),
        ("abc/def/ghi", ["abc", "def", "ghi"]),
        ("abc@def.ghi", ["abc", "def", "ghi"]),
        # multi special chars separator
        ("abc_|_def__@__ghi", ["abc", "def", "ghi"]),
        # special char separator & leading and trailing special chars
        ("_abc_def_ghi_", ["abc", "def", "ghi"]),
        # special char separator & upper case letters
        ("ABC_DEF_GHI", ["abc", "def", "ghi"]),
        # no special chars
        ("abcdefghi", ["abcdefghi"]),
        # no special chars & uppercase letters
        ("abcDefGhi", ["abcdefghi"]),
    ],
)
def test_split_on_special_chars(input_string, expected_string):
    assert SComps(input_string).split_on_special_chars() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        # empty string
        ("", []),
        # null string
        (None, []),
        # uppercase letter separator
        ("AbcDefGhi", ["abc", "def", "ghi"]),
        ("abcDefGhi", ["abc", "def", "ghi"]),
        # uppercase letter separator & leading and trailing special chars
        ("_AbcDefGhi_", ["abc", "def", "ghi"]),
        # only uppercase letters
        ("ABCDEFGHI", ["a", "b", "c", "d", "e", "f", "g", "h", "i"]),
        # uppercase letter separator & special char separator
        ("A_b_c_D_e_f_G_h_i", ["abc", "def", "ghi"]),
        # no uppercase letters
        ("abcdefghi", ["abcdefghi"]),
        # no uppercase letters & special char separator
        ("abc_def_ghi", ["abcdefghi"]),
    ],
)
def test_split_on_uppercase_letters(input_string, expected_string):
    assert SComps(input_string).split_on_uppercase_letters() == expected_string


@pytest.mark.parametrize(
    "input_compounds, expected_compounds",
    [
        # no compounds
        ([], []),
        # compounds
        (["abc", "def", "ghi"], ["abc", "def", "ghi"]),
        # compounds & empty compounds
        (["", "abc", "", "def", "", "ghi", ""], ["abc", "def", "ghi"]),
        # compounds & uppercase letters
        (["Abc", "Def", "Ghi"], ["abc", "def", "ghi"]),
        # compounds & empty compounds & uppercase letters
        (["", "Abc", "", "Def", "", "Ghi"], ["abc", "def", "ghi"]),
        # only empty compounds
        (["", "", ""], []),
    ],
)
def test_trim(input_compounds, expected_compounds):
    assert SComps.trim(input_compounds) == expected_compounds
