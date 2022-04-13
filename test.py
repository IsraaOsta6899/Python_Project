def Tribonacci(number):
    if number == 0:
        return 0 
    elif number==1 or number==2:
        return 1

    else :
        return Tribonacci(number-1)+Tribonacci(number-2)+Tribonacci(number-3)
print(Tribonacci(3))
# 0 1 1 2 4
