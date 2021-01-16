N, K, X_g = map(int, input().split())

addresses = []

for i in range(N):
    addresses.append(int(input()))

length = 0

while len(addresses) > 0:
    if len(addresses) >= K:
        eastmost = addresses[:K]
        del addresses[:K]

        if min(eastmost) > X_g:
            length += (max(eastmost) - X_g) * 2
        elif max(eastmost) < X_g:
            length += (X_g - min(eastmost)) * 2
        elif max(eastmost) > X_g and min(eastmost) < X_g:
            length += (max(eastmost) - X_g) + (max(eastmost) -
                                               min(eastmost)) + (X_g - min(eastmost))

    elif len(addresses) < K:
        eastmost = addresses[:len(addresses)]
        del addresses[: len(addresses)]

        if min(eastmost) > X_g:
            length += (max(eastmost) - X_g) * 2
        elif max(eastmost) < X_g:
            length += (X_g - min(eastmost)) * 2
        elif max(eastmost) > X_g and min(eastmost) < X_g:
            length += (max(eastmost) - X_g) + (max(eastmost) -
                                               min(eastmost)) + (X_g - min(eastmost))

print(length)
