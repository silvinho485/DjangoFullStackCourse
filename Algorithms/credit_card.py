class CCard(object):

    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

    def __str__(self):
        return ("Customer: | {}\n"
                "Bank:     | {}\n"
                "Account:  | {}\n"
                "Limit:    | {}\n"
                "Balance:  | {}").format(self._customer,
                                       self._bank,
                                       self._account,
                                       self._limit,
                                       self._balance)


if __name__ == '__main__':
    cc = CCard("Silvio", "Itau", "30128-6", 600)
    cc.charge(324)
    print(cc)
