
class Cliente:
  
  def __init__(self, nombre, mail, edad, medio_pago):
    self.nombre = nombre
    self.mail = mail
    self.edad = edad
    self.medio_pago = medio_pago

  def factura(self, mail):
    print (f'la factura fue enviada a {mail}')

  def __str__(self):
    cadena= (f'se ha creado el cliente {self.nombre}')
    return cadena

  def comprar(self, que, donde):
    print (f'el cliente {self.nombre} compro un {que} en {donde}')
  
class Socio (Cliente):
    
    def __init__(self, nombre, mail, edad, medio_pago, n_socio):
        self.n_socio  = n_socio
        super().__init__(nombre, mail, edad, medio_pago)

    def numero(self, n_socio):
      print (f"el numero de socio de {self.nombre} es {n_socio}")


    
    