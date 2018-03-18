from socket import *
import sys


class portScan:
    def __init__(self):
        sockObj = socket(AF_INET, SOCK_STREAM)
        self.ip = input("Ip: ")
        self.port = input("Até qual porta você deseja testar? ")

        if len(self.port.split(" ")) > 1:
            portas = self.port.split(" ")
            for port in portas:
                print("\nTestando a porta {}   ".format(port))
                resposta = sockObj.connect_ex((self.ip, int(port)))
                if resposta == 0:
                    print("\n\n\nA porta {} está aberta".format(port))
                    break
                else:
                    print("Fechada")
        elif(self.port.split(" ")) == 1:
            a = 1
            while int(self.port) >= a:
                print("\nTestando a porta {}   ".format(a))
                resposta = sockObj.connect_ex((self.ip, a))
                if resposta == 0:
                    print("\n\n\nA porta {} está aberta".format(a))
                    break
                else:
                    print("Fechada")
                    a += 1
        input("\npessione <Enter> para sair")
        sys.exit()
        
if __name__ == "__main__":
    rodando = portScan()
