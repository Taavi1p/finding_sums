#program written to find sums of powers where k = 11 and lef side of the equation has between 3 and 6 variables.
a = 1
b = 1
c = 1
for i in range(1000):
    a += 1
    b += 1
    c += 1
    number = a**11 + b**11 + c**11
    print(number)
    eleventhRoot = number**(1/11)
    print(eleventhRoot)
    if eleventhRoot.is_integer():
        print(str(a) +  " + " +  str(b) +  ' + ' +  str(c) + '==' ' is a solution!!!')
    else:
        print(str(a) + " + " + str(b) +  ' + ' + str(c) + '==' ' is not a solution :(')