import pytest

from typocase.string_compounds import StringCompounds as SComps


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", []),
        # null string
        (None, []),
        # one specchar spaced
        ("abc_def_ghi", ["abc", "def", "ghi"]),
        ("abc/def/ghi", ["abc", "def", "ghi"]),
        ("abc@def.ghi", ["abc", "def", "ghi"]),
        # multi specchars spaced
        ("abc_|_def__@__ghi", ["abc", "def", "ghi"]),
        # specchar spaced & leading and trailing specchars
        ("_abc_def_ghi_", ["abc", "def", "ghi"]),
        # specchar spaced & upper case letters
        ("ABC_DEF_GHI", ["abc", "def", "ghi"]),
        # no specchars
        ("abcdefghi", ["abcdefghi"]),
        # no specchars & uppercase letters
        ("abcDefGhi", ["abcdefghi"])
    ]
)
def test_extract_by_specchar_sep(input_string, expected_string):
    assert SComps(input_string).extract_by_specchar_sep() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", []),
        # null string
        (None, []),
        # uppercase letter spaced
        ("AbcDefGhi", ["abc", "def", "ghi"]),
        ("abcDefGhi", ["abc", "def", "ghi"]),
        # uppercase letter spaced & leading and trailing specchars
        ("_AbcDefGhi_", ["abc", "def", "ghi"]),
        # only uppercase letters
        ("ABCDEFGHI", ["a", "b", "c", "d", "e", "f", "g", "h", "i"]),
        # uppercase letter spaced & specchar spaced
        ("A_b_c_D_e_f_G_h_i", ["abc", "def", "ghi"]),
        # no uppercase letters
        ("abcdefghi", ["abcdefghi"]),
        # no uppercase letters & specchar spaced
        ("abc_def_ghi", ["abcdefghi"]),
    ]
)
def test_extract_by_uppercase_sep(input_string, expected_string):
    assert SComps(input_string).extract_by_uppercase_sep() == expected_string


@pytest.mark.parametrize(
    "input_compounds, expected_compounds", [
        # no compounds
        ([], []),
        # compounds
        (["abc", "def", "ghi"], ["abc", "def", "ghi"]),
        # compounds & empty compounds
        (["", "abc", "", "def", "", "ghi", ""], ["abc", "def", "ghi"]),
        # compounds & uppercase letters
        (["Abc", "Def", "Ghi"], ["abc", "def", "ghi"]),
        # compounds & uppercase letters & empty compounds
        (["", "Abc", "", "Def", "", "Ghi"], ["abc", "def", "ghi"]),
        # only empty compounds
        (["", "", ""], []),
    ]
)
def test_trim(input_compounds, expected_compounds):
    assert SComps.trim(input_compounds) == expected_compounds
