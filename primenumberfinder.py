# opens a text file 
prime_nums = open('list of numbers.txt', 'w')

# function for determining if a number is prime or not. 1, 2 3 = prime. if not divisible by 2 or 3, prime
def prime_checker(number):
    if number == 1 or number == 2 or number == 3:
        print(f'{number} is prime')
        prime_nums.write(f'{number}: PRIME\n')
    elif number % 2 == 0 or number % 3 == 0:
        print(f'{number} is not prime.')
        prime_nums.write(f'{number}: not prime and divisible by 2 or 3.\n')
    else:
        print('{number} is prime')
        prime_nums.write(f'{number}: PRIME\n')

# allows user to input a range of numbers to find all primes within that range
lower_range = int(input('enter lower range: '))
upper_range = int(input('enter upper range: '))

# loop that goes through the range
for i in range(lower_range, upper_range + 1):
    prime_checker(number=i)
prime_nums.close()
