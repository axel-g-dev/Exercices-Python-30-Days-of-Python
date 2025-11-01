# Exercice-Day3

#Declare your age as integer variable
age = 19
print("Hello, i'm", age, "years old"), 


#Declare your height as a float variable
size = 1.85
print("I am currently", size, "cm")

#Declare a variable that store a complex number

nombre_complexe = 1+1j
print(nombre_complexe)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = 20
h = 10

aire = 0.5*b*h

print("L'aire de ce triangle est :", aire)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

#print("Entrez la taille du côté a : ")
#a = float(input("..."))

#print("Entrez la taille du côté b : ")
#b = float(input("..."))

#print("Entrez la taille du côté c : ")
#c = float(input("..."))

#perimetre = a + b + c
#print("Le périmètre de ce triangle est :", perimetre) 

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
'''
length = float(input("Enter the lenght of the rectangle"))
width = float(input("Enter the width of the rectangle"))

area = length*width
perimeter = 2*(length + width)

print("L'aire de ce rectangle est : ", area)
print("Le périmètre de ce rectangle est : ", perimeter)
''' 

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
pi = 3.14 
r = float(input("Donnez le rayon du cercle : "))

area  = pi*r**2
c = 2*pi*r
print("area", area, "&", "c", c)
'''

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''
m = 2
x = 0
y_intercept = 2 * x - 2

x_intercept = 2 / 2  

print("Pente (slope) :", m)
print("Y-intercept (quand x = 0) :", y_intercept)
print("X-intercept (quand y = 0) :", x_intercept)
'''

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
'''
x_1 = 2
y_1 = 2

x_2 = 6
y_2 = 10

m = (y_2-y_1)/(x_2-x_1)

print("Le coef directeur est : ", m)
'''

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''
x = float(input("donnez un nombre"))

y = x**2 + 6*x + 9 

print(y)

'''

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') == len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print(not ('on' in 'python' and 'on' in 'dragon'))

# Find the length of the text python and convert the value to float and convert it to string
x = len('python')

print(float(x), str(x))

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_div = 7 // 3
print(float(floor_div) == int(2.7))

# Check if type of '10' is equal to type of 10

print(type('10') == type(10))

# Check if int('9.8') is equal to 10
'''
print(int(9.8) == 10)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Nombre d'heures de la semaine : "))
rate = float(input("Salaire horaire : "))
weekly_earnings = hours*rate

print('Your weekly earnings are : ', weekly_earnings)
'''

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
'''
years = float(input("Enter number of years you have lived: "))
years_that_can_be_lived = 100*365*24*3600

life = years*365*24*3600 

print('You have lived ', life, 'seconds')
print('The seconds that are remaining in your life ', years_that_can_be_lived - life, 'seconds')
'''

# Write a Python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

i = 0
for i in range (0,5) : 
    i = 1 + i
    print(i, '1', i, i**2, i**3)
   




