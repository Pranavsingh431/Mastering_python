# CONTROL FLOW STATEMENTS: if, else, elif.
# colons and indentation(whitespaces) play a very important role in these statements.

a = int(input("enter a number: "))
b = int(input("enter another number: "))

if a == 0 and b == 1:
    print("Error because the numbers are zero.")
elif a > b:
    print(f'The number {a} is greater than {b}.')
elif a < b:
    print(f'The number {a} is less than {b}.') 
else:
    print('Both the numbers are equal.')   
