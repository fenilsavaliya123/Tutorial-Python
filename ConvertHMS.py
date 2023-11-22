#Convert HMS
a=int(input("Enter Sceound:"))

Hour=(a/60)/60
Hour=int(Hour)
Minute=(a/60)%60
Minute=int(Minute)
Secound=a%60
Secound=int(Secound)




print(Hour,":",Minute,":",Secound)

