from CurrencyClass import Currency as Cur


class Currency(Cur):

    """
    TODO
    functions:
    property(currency)
    history()
    """
    
    def __init__(self, source):
        self.__currency = []
        self.source = source

    @property
    def currency(self):
        if not self.__currency:
            self.__currency.append(self.source)
        return self.__currency[-1]

    @currency.setter
    def currency(self, value):
        self.__currency.append(value)

    def history(self):
        return self.__currency


if __name__ == '__main__':
    c = Currency()
    c.currency = 1
    print(c.currency)
    c.currency = 1
    c.currency = 2
    print(c.currency)
    print(c.history())
    
