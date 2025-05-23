#N = int(input())
N = 4
queen = "Q"
empty = "-"


b = [[empty]*N for i in range(N)]

def isSafe(i, j):
	for p in range(N):
		if b[i][p] == queen or b[p][j] == queen:
			return False
	for n in range(N):
		for m in range(N):
			if i+j == n+m or i-j == n-m:
				if b[n][m] == queen:
					return False
	return True

def nqueen(noq):
	if noq == 0:
		return True
	for i in range(N):
		for j in range(N):
			if b[i][j] != queen and isSafe(i, j):
				b[i][j] = queen
				if nqueen(noq-1) == True:
					return True
				b[i][j] = empty
	return False
def printBoard(b):
	for i in b:
		for j in i:
			print(j, end=" ")
		print()
if nqueen(N):
	printBoard(b)
else:
	print("cannot place")