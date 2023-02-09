# Shortest Common Supersequence Problem

def SCSLength(X, Y, m, n):
 
	# if we have reached the end of either sequence, return
	# length of other sequence
	if m == 0 or n == 0:
		return n + m
 
	# if last character of X and Y matches
	if X[m - 1] == Y[n - 1]:
		return SCSLength(X, Y, m - 1, n - 1) + 1
 
	# last character of X and Y don't match
	return min(SCSLength(X, Y, m, n - 1) + 1, SCSLength(X, Y, m - 1, n) + 1)
 
S1 = "ABCBDAB"
S2 = "BDCABA"
 
print(SCSLength(S1, S2, len(S1), len(S2))) #9