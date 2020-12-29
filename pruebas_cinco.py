def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento
ciudades_devuelta=devuelve_ciudades("Lima","Huaraz")
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))
print(next(ciudades_devuelta))

