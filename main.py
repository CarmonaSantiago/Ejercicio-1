import csv

from Email import Email
if __name__ == '__main__':

    #Apartado 1
    print('#Creación de Cuenta#')
    nom = input('Ingrese su Nombre:')
    print('Ingrese datos del correo')
    id= input('Ingrese identificador de su cuenta (Ej:usuario233) : ')
    dom = input('Ingrese dominio de su cuenta(Ej:@gmail, @hotmail, @outlook) : ')
    tipoDom = input('Ingrese tipo de dominio de su cuenta (Ej: .com, .net) :')
    contra= input('Ingrese contraseña: ')
    email1 =Email(id,dom,tipoDom,contra)
    correo=email1.retornaEmail()
    print(f'Estimado {nom} te enviaremos tus mensajes a la dirección {correo}.\n\n')

    # Apartado 2
    print('#Modificacion de Contraseña#')
    ingresa=input('Ingresar la contraseña actual: ')
    actual=email1.getContra()
    if ingresa==actual:
        ingresa=input('Ingrese contraseña nueva : ')
        email1.cambiarContra(ingresa)
    else:
        print('Contraseña Actual incorrecta \n\n')

    #Apartado 3
    print('#Crear una nueva clase Email#')
    correo=input('Ingrese nuevo correo electronico: ')
    a=correo.split('@')
    id=a[0]
    b=a[1].split('.')
    dom=b[0]
    tipoDom=b[1]
    contra=input('Ingrese nueva contraseña del correo: ')
    email2 =Email(id,dom,tipoDom,contra)
    print('Nueva Clase: ')
    email2.mostrarDatos()
    print('\n\n')

    #Apartado 4

   archivo=open('correos.csv')
    reader=csv.reader(archivo,delimiter=',')
    i=1
    listaEmails=[]  #Lista Vacía
    for fila in reader:
        correo= Email(fila[0],fila[1],fila[2])
        listaEmails.append(correo)

    for objeto in listaEmails:
        print(f'correo{i}:Email ')
        objeto.mostrarDatos()
        print('\n')
        i += 1


    ingresa=input('Ingrese identificador de cuenta: ')
    band = False
    long = len(listaEmails)

    for objeto in listaEmails:
        id=objeto.retornaId()
        if id == ingresa:
            band=True
    if band == True:
        print('Identificador esta repetido')
    else:
        print('Identificador disponible')
