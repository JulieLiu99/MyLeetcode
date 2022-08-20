class ATM:
    # 20, 50, 100, 200, 500
    
    # Time O(n)
    # Space O(n)

    def __init__(self):
        self.banknotes = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, n in enumerate(banknotesCount):
            self.banknotes[i] += n


    def withdraw(self, amount: int) -> List[int]:
        result = []
        # withdraw from the biggest notes
        for val, n in zip(self.values[::-1], self.banknotes[::-1]):
            need = min(n, amount // val)
            result = [need] + result
            amount -= (need * val)
        # we reduce only if withdrawal was successful
        if amount == 0:
            self.deposit([-x for x in result])
            return result
        else:
            return [-1]



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)