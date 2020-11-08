from src.money import Dollar


def test_times():
    five_dollar: Dollar = Dollar(5)
    five_dollar.times(2)
    assert five_dollar.amount == 10


if __name__ == '__main__':
    test_times()
