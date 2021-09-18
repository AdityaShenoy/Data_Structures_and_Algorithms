def ceiling(a, key):
  if key > a[-1]:
    return
  l, r = 0, len(a) - 1
  while (l + 1) < r:
    mid = (l + r) // 2
    if key == a[mid]:
      return key
    if key > a[mid]:
      l = mid + 1
    else:
      r = mid
  return a[l] if key <= a[l] else a[r]

a = [1, 3, 4, 7, 8, 12, 15, 17, 19]
for i in range(21):
  print(i, ceiling(a, i), a)