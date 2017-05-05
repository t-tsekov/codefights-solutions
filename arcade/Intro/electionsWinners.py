def electionsWinners(votes, k):
    count=0
    maxo=max(votes)
    for i in range(len(votes)):
        if votes[i]+k>maxo:
            count+=1
    if k==0 and votes.count(maxo)==1:
        count=1
    return count