#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#lesser_of_two_evens(2,4) --> 2
#lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a, b):
    return  (a if a<b else b) if a%2==0 and b%2==0 else (b if a<b else a)

def lesser_of_two_evens2(a, b):
    return  (min(a,b)) if a%2==0 and b%2==0 else (max(a,b))

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens2(2,4))
print(lesser_of_two_evens2(2,5))
print("----------------------")
#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(a):
    return a.split()[0][0] == a.split()[1][0]
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print("----------------------")
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def makes_twenty(a,b):
    return a==20 or b==20 or a+b==20
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))