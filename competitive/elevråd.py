N, K = map(int, input().split())

votes = []

for i in range(K):
    votes.append(int(input()))

more_votes = [i for i in votes if i >= votes[0]]

i = 0

while max(more_votes) > more_votes[0]:
    diff = round((more_votes[0] + max(more_votes)) / 2) - more_votes[0]
    more_votes[0] += diff
    more_votes[more_votes.index(max(more_votes))] -= diff
    i += diff

print(i)
