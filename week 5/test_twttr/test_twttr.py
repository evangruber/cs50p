from twttr import shorten

def test_shorten_word_lowercase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("sequoia") == "sq"


def test_shorten_sentence_lowercase():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("The quick brown fox jumps over the lazy dog.") == "Th qck brwn fx jmps vr th lzy dg."


def test_shorten_word_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("SEQUOIA") == "SQ"


def test_shorten_mixed_case():
    assert shorten("TwItTer") == "TwtTr"
    assert shorten("sEQuOia") == "sQ"


def test_shorten_sentence_uppercase():
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"
    assert shorten("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.") == "TH QCK BRWN FX JMPS VR TH LZY DG."


def test_shorten_punctuation_symbols():
    assert shorten(".,!?/';:)(") == ".,!?/';:)("
    assert shorten("@#$%&") == "@#$%&"


def test_shorten_numbers():
    assert shorten("0123456789") == "0123456789"
    assert shorten("CS50") == "CS50"


def test_shorten_no_input():
    assert shorten("") == ""
