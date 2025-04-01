class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        DFS 

        Same as finding islands 
        - In this case islands are accounts 
        - Color is user (known through shared email)
        
        n is #accounts, k is #emails of account
        Time O(nk log_nk): for final sorting, other parts O(nk)
        Space O(nk)
        
        """
        # 1. Build the graph of email -> accounts (of the same user)
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[email].append(i)
                
        # 2. DFS for every groups of accounts
        seen_accounts = set()
        def dfs(i):
            if i in seen_accounts:
                return set()
            seen_accounts.add(i)
            all_emails_of_user = set()
            for email in accounts[i][1:]:
                all_emails_of_user.add(email)
                 # search through other accounts with the same email
                for account in email_to_accounts[email]:
                    all_emails_of_user |= dfs(account) 
            return all_emails_of_user
        
        res = []
        for i, account in enumerate(accounts):
            emails = dfs(i)
            if emails:
                res.append([account[0]] + sorted(list(emails)))
        return res
