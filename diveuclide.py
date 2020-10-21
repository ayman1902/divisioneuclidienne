#progrmmable by belhaj ayman MPSI2
def div_euclide(a,b):
    if a < 0 or b < 0:
        print("error")
    else:
        if a < b:
            a,b=b,a
        i = 0
        while a -b*i>b-1:
            i +=1
        #return a,b,(a-b*i)
        print(str(a)+"="+str(b)+"x"+str(i)+"+"+str(a-b*i)) 
div_euclide(461,4681)