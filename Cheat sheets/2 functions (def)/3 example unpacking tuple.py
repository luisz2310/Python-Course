tuples = [("Sam",1000),("Luis",800),("Jose",2000)]

def get_max_income(tuples):
    max_income = 0
    max_name = ''
    for name,income in tuples:
        if income > max_income:
            max_income = income
            max_name = name
        else:
            pass
    return max_name, max_income

print(get_max_income(tuples))
max_name, max_income = get_max_income(tuples)
print("Max income:", max_income)
print("Max name:", max_name)
