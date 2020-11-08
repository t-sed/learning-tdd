from main.money import Dollar

class MoneyTest:
    def test_times(self):
        five_dollar: Dollar = Dollar(5)
        five_dollar.times(2)
        self.assertEqual(five_dollar.amount, 10)

if __name__ == '__main__':
    MoneyTest().test_times()