class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        """
        Time O(sort)
        Space O(sort)
        
        """
        
        # sort by the (cur energy left after this task) in descending order 
        tasks.sort(key=lambda t:(t[1]-t[0]), reverse = True)
        
#         Just sorting by the begin energy requirement is wrong:
#         [[1,3],[2,4],[10,11],[10,12],[8,9]]

#         tasks.sort(key=lambda t:t[1], reverse = True)
        
#         10 12                     1 3
#         cur_energy 2              cur_energy 2
#         min_energy 12             min_energy 3 

#         10 11                     2 4
#         cur_energy 1              cur_energy 2
#         min_energy 21             min_energy 5 

#         8 9                       10 12
#         cur_energy 1              cur_energy 2
#         min_energy 29             min_energy 15 

#         2 4                       10 11
#         cur_energy 2              cur_energy 1
#         min_energy 32             min_energy 24 

#         1 3                       8 9
#         cur_energy 2              cur_energy 1
#         min_energy 33             min_energy 32 
        
        min_energy = 0
        cur_energy = 0

        for cost, begin in tasks:
            
            # don't have enough energy to start
            if begin > cur_energy:
                need = begin - cur_energy
                min_energy += need
                cur_energy += need
            
            # do the current task
            cur_energy -= cost
            
        return min_energy
