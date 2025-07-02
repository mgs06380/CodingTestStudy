

n, m, k = map(int, input().split())  #n=배열크기, m=더해지는 횟수, K=더해지는 횟수 제한
data = list(map(int, input().split()))

data.sort()        #1.먼저 입력받은 수들을 정렬
first = data[n-1]  #2.가장 큰 수 (정렬된 배열에서 마지막 index)
second = data[n-2] #3.두 번째로 큰 수 (정렬된 배열에서 마지막에서 두번째 index)

#가장 큰 수가 더해지는 횟수 계산
#반복되는 수열의 길이 (k + 1) = 4
#수열이 반복되는 횟수 M / (K + 1) = 2
#가장 큰 수가 등장하는 횟수 M / (K + 1) * K = 6
count = int(m / (k + 1)) * k
count += m % (k + 1) #M이 (k+1)로 나누어 떨어지지 않는경우

# int(M / (k + 1)) * k + M % (K + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)


