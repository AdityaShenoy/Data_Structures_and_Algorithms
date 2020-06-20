def fibo(n):
  if n in [0, 1]:
    return n
  dp = [0, 1]
  for i in range(2, n+1):
    dp.append(dp[-1] + dp[-2])
    del dp[0]
  return dp[-1]