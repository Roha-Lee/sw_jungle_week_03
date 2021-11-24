# 19	2294	상	BFS	동전 2
'''문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다.
(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''
###궁금증--!!
##!! visited 를 set으로 만들어서 not in 으로 확인할 때 set에서 찾는게 속도에 엄청난 엄향을 주었다.
# - set 은 hash 형태 -> 값으로 검색할때 하나 하나 탐색하는 것이 아니라 해쉬를 통해 해당 주소로 바로 접근할 수 있음!! O(1)
## K와 같은 값일 때마다 cnt의 최솟값을 최신화 해주지 않고 바로 함수를 종료 사켜도 통과된다. 심지어 정렬을 해주지 않은 상태로 큐에 넣어도 마찬가지다.
# 동전 조합의 개수가 while 한번 마다 늘어나기 때문에 cost == K 당시의 cnt가 가장 적은 동전의 개수기 때문에 바로 종료해도 된다.
from sys import stdin
from collections import deque 
def BFS(coin,K):
    # 큐에 코인별로 한개 씩 (1,coin[i]) 넣어준다
    q = deque([(1,c) for c in coin])
    # 시도했던(방문했던) 동전의 합 확인하는 set - set으로 만들어야 if 문에서 not in 검사할 때 리스트보다 훨씬 빠르다
    visited = set([x for x in coin])
    while q:
        # 현재 cost와 cost를 만들때 사용한 동전의 합 - cnt
        cnt, cost = q.popleft()
        # 현재 cost가 K와 같으면 조합에 필요했던 동전의 개수 출력
        if cost == K:
            print(cnt)
            return
        # 아니면 현재 cost의 동전 하나씩 추가 반복
        for c in coin:
            sum = cost + c
            # 현재 cost에 동전을 추가한 값, sum이 K보다 크지 않고 큐에 들어갔던 적(방문했던 적)이
            # 없다면 방문 set에 sum을 추가하고 큐에 sum과 sum을 만드는데 필요한 동전의 개수를 추가
            if sum <= K and sum not in visited:
                visited.add(sum)
                q.append([cnt+1, sum])
    # K가 되는 조합을 찾지 못하고 q가 비어서 반복이 끝났다면(=모든 동전의 조합을 확인했다면) -1 출력
    print(-1)
    return
    
# 동전의 개수 - N, 만들어야 할 동전의 합 - K
N, K = [int(x) for x in stdin.readline().split()]
#동전의 가치 - coin, 중복없이 set으로
coin = set()
for _ in range(N):
    tmp = int(stdin.readline())
    if tmp <= K:
        coin.add(tmp)

#BFS 시작
BFS(coin,K)