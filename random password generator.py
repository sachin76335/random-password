import random
import string
pass_len=8
charValues = string.ascii_letters +string.digits+string.punctuation
#  second method

# list comprehension [function for i in range(n)] 
password ="".join([random.choice(charValues)for i in range(pass_len)])
#print(res)

#  First method
#password = ""
#for i in range(pass_len):
 #   password += random.choice(charValues)
    #print(random.choice(charValues))
print("your random password is :",password)