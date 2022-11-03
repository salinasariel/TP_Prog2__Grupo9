from datetime import date
import sqlite3

class Programa:
    
    def menu(self):
        
        print("¿Quiere crear una tabla?")
        print("Atencion, si crea una nueva tabla sobreescribira los datos anteriormente ingresados")
        opciontabla = int(input("1-SI 0-NO "))
        if opciontabla == 1:
            borrarSql = "DROP TABLE IF EXISTS Monopatin"
            sql = "CREATE TABLE Monopatin (_id INTEGER PRIMARY KEY , modelo VARCHAR(30), marca  VARCHAR(30), potencia VARCHAR(30), color VARCHAR(30), cantidadDisponible INTEGER, precio REAL, fechaUltimoPrecio DATETIME)"
            borrarsql2 = "DROP TABLE IF EXISTS HistoricoMono"
            sql2 = "CREATE TABLE HistoricoMono (_id INTEGER PRIMARY KEY , modelo VARCHAR(30), marca  VARCHAR(30), potencia VARCHAR(30), color VARCHAR(30), cantidadDisponible INTEGER, precio REAL, fechaUltimoPrecio DATETIME)"
            self.nuevaTabla(borrarSql, sql)
            self.nuevaTabla2(borrarsql2, sql2)
        
        while True:
            print("------------------------------")
            print("MENU DE MONOPATINES ELECTRICOS")
            print("1- Cargar monopatin: ")
            print("2- Modificar precio de un monopatin: ")
            print("3- Borrar monopatin: ")
            print("4- Cargar disponibilidad: ")
            print("5- Listado de productos: ")
            print("6- Modificar al dolar actual: ")
            print("7- Mostrar registros anteriores: ")
            print("0- Salir del menu: ")
            nro = int(input("Por favor ingrese un numero: "))
            if nro == 1:
                elegir : int = 1
                print("\n\tCARGA DE DATOS")
                while elegir == 1:
                    marca = str(input("Ingrese el marca del monopatin: "))
                    modelo = str(input("Ingrese el modelo del monopatin: "))
                    potencia = str(input("Ingrese la potencia del monopatin: "))
                    color = str(input("Ingrese el color del monopatin: "))
                    cantidadDisponible = int(input("Ingrese la cantidad disponible: "))
                    precio = float(input("Ingrese el precio del monopatin: "))
                    fechaUltimoPrecio = date.today()
                    nuevo_monopatin = Monopatin(marca, modelo, potencia, color, cantidadDisponible, precio, fechaUltimoPrecio)
                    nuevo_monopatin.cargarMonopatin()
                    #nuevo_monopatinhistorico = Monopatin(marca, modelo, potencia, color, cantidadDisponible, precio, fechaUltimoPrecio)
                    #nuevo_monopatinhistorico.cargarMonopatinHistorico()
                    elegir = int(input("Desea ingresa otro monopatin? 1-SI 0-NO "))

            elif nro == 2:
                print("\n\tMODIFICAR PRECIO DE UN MONOPATIN")
                nuevoId = int(input("Ingrese el ID del monopatin: "))
                nuevoPrecio = float(input("Ingrese el nuevo precio del monopatin: "))
                Monopatin.modificarPrecio(self, nuevoId, nuevoPrecio)

            elif nro == 3: 
                print("\n\tELIMINAR MONOPATIN")
                borrarId = int(input("Ingrese ID del monopatin que desea eliminar: "))
                Monopatin.borrarMonopatin(self, borrarId) 
            
            elif nro == 4:
                print("\n\tMODIFICAR DISPONIBILIDAD DE UN MONOPATIN")
                nuevaMarca = str(input("Ingrese el ID del monopatin que desea modificar la disponibilidad: "))
                Monopatin.cargaDisponibilidad(self, nuevaMarca)    
                
            
            elif nro == 5:
                print("\nLISTADO DE MONOPATINES")
                sql = "SELECT * FROM Monopatin"
                Monopatin.mostrarDatos(self, sql)

            elif nro == 6:
                aumentoDolar: float = 0.23
                sql = "UPDATE Monopatin SET precio=precio+(precio*'{}') ".format(aumentoDolar)
                sql3 = "UPDATE Monopatin SET fechaUltimoPrecio='{}' ".format(date.today())
                Monopatin.precioDolar(self, sql, sql3)

                print("\nLISTADO DE MONOPATINES HISTORICO")
                sql2 = "SELECT * FROM HistoricoMono"
                Monopatin.mostrarDatos(self, sql2)
                

            elif nro == 7:
                print("\n\tTABLA DE REGISTROS ANTERIORES")
                anio = str(input("Ingrese el año: "))
                mes = str(input("Ingrese el mes: "))
                dia = str(input("Ingrese el dia: "))
                fechaIngresada = date(int(anio), int(mes), int(dia))
                fechaInicio = date(1000,1,1)
                Monopatin.mostrarDatos(self, "SELECT * FROM HistoricoMono where fechaUltimoPrecio BETWEEN '{}' AND '{}' ".format(fechaInicio, fechaIngresada))
            
            elif nro == 0:
                print("\n\t*RECUERDE QUE LOS DATOS CONTINUAN GUARDADOS PARA UN PROXIMO USO*")
                break
                    

    def nuevaTabla(self, borrarSql, sql) -> None:
        conexion = Conexiones() 
        conexion.abrirConexion() 
        try:
            conexion.miCursor.execute(borrarSql)
            conexion.miCursor.execute(sql)
            conexion.miConexion.commit()
            print("\tTABLA CREADA EXITOSAMENTE")
        except:
            print("\tERROR AL CREAR LA TABLA")
        finally:
            conexion.cerrarConec()

    def nuevaTabla2(self, borrarSql, sql) -> None:
        conexion = Conexiones() 
        conexion.abrirConexion() 
        try:
            conexion.miCursor.execute(borrarSql)
            conexion.miCursor.execute(sql)
            conexion.miConexion.commit()
            print("\tTABLA HISTORICA CREADA EXITOSAMENTE")

        except:
            print("\tERROR AL CREAR LA TABLA")
        finally:
            conexion.cerrarConec()

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("EmpresaDeMonopatines")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConec(self):
        self.miConexion.close()    

class Monopatin:
    _id: int = 0
    def __init__(self, marca: str, modelo: str, potencia: str, precio: float, color: str, cantidadDisponible: int, fechaUltimoPrecio: date):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.precio = precio
        self.color = color
        self.cantidadDisponible = cantidadDisponible
        self.fechaUltimoPrecio = fechaUltimoPrecio
        self._id = self._get_next_id()

    @classmethod
    def _get_next_id(cls) -> int:
        cls._id += 1
        return cls._id
    
    # Numero 1
    def cargarMonopatin(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO Monopatin(marca,modelo,potencia,color,cantidadDisponible,precio,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(self.marca, self.modelo, self.potencia, self.precio, self.color, self.cantidadDisponible, self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("\tMONOPATIN CARGADO EXITOSAMENTE")
        except:
            print("\tERROR AL CARGAR UN MONOPATIN")
        finally:
            conexion.cerrarConec()
    
    # Numero 2
    def modificarPrecio(self, nuevoId: int, nuevoPrecio: float) -> None:
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Monopatin SET precio='{}' where _id='{}' ".format(nuevoPrecio, nuevoId))
            conexion.miConexion.commit()
            print("\tPRECIO ACTUALIZADO EXITOSAMENTE")
        except:
            print("\tERROR AL ACTUALIZAR EL PRECIO")
            print("\tTenga en cuenta que el ID haya sido ingresado correctamente")
        finally:
            conexion.cerrarConec()
    
    # Numero 3
    def borrarMonopatin(self, borrarId) -> None:
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM Monopatin where _id='{}' ".format(borrarId))
            conexion.miConexion.commit()
            print("\tMONOPATIN BORRADO EXITOSAMENTE")
        except:
            print("\tERROR AL BORRAR EL MONOPATIN")
            print("\tTenga en cuenta que el ID haya sido ingresado correctamente")
        finally:
            conexion.cerrarConec()

    # Numero 4
    def cargaDisponibilidad(self, nuevaMarca) -> None:
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Monopatin SET cantidadDisponible=cantidadDisponible+1 where _id='{}'".format(nuevaMarca))
            conexion.miConexion.commit()
            print("\tSTOCK ACTUALIZADO EXITOSAMENTE")
        except:
            print("\tERROR AL ACTUALIZAR EL STOCK")
        finally:
            conexion.cerrarConec()
            
    # Numero 5
    def mostrarDatos(self, sql) -> None:
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(sql)
            monopatines = conexion.miCursor.fetchall()
            for mono in monopatines:
                print(mono)
        except:
            print("\tERROR AL MOSTRAR LA LISTA")
            print("\n\tTenga en cuenta haber creado la tabla previamente")
        finally:
            conexion.cerrarConec()

    # Numero 6        
    def precioDolar(self, sql, sql3) -> None:
        Monopatin.cargarMonopatinHistorico(self)
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(sql)
            conexion.miCursor.execute(sql3)
            conexion.miConexion.commit()
        except:
            print("\tERROR AL ACTUALIZAR EL PRECIO")
        finally:
            print("\tPRECIO ACTUALIZADO EXITOSAMENTE")
            conexion.cerrarConec()
            

    # Numero 7
    def cargarMonopatinHistorico(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM Monopatin")
        monopatines = conexion.miCursor.fetchall()
        for mono in monopatines:
            conexion.miCursor.execute("INSERT INTO HistoricoMono(marca,modelo,potencia,color,cantidadDisponible,precio,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(mono[1],mono[2],mono[3],mono[4],mono[5], mono[6], mono[7]))
        conexion.miConexion.commit()
        conexion.cerrarConec()

programa = Programa()
programa.menu()

try:
    programa = Programa()
    programa.menu()
except:
    print("\n\tERROR DEL PROGRAMA")
finally:
    print("\n\tFin del programa")