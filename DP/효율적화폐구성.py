n, m = map(int, input().split())

c = []
for _ in range(n):
    c.append(int(input()))

def coins(n, m, c):
    dp = [10001] * (m + 1)
    dp[0] = 0  # 0원을 만드는 데 필요한 동전 개수는 0

    for i in range(n):
        for j in range(c[i], m + 1):
            dp[j] = min(dp[j], dp[j - c[i]] + 1)

    if dp[m] == 10001:
        return -1
    else:
        return dp[m]

result = coins(n, m, c)
print(result)
