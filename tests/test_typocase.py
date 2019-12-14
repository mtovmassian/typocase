from typocase.typocase import TypoCase


def test_extract_compounds_non_alnum_sep():
    assert (
        TypoCase("abc_def_ghi").extract_compounds_specchar_sep()
    ) == ["abc", "def", "ghi"]

    assert (
        TypoCase("ABC_DEF_GHI").extract_compounds_specchar_sep()
    ) == ["abc", "def", "ghi"]

    assert (
        TypoCase("__abc__def__ghi__").extract_compounds_specchar_sep()
    ) == ["abc", "def", "ghi"]

    assert (
        TypoCase("abc.def.ghi").extract_compounds_specchar_sep()
    ) == ["abc", "def", "ghi"]

    assert (
        TypoCase("abcdefghi").extract_compounds_specchar_sep()
    ) == ["abcdefghi"]
