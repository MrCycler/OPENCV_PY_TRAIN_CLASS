import os

def create_pos_n_neg():

    print("\n")
    print("Creando archivo bg.txt")
    print("\n")
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

    print("Creando carpeta info")
    print("\n")
    if not os.path.exists('info'):
        os.makedirs('info')

    print("Creando carpeta pos")
    print("\n")
    if not os.path.exists('pos'):
            os.makedirs('pos')

    print("Programa finalizado")
    print("\n")
create_pos_n_neg()