class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        DFS 
        
        Time O(n) 
        Space O(n)
        
        """
        # 1. Build the graph of email -> all accounts accociated with the email owner
        
        email_to_account = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)
                
        # 2. DFS for every account, find all emails accociated with the account user
        merged_accounts = set()
        def dfs(i):
            if i in merged_accounts:
                return set()
            merged_accounts.add(i)
            emails_of_accountUser = set()
            for email in accounts[i][1:]:
                emails_of_accountUser.add(email)
                for account in email_to_account[email]: # other accounts this email links to 
                    emails_of_accountUser |= dfs(account)  # add their associated emails too
                    # same as: emails_of_accountUser  = emails_of_accountUser.union(dfs(account))
            return emails_of_accountUser
        
        res = []
        for i, account in enumerate(accounts):
            emails = dfs(i)  # find all emails belonging to the same account
            if emails:
                res.append([account[0]] + sorted(list(emails)))
        return res
