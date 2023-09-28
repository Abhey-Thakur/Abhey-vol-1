a = int(input("Which number table : "))
b = 1
while b<=10:
    c = int(input(str(a)+" times "+str(b)+" = "))
    while c != a*b:
        print("wrong!, try again")
        c = int(input(str(a)+" times "+str(b)+" = "))     
    print("Correct")
    b += 1

