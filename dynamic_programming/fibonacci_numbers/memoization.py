def fibo(n):
  return fibo_memo(n, dict())

def fibo_memo(n, dp):
  if n in dp:
    return dp[n]
  if n in [0, 1]:
    dp[n] = n
  else:
    dp[n] = fibo_memo(n - 1, dp) + fibo_memo(n - 2, dp)
  return dp[n]