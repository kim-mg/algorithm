import sys
input = sys.stdin.readline

def solution(n, k, l):
	m = l[k]
	for i in range(k+1, n+1):
		t = l[i] - l[i-k]
		m = t if t > m else m
	print(m)

# =======================================================
# best time
def solve(n,k,arr):
    temp=sum(arr[:k+1])
    ans=temp

    for i in range(k+1,n+1):
        temp+=arr[i]
        temp-=arr[i-k]
        if temp>ans:
            ans=temp
    return ans if n!=k else temp

if __name__ == "__main__":
	n, k = map(int, input().split())
	l = [0]
	for i in map(int, input().split()):
		l.append(l[-1] + i)
	solution(n, k, l)