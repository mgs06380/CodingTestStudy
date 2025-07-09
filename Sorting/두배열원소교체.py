n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # A는 오름차순 정렬
b.sort(reverse=True) # B는 내림차순 정렬

# 각 배열의 첫 번째 원소끼리 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if  a[i] < b[i]:
        a[i], b[i] = b[i], a[i] # 두 원소 교체
    else:
        break
print(sum(a))