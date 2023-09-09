from collections import defaultdict
from itertools import permutations

# Utility function to count frequencies and checking whether letter can make a palindrome or not
def isPalin(s, freq):
	# Initialising frequency array with all zeros
	freq.clear()
	for i in range(26):
		freq[chr(ord('a')+i)] = 0
	l = len(s)

	# Updating frequency according to given string
	for i in range(l):
		freq[s[i]] += 1

	odd = 0

	# Loop to count total letter with odd frequency
	for i in range(26):
		if freq[chr(ord('a')+i)] % 2 == 1:
			odd += 1

	# Palindrome condition :
	# if length is odd then only one letter's frequency must be odd
	# if length is even no letter should have odd frequency
	return (l % 2 == 1 and odd == 1) or (l % 2 == 0 and odd == 0)

# Utility function to reverse a string
def reverse(s:str)->str:
	return s[::-1]

# Function to print all possible palindromes by letter of given string
def printAllPossiblePalindromes(s:str)->None:
	freq = defaultdict(int)

	# checking whether letter can make palindrome or not
	if not isPalin(s, freq):
		return

	l = len(s)

	# half will contain half part of all palindromes,
	# that is why pushing half freq of each letter
	half = ""
	oddC = ''
	for i in range(26):
		if freq[chr(ord('a')+i)] % 2 == 1:
			oddC = chr(ord('a')+i)
		half += freq[chr(ord('a')+i)] // 2 * chr(ord('a')+i)

	# palin will store the possible palindromes one by one
	palin = ""

	# Now looping through all permutation of half, and adding
	# reverse part at end.
	# if length is odd, then pushing oddCharacter also in mid
	xd=set()
	for p in permutations(half):
		palin = ''.join(p)
		if l % 2 == 1:
			palin += oddC
		palin += reverse(''.join(p))
		if palin not in xd:
			print(palin)
			xd.add(palin)

# Driver Program to test above function
if __name__ == "__main__":
	s = "aabbcadad"
	print(f"All palindrome permutations of {s}")
	printAllPossiblePalindromes(s)
