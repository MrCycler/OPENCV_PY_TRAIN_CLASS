import os
import sys

def change_info_files(offside):
    print('Numero de inicio',offside)

    for file_type in ['info']:
        
        for file in os.listdir(file_type):
            if file !="info.lst":
                print('Procesando:',file)
                file_split = file.split('_',1)
                numero_inicial = int(file_split[0],10)
                numero_final =""
                numero_final = "%04d" % (numero_inicial+offside)
                file_out = numero_final +'_'+ file_split[1]
                print('Cambiado a:',file_out)
                file = "info/"+file
                file_out = "info/"+file_out
                os.rename(file,file_out)
                print("\n")

    f = open('info/info.lst', 'r')
    oif = open('info.lst', 'r')
    oiflineas = oif.read()
    oif.close()
    of = open('info.lst', 'w')
    lineas  = f.read()
    of.write(oiflineas)
    for linea in lineas.split('\n'):
        if linea !='':
            print('Procesando en archivo:',linea)
            linea_split = linea.split(' ',1)
            name_file_split = linea_split[0].split('_',1)
            numero_inicial = int(name_file_split[0],10)
            numero_final =""
            numero_final = "%04d" % (numero_inicial+offside)
            name_file_out = numero_final +'_'+ name_file_split[1]
            linea_out = name_file_out+' '+linea_split[1]
            print('Cambiado en archivo a:',linea_out)
            print("\n")
            of.write(linea_out)
            of.write("\n")
    f.close()
    of.close()
    print('Procesamiento finalizado')

n_offside = int(sys.argv[1])
change_info_files(n_offside)