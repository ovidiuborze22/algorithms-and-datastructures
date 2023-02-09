# Diff Utility

def LCSLength(S1, S2, m, n, lookup):
	for i in range(m + 1):
		lookup[i][0] = 0
	for j in range(n + 1):
		lookup[0][j] = 0
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if S1[i - 1] == S2[j - 1]:
				lookup[i][j] = lookup[i - 1][j - 1] + 1
			else:
				lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

# Function to display the differences between two Strings
def diff(S1, S2, m, n, lookup):
 
	# if last character of S1 and S2 matches
	if m > 0 and n > 0 and S1[m - 1] == S2[n - 1]:
		diff(S1, S2, m - 1, n - 1, lookup)
		print("", S1[m - 1], end='')
 
	# current character of S2 is present not in S1
	elif n > 0 and (m == 0 or lookup[m][n - 1] >= lookup[m - 1][n]):
 
		diff(S1, S2, m, n - 1, lookup)
		print(" +" + S2[n - 1], end='')
 
	# current character of S1 is present not in S2
	elif m > 0 and (n == 0 or lookup[m][n - 1] < lookup[m - 1][n]):
 
		diff(S1, S2, m - 1, n, lookup)
		print(" -" + S1[m - 1], end='')
 
 
 
# Function to fill lookup table by finding the length of LCS
# of subS1[0..m-1] and S2[0..n-1]
def LCSLength(S1, S2, m, n, lookup):
 
	# first column of the lookup table will be all 0
	for i in range(m + 1):
		lookup[i][0] = 0
 
	# first row of the lookup table will be all 0
	for j in range(n + 1):
		lookup[0][j] = 0
 
	# fill the lookup table in bottom-up manner
	for i in range(1, m + 1):
 
		for j in range(1, n + 1):
			# if current character of S1 and S2 matches
			if S1[i - 1] == S2[j - 1]:
				lookup[i][j] = lookup[i - 1][j - 1] + 1
				# else if current character of S1 and S2 don't match
			else:
				lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
 
 
S1 = "ABCDFGHJQZ"
S2 = "ABCDEFGIJKRXYZ"
 
		# lookup[i][j] stores the length of LCS of subS1[0..i-1], S2[0..j-1]
lookup = [[0 for x in range(len(S2) + 1)] for y in range(len(S1) + 1)]
 
		# fill lookup table
LCSLength(S1, S2, len(S1), len(S2), lookup)
 
		# find difference
 
diff(S1, S2, len(S1), len(S2), lookup)
 