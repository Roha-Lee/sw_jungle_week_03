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
##!! visited 를 set으로 만들어서 not in 으로 확인할 때 set에서 찾는게 속도에 엄청난 엄향을 주었다. 이유는 모르겠다. 
# - set 은 hash 형태 -> 값으로 검색할때 하나 하나 탐색하는 것이 아니라 해쉬를 통해 해당 주소로 바로 접근할 수 있음!! O(1)
## K와 같은 값일 때마다 cnt의 최솟값을 최신화 해주지 않고 바로 함수를 종료 사켜도 통과된다. 심지어 정렬을 해주지 않은 상태로 큐에 넣어도 마찬가지다. 이유는?!!
# 동전 조합의 개수가 while 한번 마다 늘어나기 때문에 cost == K 당시의 cnt가 가장 적은 동전의 개수기 때문에 바로 종료해도 된다.

from sys import stdin
from collections import deque 

def BFS(coin,K):
    q = deque([(1,c) for c in coin])
    visited = set([x for x in coin])

    while q:
        cnt, cost = q.popleft()
        if cost == K:
            print(cnt)
            return
        for c in coin:
            sum = cost + c
            if  sum <= K and sum not in visited:
                visited.add(sum)
                q.append([cnt+1, sum])

    print(-1)
    return
    

N, K = [int(x) for x in stdin.readline().split()]

coin = set()
for _ in range(N):
    tmp = int(stdin.readline())
    if tmp <= K:
        coin.add(tmp)

# coin = sorted(list(coin), reverse=True)

BFS(coin,K)