class Saludo():
  def __init__(self,precio,nombre):
      self.precio  = precio
      self.nombre = nombre
  def saludar(self):
      print(f'Bienvenida {self.nombre}')
s = Saludo('250','Imelda')
s.saludar()

class pasteles:
    def __init__(self,precio):
        self.precio  = precio
    def tamaño (self, mensaje):
            print(mensaje)

vainilla = pasteles (250)
chocolate = pasteles (250)

print ('El pastel de vainilla tiene un costo de: ', vainilla.precio)
print ('El pastel de chocolate tiene un costo de: ', chocolate.precio)

vainilla.tamaño  ('El costo del pastel de vainilla  es de tamaño grande')
chocolate.tamaño  ('El costo del pastel de chocolate es de tamaño grande')

class pasteles:
    def __init__(self,sabor,precio,tamaño):
        self.sabor= sabor
        self.precio= precio
        self.tamaño= tamaño

        print(f"El pastel de {self.sabor} tiene un costo de ${self.precio} el de tamaño {self.tamaño}")

print("----------PASTELERIA EL MENCHO----------")
print("------------------MENU------------------")
vainilla = pasteles("vainilla","350", "grande")

vainilla2= pasteles("vainilla","250", "mediano")

chocolate = pasteles("chocolate","350","grande")

chocolate2= pasteles("chocolate","250", "mediano")

fresa = pasteles("fresa","350", "grande")

fresa2= pasteles("fresa","250", "mediano")

cake=input("escriba el sabor de pastel de tu preferencia ")

size=input("escriba el tamaño del pastel ")
if cake== "vainilla":
    print("pastel de vainilla de tamaño ",size)
    if size==("grande"):
        print("costo de $350")
    if size==("mediano"):
        print("costo de $250")
if cake== "chocolate":
    print("pastel de chocolate de tamaño ",size)
    if size==("grande"):
        print("costo de $350")
    if size==("mediano"):
        print("costo de $250")
if cake== "fresa":
    print("pastel de fresa de tamaño ",size, )
    if size==("grande"):
        print("costo de $350")
    if size==("mediano"):
        print("costo de $250")

opcion=input("desea imprimir su ticket?")
if opcion== "si":
    print("----------PASTELERIA EL MENCHO----------")
    print("PASTEL SABOR", cake,"DE TAMAÑO",size)
    if size=="grande":
        print("TOTAL: $350")
    if size=="mediano":
        print("TOTAL: $250")
    print("----MUCHAS GRACIAS POR SU PREFERENCIA---")
if opcion=="no":
    print("muchas gracias, vuelva pronto!")






class saludo:
    def __init__(self,mensaje,nombre):
        self.mensaje=mensaje
        self.nombre=nombre
        print(f"{self.mensaje} {self.nombre}")

usuario = saludo("Tenga un buen dia","Imelda")
