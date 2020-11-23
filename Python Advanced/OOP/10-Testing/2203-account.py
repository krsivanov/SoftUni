class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
            return
        raise ValueError("please use int for amount")

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    # def __getitem__(self, index):
    #     return self._transactions[index]

    def __getitem__(self,inx):
        return self._transactions[inx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __ge__(self, other):
        return self.balance >= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        acc = Account(owner=f"{self.owner}&{other.owner}", amount=self.amount + other.amount)
        acc._transactions.extend(self._transactions + other._transactions)
        return acc



# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
#

import unittest

class TestAcount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Ines", 100)

    def test_add_transactionInvalidType(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction(50.20)

    def test_add_transaction(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account._transactions), 1)

    def test_balance_property(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_validate_transaction_raises_exception_less_than_zero(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, -102)

    def test_validate_transaction(self):
        result = Account.validate_transaction(self.account, 100)
        self.assertEqual(result, "New balance: 200")

    def test_validate_transactions_is_static_method(self):
        import types
        self.assertTrue(isinstance(self.account.validate_transaction,types.FunctionType))

    def test_validate_transaction_invalid_amount_type(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, 50.63)

    def test_custom_str(self):
        result = str(self.account)
        self.assertEqual(result, "Account of Ines with starting amount: 100")

    def test_custom_repr(self):
        result =  repr(self.account)
        self.assertEqual(result, "Account(Ines, 100)")

    def test_custom_len(self):
        self.account.add_transaction(50)
        result = len(self.account)
        self.assertEqual(result, 1)

    def test_custom_iter(self):
        self.account.add_transaction(50)
        self.account.add_transaction(50)
        for t in self.account:
            self.assertEqual(t, 50)

    def test_custom_get_item(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = self.account[1]
        self.assertEqual(result, 150)

    def test_custom_gt(self):
        account_2 = Account("Test", 50)
        self.assertGreater(self.account, account_2)
        self.assertTrue(self.account > account_2)

    def test_custom_ge(self):
        account_2 = Account("Test", 50)
        self.assertGreaterEqual(self.account, account_2)
        self.assertTrue(self.account >= account_2)
        # self.assertEqual(self.account, account_2)

    def test_custom_add(self):
        account_2 = Account('Test', 50)
        account_3 = self.account + account_2
        self.assertEqual(repr(account_3), "Account(Ines&Test, 150)")
        self.assertEqual(account_3.balance, 150)
        self.assertEqual(account_3.owner, "Ines&Test")

    def test_custom_eq(self):
        account_2 = Account("Test", 50)
        self.assertFalse(self.account == account_2)

    def test_custom_reversed(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = list(reversed(self.account))
        self.assertEqual(result, [150, 50])


    def test_custom_ne(self):
        account_2 = Account("Test", 50)
        result = self.account != account_2
        self.assertTrue(result)
        self.assertEqual(self.account.amount, 100)
        self.assertEqual(account_2.amount, 50)


if __name__ == "__main__":
    unittest.main()
