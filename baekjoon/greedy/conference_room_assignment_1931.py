import sys
input = sys.stdin.readline

# ==========================================================
# basic greedy
def solution(lst, n):
	cnt = 0
	end = 0
	for t in lst:
		if t[0] >= end:
			end = t[1]
			cnt += 1
	return cnt

# ==========================================================
# best time greedy
# time ==> 'basic / 2' normally

def solution_2():
    n=int(input())
    dic={}
    trash=0
    ltrash={}
    for i in range(n):
        a,b=map(int, input().split())
        if a not in dic and b!=a: dic[a]=b
        elif b==a:
            trash+=1
            if b not in ltrash: ltrash[b]=0
        elif dic[a]>b and b!=a: dic[a]=b 
    for e in ltrash:
        if e not in dic:
            dic[e]=e
            trash-=1
    arr=list(dic)
    arr.sort()
    tmp=dic[arr[0]]
    cnt=1
    for i in range(1,len(arr)):
        if tmp>dic[arr[i]]:
            tmp=dic[arr[i]]
        else:
            if arr[i]>=tmp:
                cnt+=1
                tmp=dic[arr[i]]
    print(cnt+trash)

if __name__ == "__main__":
	n = int(input())
	lst = []
	for _ in range(n):
		lst.append(list(map(int, input().split())))
	lst = sorted(lst, key=lambda x:(x[1], x[0]))
	print(solution(lst, n))
