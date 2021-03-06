import sys
import sqlite3
conn = sqlite3.connect('C:\Users\user\Documents\SW-Taller2\BD')

class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def

#Patrón singleton
class Cine:
    instancia = None
    @classmethod
    def get_instance(cls, cine):
        if cls.instancia == None:
            if cine == 'CineStark':
                cls.instancia = CineStark()
            elif cine == 'CinePlaneta':
                cls.instancia = CinePlaneta()
            else:
                return Cine()
        return cls.instancia

    def ingresar_cine(self):
        c = conn.cursor()
        c.execute('''INSERT INTO CINES (1,'CinePlaneta')''')
        c.execute('''INSERT INTO CINES (2,'CineStark')''')
        c.commit()

    def ingresar_peliculas(self):
        c = conn.connect()
        c.execute('''INSERT INTO PELICULA (1, 'IT')''')
        c.execute('''INSERT INTO PELICULA (2, 'La Hora Final')''')
        c.execute('''INSERT INTO PELICULA (3, 'Desaparecido')''')
        c.execute('''INSERT INTO PELICULA (4, 'Deep El Pulpo')''')
        c.commit()

    def ingresar_funciones(self):
        c = conn.conect()
        #CP-IT
        c.execute('''INSERT INTO FUNCIONES (1,1, '19:30')''')
        c.execute('''INSERT INTO FUNCIONES (1,1, '20:30')''')
        c.execute('''INSERT INTO FUNCIONES (1,1, '22:00')''')
        #CP-HF
        c.execute('''INSERT INTO FUNCIONES (1,2, '21:00')''')
        #CP-D
        c.execute('''INSERT INTO FUNCIONES (1,3, '20:00')''')
        c.execute('''INSERT INTO FUNCIONES (1,3, '23:00')''')
        #CP-DP
        c.execute('''INSERT INTO FUNCIONES (1,4, '16:00')''')

        #CS-D
        c.execute('''INSERT INTO FUNCIONES (2,3, '21:00')''')
        c.execute('''INSERT INTO FUNCIONES (2,3, '23:00')''')
        #CS-DP
        c.execute('''INSERT INTO FUNCIONES (2,4, '16:00')''')
        c.execute('''INSERT INTO FUNCIONES (2,4, '20:00')''')

class CinePlaneta:
    def __init__(self):
        peliculaIT = Pelicula(1, 'IT')
        peliculaHF = Pelicula(2, 'La Hora Final')
        peliculaD = Pelicula(3, 'Desaparecido')
        peliculaDeep = Pelicula(4, 'Deep El Pulpo')

        peliculaIT.funciones = ['19:00', '20.30', '22:00']
        peliculaHF.funciones = ['21:00']
        peliculaD.funciones = ['20:00', '23:00']
        peliculaDeep.funciones = ['16:00']

        self.lista_peliculas = [peliculaIT, peliculaHF, peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


#Patrón factory
class CineStark:
    def __init__(self):
        peliculaD = Pelicula(1,  'Desaparecido')
        peliculaDeep = Pelicula(2, 'Deep El Pulpo')

        peliculaD.funciones = ['21:00', '23:00']
        peliculaDeep.funciones = ['16:00', '20:00']

        self.lista_peliculas = [peliculaD, peliculaDeep]
        self.entradas = []


    def listar_peliculas(self):
        return self.lista_peliculas

    def listar_funciones(self, pelicula_id):
        return self.lista_peliculas[int(pelicula_id) - 1].funciones

    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)

class CineFactory:
    def obtener_cine(self, cine):
        if cine == '1':
            return CinePlaneta()
        elif cine == '2':
            return CineStark()

#Patrón Fachada
class GestorEntrada:
    def comprar_entrada(seflf, cine):
        peliculas = cine.listar_peliculas()
        for pelicula in peliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        pelicula_elegida = input('Elija pelicula:')
        #pelicula = obtener_pelicula(id_pelicula)
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')

        for funcion in cine.listar_funciones(pelicula_elegida):
            print('Función: {}'.format(funcion))
        funcion_elegida = input('Funcion:')
        cantidad_entradas = input('Ingrese cantidad de entradas: ')
        codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
        print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))

#Patrón fachada
class Plataforma:
    def mostrar_menu2(self):
        print('********************')
        print('Lista de cines')
        print('1: CinePlaneta')
        print('2: CineStark')
        print('********************')

    def mostrar_plataforma(self):
        terminado = False;
        while not terminado:
            print('Ingrese la opción que desea realizar')
            print('(1) Listar cines')
            print('(2) Listar cartelera')
            print('(3) Comprar entrada')
            print('(0) Salir')
            opcion = input('Opción: ')

            if opcion == '1':
                self.mostrar_menu2()

            elif opcion == '2':
                self.mostrar_menu2()

                cine = input('Primero elija un cine:')
                factory = CineFactory()
                cine = factory.obtener_cine(cine)

                peliculas = cine.listar_peliculas()
                print('********************')
                for pelicula in peliculas:
                    print("{}. {}".format(pelicula.id, pelicula.nombre))
                print('********************')

            elif opcion == '3':
                self.mostrar_menu2()
                cine = input('Primero elija un cine:')
                factory = CineFactory()
                cine = factory.obtener_cine(cine)

                gestorEntrada = GestorEntrada()
                gestorEntrada.comprar_entrada(cine)

            elif opcion == '0':
                terminado = True
            else:
                print(opcion)

class SQL:
    def crear_tablas(self):

        c = conn.cursor()

        c.execute('''CREATE TABLE CINES (cine_id int, nombre text)''')
        c.execute('''CREATE TABLE PELICULA (pelicula_id int, nombre text)'''))
        c.execute('''CREATE TABLE FUNCIONES (cine_id int, pelicula_id int,
            funcion text)'''))

def main():
    bd = SQL()




    plataforma = Plataforma()
    plataforma.mostrar_plataforma()

    #Crea la base de datos

    c = conn.cursor()
    #c.execute("CREATE TABLE Entradas (id, cine text, pelicula text, cantidad_entradas real)")



if __name__ == '__main__':
    main()
