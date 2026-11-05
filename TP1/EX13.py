q=int(input("donner la quantite achetee : "))
priX_unitaire=float(input("Donner le prix unitaire: "))
PT=q*priX_unitaire
reduction=PT*15/100
PF=PT-reduction
print(PT)
print(reduction)
print(PF)