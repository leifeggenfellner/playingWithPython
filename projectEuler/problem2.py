prevNum = 0
num = 1

sum = 0

while(1):
    temp = num
    num += prevNum
    prevNum = temp

    if num > 4 * 10**6:
        break
    else:
        if num % 2 == 0:
            sum += num

print(sum)
