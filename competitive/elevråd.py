import math

N, K = map(int, input().split())

votes = []

for i in range(K):
    votes.append(int(input()))


def second_largest(lst):
    count = 0
    m1 = m2 = float('-inf')
    for x in lst:
        count += 1
        if x > m2:
            if x > m1:
                m1, m2 = x, m1
            elif x == m1:
                continue
            else:
                m2 = x
    return m2 if count >= 2 else None


more_votes = [i for i in votes if i >= votes[0]]

j = 0

while votes[0] < max(votes):
    difference = max(votes) - second_largest(votes)
    if votes[0] + difference <= max(votes) - difference:
        votes[0] += difference
        votes[votes.index(max(votes))] -= difference
        j += difference
    elif votes[0] + difference > max(votes) - difference:
        votes[0] += math.ceil(difference / 2)
        votes[votes.index(max(votes))] -= math.ceil(difference / 2)
        j += math.ceil(difference / 2)


print(j)
