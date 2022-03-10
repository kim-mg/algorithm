import sys
input = sys.stdin.readline

def calcul_price(dice_lst):
	dices = [0] * 6
	for dice in dice_lst:
		dices[dice - 1] += 1
	for i in range(len(dices)):
		if dices[i] > 2:
			return 10000 + (i + 1) * 1000
		if dices[i] > 1:
			return 1000 + (i + 1) * 100
		if dices[i] == 1:
			rtn = (i + 1) * 100
	return rtn
    
if __name__ == "__main__":
	dices = list(map(int, input().split()))
	print(calcul_price(dices))