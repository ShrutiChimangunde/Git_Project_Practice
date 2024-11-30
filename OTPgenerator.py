import random
#generate random otp of 4 digit.
otp = random.randrange(1000, 10000)
print(otp)

#Create user authentication

user = int(input('Enter the OTP: '))
if otp == user:
    print(' Welcome ! Access granted ')
else:
    print('Opps! access denied , please enter correct OTP. ')