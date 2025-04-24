def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  print(f"Left: {left}, Right: {right}")
  return merge(left, right)

def merge(left, right):
  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  merged += left[i:]
  print(f"Merged Left: {merged}")
  merged += right[j:]
  print(f"Merged Right: {merged}")    
  return merged

merge_sort([38, 27, 43, 3, 9, 82, 10])