import heapq

# 인구수, 센티의 키, 망치 횟수
population, height, count = map(int,input().split())
heap=[]
for i in range(population):
    heapq.heappush(heap,-int(input())) # 음수로 변환하여 최소 힙을 최대 힙처럼 사용

# 때린 횟수
hammer=0

while hammer < count: 
    max_num= -heapq.heappop(heap) # 힙에서 꺼내고 다시 양수로 반환

    # 제일 큰 거인의 키가 센티보다 작거나, 1이면 망치질 할 필요 없으니까 break
    if height > max_num or max_num == 1:
        heapq.heappush(heap,-max_num)
        break
    
    # 가장 큰 키 절반으로 줄이고, 횟수 늘리고, 음수로 반환해서 다시 넣기
    max_num //= 2
    hammer += 1
    heapq.heappush(heap,-max_num)

max_num= -heapq.heappop(heap)

if height > max_num: # 모든 거인이 센티보다 키가 작으면 때린 횟수 출력
    print(f'YES\n{hammer}')
else: # 아니면 가장 큰 거인의 키 출력
    print(f'NO\n{max_num}')