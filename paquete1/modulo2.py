
import json

usuario_contraseña = {}

def cargar_archivo():
    ruta = '/Users/Usuario/OneDrive/Escritorio/python/ejerciciopython/2dapreentrega'
    try:
        with open(ruta + "/usu_cont.txt", "r") as login:
            for line in login:
                data = json.loads(line.strip())
                usuario_contraseña.update(data)
    except FileNotFoundError:
        pass

cargar_archivo()

def agregar(users):
  while True:
    usuario =input('ingrese nuevo usuario: ')
    if usuario == '' or usuario in usuario_contraseña:
      print ("usuario invalido")
    elif usuario != '':
      print ('usuario aceptado')
      #break
      check = False
      while check == False:
        contraseña = input('ingrese contraseña para registrar (4 digitos): ')
        contra_long = len(contraseña)
        if contraseña.isdigit() == False:
          check = False
          print (f'la contraseña debe ser solo numeros')
        elif contra_long < 4 or contra_long > 4:
          print (f"la contraseña debe contenter 4 digitos")
        else:
          print ('registro exitoso')
          users[usuario] = contraseña
          guardar(users)
          comprobar(usuario_contraseña)
          return
          break

      key, value = usuario, contraseña
      users[key] = value
      return

def mostrar (users):
  #return(f'los usuarios y contraseñas almacenados son: {users}')
  print(f'los usuarios y contraseñas almacenados son: {users}')

def guardar (users):
  ruta = '/Users/Usuario/OneDrive/Escritorio/python/ejerciciopython/2dapreentrega'
  #login = open(ruta + "/usu_cont.txt","wt")
  login = open(ruta + "/usu_cont.txt","w")
  login2 = json.dumps(users)
  login.write(login2)
  login = json.loads(login2)
  #return

def comprobar (users):
  comprueba_usuario = input("ingrese su usuario: ")
  if comprueba_usuario in usuario_contraseña:
    print (f"usuario registrado")
    intentos = 0
    while intentos != 3:
      posib_int = 3
      for i in range(posib_int):
        comp_contraseña = input("ingrese su contraseña: ")
        if comp_contraseña == usuario_contraseña[comprueba_usuario]:
          print ("la contraseña es correcta")
          return ("la contraseña es correcta")
          #break
        else:
          print('la contraseña es incorrecta.  %d intentos restantes' % (posib_int-i-1))
          intentos += 1
        if intentos == 3:
          print ('numero maximos de intentos')
          #return ('numero maximos de intentos')

  elif comprueba_usuario not in usuario_contraseña:
    print ("el usuario no existe")
    opcion = None
    print(f"1. Para registrarse. \n2. Para usuario registrado. \nCualquier tecla para salir.")
    opcion = input()
    #opcion = input("1. Para registrarse. \n2. Para usuario registrado. \nCualquier otra tecla para salir.")
    if opcion == '1':
      agregar(usuario_contraseña)
    elif opcion == '2':
      comprobar(usuario_contraseña)
    else:
      print('Has salido')

def menu (users):
    print (f"1. Para registrarse. \n2. Para usuario registrado. \nCualquier otra tecla para salir.")
    opcion = input ()
    if opcion == '1':
      agregar(usuario_contraseña)
    elif opcion == '2':
      comprobar(usuario_contraseña)
    else:
      print ("has salido")
      #exit()



menu (usuario_contraseña)  
mostrar(usuario_contraseña)
guardar(usuario_contraseña)