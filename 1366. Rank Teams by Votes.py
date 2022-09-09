class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        """
        Dictionary - team: [votes]
        Sort by votes
        
        """
        n = len(votes[0])
        team_votes = {}
        
        for vote in votes:
            for i, team in enumerate(vote):
                if team not in team_votes:
                    team_votes[team] = [0] * n
                team_votes[team][i] += 1

        teams = sorted(team_votes.keys()) # sort alphabetically
        ranked = sorted(teams, key=lambda x: team_votes[x], reverse=True) # sort by list of votes, most to least
        
        return "".join(ranked)
