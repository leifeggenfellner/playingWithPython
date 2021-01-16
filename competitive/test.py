
import heapq
from itertools import permutations
from collections import Counter
import datetime

# alphabets = [str(x)for x in range(10000000)]
# a = datetime.datetime.now()  # store initial time
# for item in alphabets:
#     len(item)
# b = datetime.datetime.now()  # store final time
# print((b-a).total_seconds())  # results
# a = datetime.datetime.now()
# length = len                    # function stored locally
# for item in alphabets:
#     length(item)
# b = datetime.datetime.now()
# print((b-a).total_seconds())


# perm = permutations([1, 2, 3], 2)
# for i in list(perm):
#     print(i)


# Code to find top 3 elements and their counts
# using most_common
# arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5, 6, 6, 6, 6]
# counter = Counter(arr)
# count = counter.most_common()
# top_three = counter.most_common(3)
# print(count)
# print(top_three)


# Python code to find 3 largest and 4 smallest
# elements of a list.
# grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
# print(heapq.nlargest(3, grades))
# print(heapq.nsmallest(4, grades))


# Python code to demonstrate use of zip.
# stocks = {
#     'Goog': 520.54,
#     'FB': 76.45,
#     'yhoo': 39.28,
#     'AMZN': 306.21,
#     'APPL': 99.76
# }

# zipped_1 = zip(stocks.values(), stocks.keys())

# sorting according to values
# print(sorted(zipped_1))

# zipped_2 = zip(stocks.keys(), stocks.values())
# print(sorted(zipped_2))
# sorting according to keys


# Python code to apply a function on a list
# income = [10, 30, 75]


# def double_money(dollars):
#     return dollars * 2


# new_income = list(map(double_money, income))
# print(new_income)


# string = ""
# lst = ["I", "Simp", "For", "Patrick"]
# for i in lst:
#     string += i
# print(string)


# lst = ["I", "Simp", "For", "Patrick"]
# string = ''.join(lst)
# print(string)

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


list = [1, 2, 3, 4, 5, 6, 6]

print(second_largest(list))
