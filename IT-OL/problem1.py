N = int(input())

nums = []

for i in range(N):
    nums.append(int(input()))


def lowestNum(lst):
    for n in sorted(lst):
        if lst.count(n) == 1:
            return n

    return -1


print(lowestNum(nums))
