#  Copyright (c) 2019
#  Author : Samsul Ma'arif <samsulma828@gmail.com>

import wordProtector as wp
print("=" * 50)
print("Created by: Samsul Ma'arif")
print("=" * 50)
while True:
    print("")
    print("=" * 25 + " Protect Your Information " + "=" * 25)
    print("=" * 25 + " Menu " + "=" * 25)
    print("1. Encrypt your information")
    print("2. Decrypt your information")
    print("3. Exit")

    choice = input("Please type menu number u want ? ")
    if choice == "3":
        print("Thank u for coming")
        break
    elif choice == "1":
        x = input('Please input your information for encrypt : ')
        secret = input("please enter your secret key, that just u and your friend know, to read this message : ")
        result = wp.enc(x, secret)
        print("now u can share your information to your friend with safe : "+result)
    elif choice == "2":
        x = input('Please input your encrypted word : ')
        secret = input("please enter your secret key, that just u and your friend know, to read this message : ")
        result = wp.decr(x, secret)
        print("now u can read your information with safe : " + result)
    else:
        print("Please type correct number u want to do in this system")
    print