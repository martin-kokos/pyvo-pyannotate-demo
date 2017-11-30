import flipper


def test_flip():
    # assert <statement>, 'Info message in case of failure of statement'
    assert flipper.flip('John') == 'nhoJ'
