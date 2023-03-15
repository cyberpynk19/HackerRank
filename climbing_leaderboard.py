ranked_count = 6
ranked = [100,90,90,80,75,60]
player_count = 5
player = [50,65,77,90, 102]

##uniq_ranked = list(set(ranked))

def climbingLeaderboard(ranked, player):
    player = player[::-1]
    player_rank = []
    i = 0
    cur = 1
    len_ranked = len(ranked)
    for j in range(len(player)):
        while i < len_ranked and player[j] < ranked[i]:
            if i and ranked[i] == ranked[i-1]:
                print(ranked[i] , ranked[i-1])
                i += 1
                continue
            else:
                i += 1
                cur += 1
        player_rank.append(cur)

    player_rank = player_rank[::-1]
    return player_rank            



            
print(climbingLeaderboard(ranked, player))
    
