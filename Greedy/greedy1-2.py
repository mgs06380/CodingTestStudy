

n, m, k = map(int, input().split())  #n=배열크기, m=더해지는 횟수, K=더해지는 횟수 제한
data = list(map(int, input().split()))

data.sort()        #1.먼저 입력받은 수들을 정렬
first = data[n-1]  #2.가장 큰 수 (정렬된 배열에서 마지막 index)
second = data[n-2] #3.두 번째로 큰 수 (정렬된 배열에서 마지막에서 두번째 index)

print(data)

result = 0

while True:
    for i in range(k): #원소마다 K번씩 더해저야하니까 반복문 사용
        if m == 0: #m이 0이면 반복문 즉시 탈출 ex) m번 더해지면 계산종료 조건문
            break
        result += first # 6 6 6 5 => 6 6 6 5
        m -= 1 #더할때마다 1 횟수 감소
    if m == 0: break # 5
    result += second #두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)


