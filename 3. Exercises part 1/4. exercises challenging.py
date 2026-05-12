# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(in_list):
    expected = [0,0,7]
    for n in in_list:
        if len(expected) >= 1 and expected[0] == n:
            expected.pop(0)
    return len(expected)==0

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

def count_primes(n):
    count = 0
    for i in range(2,n+1):
        count_prime = 0
        for j in range(1,i+1):
            if i%j==0:
                count_prime = count_prime + 1
        if count_prime==2:
            count = count + 1
    return count

print(count_primes(100))
