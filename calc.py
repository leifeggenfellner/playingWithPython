import math

k_e = 8.99 * 10 ** 9

t = 2*(7.425*10**-13-3.5*10**-13)
n = 6.6*10**-27

a = math.sqrt(t / n)
print(a)
print("{:e}".format(a))
