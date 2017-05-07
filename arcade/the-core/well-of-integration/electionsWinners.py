def electionsWinners(votes, k):
    M = max(votes)

    if not k:
        return 1 if votes.count(M) == 1 else 0
    res = 0
    for v in votes:
        if v + k > M:
            res += 1
    return res