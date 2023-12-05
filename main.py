

from paquete1.modulo1 import Cliente, Socio
from paquete1.modulo2 import cargar_archivo, agregar, menu, mostrar, guardar, comprobar

cliente1 = Cliente ("Juan", "juan@mail.com", 30, "tarjeta de credito" )

cliente1.comprar("laptop", "walmart")

cliente1s = Socio ("Roberto", "roberto@mail.com", 47, "tarjeta de credito", 5678)

cliente1.factura(cliente1.mail)

print(cliente1)

cliente1s.numero(cliente1s.n_socio)

print(cliente1s)