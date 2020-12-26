#for i in ["primavera","verano","otogno","invierno"]:
 #   print(i,end=" ")

#email=False
#miEmail=input("introduce tu correo electronico:  ")
#for i in miEmail:
 #   if (i=="@" ) :
  #     email=True
#if email==True :
 # print("el email es correcto")
#else :
 # print("el email es incorrecto")  
#print("el programa termino")  



#alido=False
email=input("introduce tu email :  ")
for i in range(len(email)):
    if email[i]=="@" :
        valido=True
if valido==True:
    print("email correcto")
else :
 print("email incorrecto")            

i=1
while i<=10:
    print("ejecucion"+str(i))
    i=i+1
print("termino la ejecucion")    
