'''
#Swapping
a= 5
b= 6
a, b = b, a         #to swap to values
print('a= ', a)
print('b= ', b)


#Palindrom Check

string = input('Enter an english word: ')           #like: 'racecar'
check = bool(string.find(string[::-1])+1)
print(check)
'''

#Sum of Two integers
print((lambda a,b: a+b)(10,20))