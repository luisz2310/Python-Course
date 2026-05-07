# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False
def has_33(list_nums):
    for i, num in enumerate(list_nums[:-1]):
        if num == 3 and list_nums[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3, 1, 3, 1, 3, 3, 1]))
print("-------------------")

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(word):
    return "".join( n*3 for n in word)
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print("-------------------")

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(*arg):
    d=sum(arg)
    if d <= 21:
        return d
    elif 11 in arg and d <= 31:
       return d-10
    else:
        return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print("-------------------")

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#     summer_69([1, 3, 5]) --> 9
#     summer_69([4, 5, 6, 7, 8, 9]) --> 9
#     summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(args):
    a = 0
    flag = False
    for arg in args:
        if arg == 6:
            flag = True
        if not flag:
            a += arg
        if arg == 9:
            flag = False
    return a
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))