import pytest

from typocase.string_compounds import StringCompounds as SComps


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", []),
        # null string
        (None, []),
        # special char separator
        ("abc123_def456_ghi789", ["abc123", "def456", "ghi789"]),
        ("abc123/def456/ghi789", ["abc123", "def456", "ghi789"]),
        ("abc123@def456.ghi789", ["abc123", "def456", "ghi789"]),
        # multi special chars separator
        ("abc123_|_def456__@__ghi789", ["abc123", "def456", "ghi789"]),
        # special char separator & leading and trailing special chars
        ("_abc123_def456_ghi789_", ["abc123", "def456", "ghi789"]),
        # special char separator & upper case letters
        ("ABC123_DEF456_GHI789", ["ABC123", "DEF456", "GHI789"]),
        # no special chars
        ("abc123def456ghi789", ["abc123def456ghi789"]),
        # no special chars & uppercase letters
        ("abc123Def456Ghi789", ["abc123Def456Ghi789"])
    ]
)
def test_split_on_special_chars(input_string, expected_string):
    assert SComps(input_string).split_on_special_chars() == expected_string


@pytest.mark.parametrize(
    "input_string, expected_string", [
        # empty string
        ("", []),
        # null string
        (None, []),
        # uppercase letter separator
        ("Abc123Def456Ghi789", ["Abc123", "Def456", "Ghi789"]),
        ("abc123Def456Ghi789", ["abc123", "Def456", "Ghi789"]),
        # uppercase letter separator & leading and trailing special chars
        ("_Abc123Def456Ghi789_", ["Abc123", "Def456", "Ghi789"]),
        # only uppercase letters
        (
            "ABC123DEF456GHI789",
            ["A", "B", "C123", "D", "E", "F456", "G", "H", "I789"]
        ),
        # uppercase letter separator & special char separator
        (
            "A_b_c_1_2_3_D_e_f_4_5_6_G_h_i_7_8_9",
            ["Abc123", "Def456", "Ghi789"]
        ),
        # no uppercase letters
        ("abc123def456ghi789", ["abc123def456ghi789"]),
        # no uppercase letters & special char separator
        ("abc123_def456_ghi789", ["abc123def456ghi789"]),
    ]
)
def test_split_on_uppercase_letters(input_string, expected_string):
    assert SComps(input_string).split_on_uppercase_letters() == expected_string


@pytest.mark.parametrize(
    "input_compounds, expected_compounds", [
        # no compounds
        ([], []),
        # compounds
        (["abc", "def", "ghi"], ["abc", "def", "ghi"]),
        # compounds & empty compounds
        (["", "abc", "", "def", "", "ghi", ""], ["abc", "def", "ghi"]),
        # compounds & uppercase letters
        (["Abc", "Def", "Ghi"], ["Abc", "Def", "Ghi"]),
        # compounds & empty compounds & uppercase letters
        (["", "Abc", "", "Def", "", "Ghi"], ["Abc", "Def", "Ghi"]),
        # only empty compounds
        (["", "", ""], []),
    ]
)
def test_trim(input_compounds, expected_compounds):
    assert SComps.trim(input_compounds) == expected_compounds
