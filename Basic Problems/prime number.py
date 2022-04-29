num = int(input("Enter to check if number is prime or not:" ))
if num > 1:
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            print(num,"is not the prime number")
            break
    else:
         print(num,"is Prime Number")