import os

try:
    archivo = "miArchivo8.txt"
    modFile = "r+" if os.path.exists(archivo) else "w"
    miArchivo = open(archivo,modFile)
    try:
        if modFile =="w":
            i= 1
            while i <= 15:
                miArchivo.write("Lorem ipsom ... " + str(i) + "\n")
                i +=1
        else:
            # print(miArchivo.read())
            print(miArchivo.readline(),end="")
            print(miArchivo.readline(),end="")
            miArchivo.seek(0,0)
            ultVal =0
            for linea in miArchivo.readlines():
                print("Linea leida: " + linea, end="")
                ultLin = linea[15:18]
                
                if ultLin.strip().isdigit():
                    ultVal = int(ultLin.strip()) 

            # ultLin = miArchivo.readlines()
            print()
            ultVal +=1
            ultVal = str(ultVal)
            miArchivo.write("Lorem ipsom ... " + ultVal + "\n")

            # miArchivo.write("Última linea %i \n" %ultVal)
            # miArchivo.write("Última linea %i \n" %ultVal)

    except:
        print("Something went wrong when writing to the file.")
    finally:
        miArchivo.close()
        print("Process finally!.")

except:
    print("Error al crear archivo") 