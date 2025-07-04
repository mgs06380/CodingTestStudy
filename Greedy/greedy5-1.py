n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도가 낮은 것부터 하나씩 확인
    count += 1  # 현재 그룹에 해당 모험가를 포함
    if count >= i:  # 현재 그룹에 포함된 모험가 수가 현재 모험가의 공포도 이상이면
        result += 1  # 그룹 결성
        count = 0    # 다음 그룹을 위해 초기화

print(result)
