number  = 29
flag = False

if number>1:
    for i in rage(2,29):

        if (number % i) == 0:
            flag = True
            break

        if flag:
            print(number," is not a prime number")

        else:
            print(number, "is a prime number")

