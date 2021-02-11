def isPalindrome(x):
	num = str(x)
	result = True
	i = 0
	j = len(num) - 1

	while (i < j and result):
		result = num[i] == num[j]
		i += 1
		j -= 1

	return result

def find(nDigits):

	lowerBound = pow(10, nDigits - 1)

	upperBound = (lowerBound * 10) - 1

	resultP = 0
	resultQ = 0
	resultR = 0

	for p in range(upperBound, 
				lowerBound, -11):

		while (p % 11 != 0):
			p -= 1

		for q in range(upperBound, 
					lowerBound, -1):
			t = p * q

			if (t > resultR and
				isPalindrome(t)):
				resultP = p
				resultQ = q
				resultR = t
				break

	print(resultR)

user_input = 4
find(user_input)