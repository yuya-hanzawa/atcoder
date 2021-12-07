# 計算量 im-place(追加で外部メモリが必要か) 安定性

# 投入ソート(insertion_sort)
# O(N**2) in-plac ◯ 安定性 ◯
def insertion_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp
    return nums

# マージソート
# O(NlogN) in-place × 安定性 ◯
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

# クイックソート
# O(NlogN) in-place ◯ 安定性 ×
def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

# バケットソート
# 整数でしか使えない
def bucket_sort(arr):
  arrc = [0]*(max(arr)+1)
  for i in arr:
    arrc[i] += 1
  ans=[]
  for j in range(1, len(arrc)):
    ans.extend([j]*arrc[j])
  return ans 
