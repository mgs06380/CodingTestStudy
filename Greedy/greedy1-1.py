n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


#화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)
#시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받는다.