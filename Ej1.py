import os

descargas = os.scandir(r'C:\Users\Barbys\Downloads')
ficheros = []
size = []
for archivo in descargas:
    if os.path.isfile(archivo):
        ficheros.append(archivo)
print(ficheros) 

for file in ficheros:
    tamanio = os.path.getsize(file)
    size.append(f'{int(tamanio/1024)}Kb')
print(size)