"""Password Generator Project"""

import string
import random

password = ""
temp = []

lc = list(string.ascii_lowercase)
uc = list(string.ascii_uppercase)
d = list(string.digits)
p = list(string.punctuation)

n = int(input("Enter length of password: \n"))
if n <= 4:
    n = int(input("Password length should be greater than 4: \n"))

lst = [lc, uc, d, p]
password = random.choice(lc) + random.choice(uc) + random.choice(d) + random.choice(p)

for i in range(n - 4):
    char = random.choice(lst)
    temp.append(random.choice(char))

for i in temp:
    password += i

print(password)