from bank import value


def test_value_normalization():
    assert value("HELLO") == 0
    assert value("   hello") == 0
    assert value("HEY") == 20
    assert value("   HEY") == 20


def test_value_hello():
    assert value("Hello") == 0
    assert value("Hello, Name") == 0


def test_value_startswith_h():
    assert value("Hey") == 20
    assert value("Hi!") == 20
    assert value("How's it going?") == 20
    assert value("How are you?") == 20


def test_value_other_greetings():
    assert value("What's up?") == 100
    assert value("Greetings") == 100
    assert value("What's happening?") == 100
    assert value("") == 100
