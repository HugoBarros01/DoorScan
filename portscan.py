import socket

ports = [21, 22, 80, 443, 445, 3306, 25]

print("Qual é o endereço IP?")
host = input()

try:
    ip = socket.gethostbyname(host)  # Resolve o host para um endereço IP

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, port))
        if code == 0:
            print(f"A porta {port} está ABERTA")
        else:
            print(f"A porta {port} está FECHADA")

except socket.gaierror:
    print("Não foi possível resolver o host. Verifique o endereço IP ou nome de host fornecido.")
except KeyboardInterrupt:
    print("Varredura interrompida pelo usuário.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

