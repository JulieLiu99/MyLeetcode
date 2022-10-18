class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        Store seen transactions grouped by user name
        
        Time O(n^2)
        Space O(n)
        """
        res = set()
        seen = defaultdict(set) # name: [transction]
    
        for i, inf in enumerate(transactions):
            name, time, amount, city = inf.split(",")

            if int(amount) > 1000:
                res.add(i)

            for j, t, c in seen[name]:
                if c != city and abs(int(t) - int(time)) <= 60:
                    res.add(j)
                    res.add(i)

            seen[name].add((i, time, city))

        return [transactions[i] for i in res]
