import sys
input = sys.stdin.readline

n = int(input())
a = 665
while n > 0:
    a += 1
    if str(a).find('666') != -1:
        n -= 1

print(a)

######################################################################
# best

n = int(input())
front = 0
back = 0
fronttemp = 0
backlength = 0
backlimit = 0
pos = -1
state = 'front'


for _ in range(n-1) :
    if state == 'front' :
        front += 1
        pos = str(front*100 + 66).find('666')
        if pos != -1 :
            state = 'back'
            backlength = len(str(front)) - pos
            backlimit = 10**backlength
            fronttemp = front // backlimit
            back = 0
    else :
        back += 1
        if back >= backlimit :
            state = 'front'
            front += 1

if state == 'front' :
    print(front*1000 + 666)
else :
    print((fronttemp*1000 + 666)*backlimit + back)

###########################################################################
# best 2
n = int(input())
if n==1:
    print(666)
else:
    count = 1
    for i in range(2, n+1):
        base_title = "{0}666".format(i-1)
        num_of_extra_six_in_row = 0
        for k in range(len(base_title)-3):
            if base_title[-4-k]=='6':
                num_of_extra_six_in_row += 1
            else:
                break
        count += int(10**num_of_extra_six_in_row)
        if count >= n:
            break
            
    if num_of_extra_six_in_row > 0:
        base = int(10**num_of_extra_six_in_row)
        count -= base
        base_title = int(base_title) - int(base_title)%base + (N - count-1)
        
    print(base_title)