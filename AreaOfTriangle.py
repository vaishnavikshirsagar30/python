a = float(input('Enter 1st side: '))  
b = float(input('Enter 2nd side: '))  
c = float(input('Enter 3rd side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   
