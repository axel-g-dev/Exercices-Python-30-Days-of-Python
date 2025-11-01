# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of'
word_4 = 'Python'

print(word_1 + ' ' + word_2 + ' ' + word_3 + ' ' + word_4)
print("-------------------")
# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"
print(company)

print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize(), " ensuite ", company.title(), " puis ", company.swapcase())

company_word_1 = print(company[0:6])
company_word_2 = print(company[7:10])
company_word_3 = print(company[11:14])

print(company.replace('Coding', 'Python'))

print(company.strip('Coding For '))

print(company.split())
print("-------------------")
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

gafam = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(gafam.split(', '))
print("-------------------")
# What is the character at index 0 in the string Coding For All.
quote = 'Coding For All'
first_letter = quote[0]
print(first_letter) 
print("-------------------")
# What is the last index of the string Coding For All.
last_letter = quote[-1]
print(last_letter) 
print("-------------------")
# What character is at index 10 in "Coding For All" string.
tenth_letter = quote[9]
print(tenth_letter) 
print("-------------------")

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
print(phrase[0], phrase[7], phrase[11])
print("-------------------")

# Use index to determine the position of the first occurrence of C in Coding For All.
coding_for_all = 'Coding For All'
substring_1 = 'C'
substring_2 = 'F'
print(coding_for_all.rindex(substring_1), coding_for_all.rindex(substring_2))
print("-------------------")

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
cdfap = 'Coding For All People.'
last_l = 'l'
print(len(cdfap))
print(cdfap.rfind('l'))
print("-------------------")

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
last_because = sentence.rindex('because')
print(last_because)
print(len(sentence))
print("-------------------")


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_sentence_1 = sentence[0:30]
sliced_sentence_2 = sentence[54:71]
print (sliced_sentence_1 + sliced_sentence_2)
print("-------------------")

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_of_because = print(sentence.find('because'))
print("-------------------")
# Does ''Coding For All' start with a substring Coding?

test = 'Coding For All'
print(test.startswith('Coding'))
print("-------------------")

# Does 'Coding For All' end with a substring coding?
test_endwith = print(test.endswith('coding'))
print("-------------------")

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

cda = '   Coding For All      '
sli_1 = cda[3:17]
print(sli_1)
print("-------------------")

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python --> celui-ci :)

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
librairie = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultat = ' '.join(librairie) 
print(resultat)
print("-------------------")

# Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. I just wonder what is next.

line_escape_sentence = print("I am enjoying this challenge.\nI just wonder what is next.")

# Use the string formatting method to display the following:
'''
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''

radius = 10 
area = 3.14 * radius ** 2
print("The area of a circle with radius", str(radius), "is", str(area), "meters square.")

print("-------------------")