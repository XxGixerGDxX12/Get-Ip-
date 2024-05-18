import socket

def obtener_ip_de_url(url):
    try:
        # Extraer el nombre del host de la URL
        host = url.split('//')[-1].split('/')[0]
        # Obtener la dirección IP del host
        ip = socket.gethostbyname(host)
        return ip
    except Exception as e:
        return f"Error al obtener la IP: {e}"

if __name__ == "__main__":
    url = input("Ingrese una URL: ")
    ip = obtener_ip_de_url(url)
    print(f"La dirección IP de {url} es: {ip}")
