def binary_search(a, key):
  l, r = 0, len(a) - 1
  while l <= r:
    mid = (l + r) // 2
    if key == a[mid]:
      return mid
    if key < a[mid]:
      r = mid - 1
    else:
      l = mid + 1
  return -1

a = [1, 3, 4, 7, 8, 12, 15, 17, 19]
for i in range(21):
  print(i, binary_search(a, i), a)