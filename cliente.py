import socket
import threading
import Badwords
from colorama import Fore
#En terminal no es posible ver colores (Colorama), Correr en otro ladoo
class Cliente_chat:
    def __init__(self):
        self.crear_connexion()

    def crear_connexion(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:  # Valida hasta incresar correctamente al servidor
            try:
                host = input('Ingrese la dirección IP del Servidor Chat: ')
                port = int(input('Ingrese el número del puerto: '))
                self.s.connect((host, port))
                break
            except:
                print("El servidor no se puende enlazar, intente nuevamente!.")

        self.username = input('Ingrese su nombre o alias: ')
        self.s.send(self.username.encode())
        print('¡Bienvenido al Chat! Recuerda evitar vulgaridades... o seran censuradas de INMEDIATO!!!')

        gestor_entradas = threading.Thread(target=self.gestor_entradas, args=())
        gestor_entradas.start()

        gestor_salidas = threading.Thread(target=self.gestor_salidas, args=())
        gestor_salidas.start()




    def gestor_entradas(self):
        while 1:
            print(self.s.recv(1204).decode())

    def gestor_salidas(self):
        print('Ahora puedes enviar mensajes: ')
        while 1:
            texto = input()
            f = Badwords.BadwordsFilter(['aguacate', 'gono\w+', '\w+rr', '\w+norr\w+','pordio\w+','prost\w+',
                                         'pullon','puta\w+','rame\w+','\w+dicu\w+','sap\w+','\w+jue\w+','su madre',
                                         'tetas','teton','tirar','tont\w+','tripleh\w+','zorra','zunga',
                                         'mond\w+','\w+puta','puti\w+','lameculo','lampara','lampa\w+','lichigo','loba',
                                         'malpa\w+','mame\w+','maric\w+','mastur\w+','orto','ort0','0rto','pen\w+',
                                         'perro','pich\w+','pija','pinc\w+','pingo','piro\w+','poll\w+','chim\w+',
                                         'choch\w+','chuchesumadre','chunchurria','chup\w+','\w+erda','cuca','cul\w+',
                                         'delputas','dobleh\w+','estup\w+','fari\w+','follar','garbi\w+','gorrero',
                                         'grantriplehijueputa','guis\w+','gurru\w+','hipocrita','huev\w+','guev\w+',
                                         'imbe\w+','jartera','caco\w+','aguev\w+','agueb\w+','ahuev\w+','ahueb\w+',
                                         'ano','arrec\w+','babo\w+','b0b0','bobo','boba','bochinche','boletoso',
                                         'bombril','cach\w+','caco\w+','carechimba','caremonda','careverga','sarn\w+',
                                         'care\w+','hp\w+','\w+icada','mka','Pende\w+','anal','sexo','mk\w+','mari\w+',
                                         'monda','m0nda'], reemplazo="*")
            texto = f.cambiar(texto)
            print('Tu: '+texto)

            self.s.send((Fore.LIGHTBLUE_EX+self.username + ' > ' + texto).encode())


if __name__ == '__main__':
    cliente = Cliente_chat()
