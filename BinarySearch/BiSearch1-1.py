def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)   # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)     # 중간점의 값보다 찾고자 하는 값이 클 경우 오른쪽 확인

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('Not found')
else:
    print(result + 1)