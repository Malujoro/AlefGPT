import socket
import threading

HOST = '127.0.0.1'
PORT = 7000
ADDR = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

def escutar_mensagens():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(f"\nMensagem recebida: {msg}\n")
        except:
            print("Erro ao receber mensagem.")
            break

thread_escuta = threading.Thread(target=escutar_mensagens, daemon=True)
thread_escuta.start()

def menu():
    while True:
        print("\nMenu")
        print("1 - Enviar mensagem")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            destino_ip = input("Digite o IP do destinatário: ")
            destino_port = input("Digite a porta do destinatário: ")
            destino = (destino_ip, int(destino_port))
            msg = input("Digite a mensagem: ")
            client_socket.send(f"{destino}:{msg}".encode())

        elif opcao == '2':
            print("Saindo...")
            client_socket.close()
            break

        else:
            print("Opção inválida")

menu()
