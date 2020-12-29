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
