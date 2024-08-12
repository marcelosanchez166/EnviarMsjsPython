# Contador de palabras:
# Escribir una función que cuente la frecuencia de palabras en un texto.
# Ignorar la capitalización y puntuación.

"""import re
def contar_palabras(texto):
    texto = re.sub(r'[^\w\s]', '', texto).lower()
    palabras = texto.split()
    listado_palabras={}
    for palabra in palabras:
        if palabra not in listado_palabras:
            listado_palabras[palabra]=1
        else :
            listado_palabras[palabra]+=1
    print(listado_palabras)

contar_palabras("hola como estas todo bien si todo Bien que bueno me alegro gracias igual, hola ya regrese. hola que bueno jajaja que bueno verte Hola")
"""
# Generador de contraseñas:
# Crear una función que genere contraseñas aleatorias.
# La contraseña debe incluir letras mayúsculas, minúsculas, números y caracteres especiales.

# sample () es una función incorporada del módulo random en Python que devuelve 
# una lista de longitud particular de elementos elegidos de una secuencia, es decir, una lista, tupla, cadena o conjunto.

# Importamos el método sample de random.
"""from random import sample"""

# Declaramos la función con un argumento (longitud de la contraseña)
"""def password_generator(longitud):
    # Definimos los caracteres y simbolos
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"
    # HACK: upper() transforma las letras de una cadena en mayusculas
    abc_mayusculas = abc_minusculas.upper()
    numeros = "0123456789"
    simbolos = "{}[]()*;/,_-"
    # Definimos la secuencia
    secuencia = abc_minusculas + abc_mayusculas + numeros + simbolos
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    password_union = sample(secuencia, longitud)
    # Con join insertamos los elementos de una lista en una cadena
    password_result = "".join(password_union)
    # Retornamos la variables "password_result"
    return password_result
# Llamos a la función "password_generatos" y le pasamos el valor "12"
password = password_generator(12)
# Imprimimos el resultado
print("Contraseña: ", password)"""



import pywhatkit

# Prompt user for group id and message
# group_id = input("Introduce el id del grupo de WhatsApp: ")
# message = input("Introduce el mensaje: ")# J3ry9K2c30pAiJg9M6Bk9H
numero=input("Introduce el telefono de WhatsApp: ")
mensaje = input("Introduce el mensaje: ")
# Send message to WhatsApp group
#pywhatkit.sendwhatmsg_to_group_instantly(group_id, message, tab_close=False, close_time=3)
pywhatkit.sendwhatmsg_instantly(numero,mensaje)



"""Este código permite descargar una lista de reproducción de YouTube utilizando la biblioteca pytube. 
Se solicita la URL de la lista de reproducción al usuario, se obtiene la lista de videos y se descarga cada video en su resolución más alta."""

# from pytube import Playlist

# playlist_url = input('Enter Playlist: ')
# playlist = Playlist(playlist_url)

# for video in playlist.videos:
#     video.streams.get_highest_resolution().download()




# from pytube import Playlist
# from pytube.exceptions import PytubeError

# playlist_url = input('Enter Playlist: ')
# try:
#     playlist = Playlist(playlist_url)
# except PytubeError as e:
#     print(f"Error al acceder a la lista de reproducción: {e}")
#     exit()

# for video in playlist.videos:
#     try:
#         print(f"Descargando {video.title}...")
#         video.streams.get_highest_resolution().download()
#         print(f"{video.title} descargado exitosamente.")
#     except PytubeError as e:
#         print(f"Error al descargar {video.title}: {e}")
#     except Exception as e:
#         print(f"Error inesperado al descargar {video.title}: {e}")



"""Este código realiza un escaneo de puertos en una dirección IP o nombre de dominio especificado. 
La función port_scanner toma un objetivo (target) y una lista de puertos, y luego verifica si cada puerto está abierto."""

# import socket

# def port_scanner(target, ports):
#     clcoding = socket.gethostbyname(target)
#     print(f"Scanning {target} ({clcoding})")

#     for port in ports:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         socket.setdefaulttimeout(1)
#         result = sock.connect_ex((clcoding, port))
#         if result == 0:
#             print(f"Port {port}: Open")
#         sock.close()

# # Example usage
# target = "clcoding.com"
# ports = [22, 80, 443, 8080]
# port_scanner(target, ports)


