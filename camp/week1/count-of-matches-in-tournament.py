class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_advanced_teams=0
        while(n!=1):
            number_of_last_advanced_team=0
            if(n%2==1):
                number_of_last_advanced_team=1
            n//=2
            number_of_last_advanced_team+=n
            total_advanced_teams+=number_of_last_advanced_team
        return total_advanced_teams


