class Email:
    def __init__(self, id, dom, tipoDom, contra=None):
        self.__id = id
        self.__dom = dom
        self.__tipoDom = tipoDom
        self.__contra = contra

    def retornaEmail(self):
        Correo = self.__id + self.__dom + self.__tipoDom
        return Correo

    def getContra(self):
        return self.__contra

    def cambiarContra(self,ingresa):
        self.__contra=ingresa
        print('Se modifico la contraseña\n\n')

    def getDominio(self):
        return self.__dom

    def mostrarDatos(self):
        print('Id: ',self.__id)
        print('Dominio: ',self.__dom)
        print('Tipo Dominio: ',self.__tipoDom)

