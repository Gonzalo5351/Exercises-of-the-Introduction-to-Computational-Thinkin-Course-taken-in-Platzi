# Que reciba el nombre del usuario.
# Que le del un saludo.
# Que le diga cuál es la longitud de la cadena.

def run():
  usr_name = input ("Hello, wath's your name?: ")
  print(f'The length of your name is {str(len(usr_name))} letters.')
if __name__ == '__main__':
    run()