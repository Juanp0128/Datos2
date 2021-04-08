import socket
import threading


class ServidorChat:
    def __init__(self):
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = socket.gethostbyname(socket.gethostname())
        port = int(input('Ingrese el número del puerto del servicio: '))
        self.s.bind((host, port))
        self.s.listen(100)

        print(f'Servidor Chat en la dirección IP (host): {host}')
        print(f'Servidor Chat en el puerto (port): {port}')

        self.clientes = []
        self.nombre_clientes = {}

        # ciclo infinito
        while True:
            conexion, addr = self.s.accept()
            username = conexion.recv(1024).decode()

            print(f'Nueva conexión. Username: {username}')
            self.transmitir(f'Una nueva persona se ha unido al salón. Username: {username}')

            self.nombre_clientes[conexion] = username

            self.clientes.append(conexion)

            threading.Thread(target=self.enlazar_cliente, args=(conexion, addr,)).start()

    def transmitir(self, msg):
        for connection in self.clientes:
            connection.send(msg.encode())

    def enlazar_cliente(self,conexion,addr):
        while True:
            try:
                msg = conexion.recv(1024)
            except:
                conexion.shutdown(socket.SHUT_RDWR)
                self.clientes.remove(conexion)

                print(str(self.nombre_clientes[conexion])+' abandono el salón.')
                self.transmitir(str(self.nombre_clientes[conexion])+' se salio del salón.')

                break

            if msg.decode() != '':
                print('Nuevo mensaje: '+str(msg.decode()))
                for connection in self.clientes:
                    if connection != conexion:
                        connection.send(msg)

if __name__ == '__main__':
    servicio = ServidorChat()
