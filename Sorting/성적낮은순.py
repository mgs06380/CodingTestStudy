n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 이름대신에 점수를 기준으로 정렬
array = sorted(array, key=lambda x: x[1])

# 결과 출력
for x in array:
    print(x[0], end=' ')