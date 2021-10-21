# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
print("1.")

def lesser_of_two_evens(a, b):
	if a%2==0 and b%2==0:
		if a<b:
			return a
		else:
			return b
	else:
		if a>b:
			return a
		else:
			return b

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

print("\n")

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
print("2.")

def animal_crackers(text):
	a = text.split()
	if a[0][0] == a[1][0]:
		return True
	else:
		return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

print("\n")

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
print("3.")

def old_macdonald(name):
	firstCap = name[0:1].upper()
	secCap = name[3:4].upper()
	name = firstCap + name[1:3] + secCap + name[4:]
	return name

print(old_macdonald('macdonald'))

print("\n")

# MASTER YODA: Given a sentence, return a sentence with the words reversed
print("4.")

def master_yoda(text):
	reverse = []
	for let in text.split():
		reverse.insert(0, let)
	a = " ".join(reverse)
	return a

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print("\n")

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
print("5.")

def almost_there(n):
	bool = False
	if (90 <= n <= 110) or (190 <= n <= 210):
		bool = True
	else:
		bool = False
	return bool

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

print("\n")

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print("6.")

def has_33(nums):
	bool = False
	for i in range(len(nums) - 1):
		if nums[i] == 3 and nums[i+1] == 3:
			bool = True
	return bool

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

print("\n")

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
print("7.")

def paper_doll(text):
	triple = ""
	for i in text:
		triple += i + i + i
	return triple

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print("\n")

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
print("8.")

def blackjack(*args):
	ace = False
	total = sum(args)

	for i in args:
		if i == 11:
			ace = True

	if total <= 21:
		ret = total
	elif total > 21:
		if ace == True:
			ret = total - 10
		else:
			ret = "BUST"

	return ret

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(2,2,3,11,10,3))
print(blackjack(10,11))

print("\n")

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
print("9.")

def summer_69(arr):
	add = True
	total = 0

	for i in arr:
		if i == 6:
			add = False
		if i == 9:
			add = True
			total = total - 9

		if add == True:
			total = total + i
		else:
			total = total

	return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print("\n")

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
print("10.")

def spy_game(nums):
	ck1 = False
	ck2 = False
	ck3 = False

	for i in nums:
		if i == 0:
			ck1 = True
		if ck1 == True and i == 0:
			ck2 = True
		if ck2 == True and i == 7:
			ck3 = True

	if ck1 == True and ck2 == True and ck3 == True:
		return True
	else:
		return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([1,7,2,0,0,0,7]))

print("\n")

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
print("11.")

def count_primes(num):
	numPrimes = 0
	isPrime = False

	for thisNum in range(num):
		isPrime = False
		if thisNum == 0 or thisNum == 1:
			isPrime = False
		if thisNum == 2 or thisNum == 3:
			isPrime = True

		for i in range(2, int((thisNum**0.5)+1)):
			if thisNum % i == 0:
				isPrime = False
				break
			else:
				isPrime = True

		if isPrime == True:
			numPrimes = numPrimes + 1

	return numPrimes

print(count_primes(100))