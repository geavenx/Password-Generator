import random
import string

print('Welcome to my first Python project, a simple password Generator')
input('Press ENTER to continue...')

alphaLowercase = list(string.ascii_lowercase)
alphaUppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
specialCharacters = list('!@#$%&*()`¨^')

lenghtUppercase = int(input('Enter uppercase count in password: '))
lenghtLowercase = int(input('Enter lowercase count in password: '))
lenghtNumbers = int(input('Enter digits count in password: '))
lenghtSpecialCharacters = int(
    input('Enter special character count in password: '))

password = []

for x in range(lenghtUppercase):
    password.append(random.choice(alphaUppercase))
for x in range(lenghtLowercase):
    password.append(random.choice(alphaLowercase))
for x in range(lenghtNumbers):
    password.append(random.choice(numbers))
for x in range(lenghtSpecialCharacters):
    password.append(random.choice(specialCharacters))

random.shuffle(password)

print("".join(password))
input('press ENTER to exit...')

