N=int(input("Ecrire la valeur de N: "))
S=0
while N<=0 :
   N=int(input("taper N:"))
for  i in range (1,N+1) :
    S=S+(1/i)
    print ("la somme est: ",S)

