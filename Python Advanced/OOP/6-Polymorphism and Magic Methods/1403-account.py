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
