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



valido=False
email=input("introduce tu email :  ")
for i in range(len(email)):
   if email[i]=="@" :
        valido=True
if valido==True:
    print("email correcto")
else :
 print("email incorrecto")            

 def generapares(limite):
    numero=1
    lista=[]
    while numero<limite:
        lista.append(numero*2)
        numero=numero+1
    return lista
print(generapares(20))         


def genera_pares(limit):
     num=1
     while num<limit:
         yield num*2
         num=num+1
devuelvepares=genera_pares(20) 
for i in devuelvepares:
    print(i)        





