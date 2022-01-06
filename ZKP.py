import random


def compute(h, g,x,p):
    product = 1
    for i in range(0,x):
        product = product*g
        if product > p:
            product = product%p

    product = ((h%p)*product)%p
    return product%p

def authenticate_user(y):
    #rand = random.randint(0,p-1)
    #s = int(input("Enter s: "))
    flag = 1
    g = 2
    p = 11
    t = 2
    hs = []
    print("Remember g = " + str(g)+ " and "  + "p = "+ str(p))
    i =0
    while (i < t):
        print("Round (" + str(i+1) + "/" + str(t)  +" )")
        h = int(input("Enter h = g^r mod p : "))
        if h in hs:
            print("You already used this h-value!!! Pls try using another h-value")
            #i = i-1
            continue
        else:
            hs.append(h)
            b = random.randint(0,1)
            print("B value : "+str(b))
            
            s = int(input("Enter the value r+bx mod (p-1) : "))
           # print(compute(1,g,s,p))
            #print(compute(h,y,b,p))

            if(compute(1,g,s,p)!= compute(h,y,b,p)):
                flag =0
                #print("Authentication failed!!!")
                return False
        i = i+1

    if(flag == 1):
        #print("Authentication successful")
        return True

    return flag

#verify_ID(10)


