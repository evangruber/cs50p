from plates import is_valid


def test_is_valid_plate_length():
    assert not is_valid("")
    assert not is_valid("C")
    assert is_valid("CS")
    assert is_valid("CSPYTH")
    assert not is_valid("CSPYTHO")


def test_is_valid_first_two_isalpha():
    assert is_valid("CS")
    assert is_valid("CSP")
    assert is_valid("CS5")
    assert not is_valid("5CSP")
    assert not is_valid("C5PY")
    assert not is_valid("50")


def test_is_valid_no_punctuation():
    assert not is_valid("CS5!)")
    assert not is_valid("CSP.2/")
    assert not is_valid("CS,PY")


def test_is_valid_no_whitespace():
    assert not is_valid("  CSP")
    assert not is_valid("CSP  ")
    assert not is_valid(" CSP ")


def test_is_valid_digit_started_nonzero():
    assert is_valid("CS50")
    assert is_valid("CS500")
    assert not is_valid("CS05")


def test_is_valid_digit_started_noalpha():
    assert is_valid("CS5012")
    assert not is_valid("CS50P")
    assert not is_valid("CS50P1")
