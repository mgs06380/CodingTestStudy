n,k = map(int, input().split())
result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k # 만약 25 3 이면 8 * 3 = 24 즉 k로 나누기위한 최대 배수가 24인 숫자를 target에 지정
    result += (n - target) # 25 - 24 = 1 즉 1번의 빼기가 필요하니 result 1증가
    n = target
    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)