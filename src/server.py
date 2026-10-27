import socket  
from views import render_template  
  
def run_server(host: str = "127.0.0.1", port: int = 8080):  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    server_socket.bind((host, port))  
    server_socket.listen(1)  
    print(f"Сервер запущен на http://{host}:{port}")  
    while True:  
        client_socket, addr = server_socket.accept()  
        request = client_socket.recv(1024).decode("utf-8")  
        if not request:  
            client_socket.close()  
            continue  
        first_line = request.split("\n")[0]  
        method = first_line.split(" ")[0]  
        if method == "POST":  
            print("\n=== Получен POST-запрос ===")  
            body = request.split("\r\n\r\n", 1)[1] if "\r\n\r\n" in request else ""  
            print(f"Данные от пользователя:\n{body}\n")  
            response_body = "<h1>Данные получены!</h1>"  
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {len(response_body.encode('utf-8'))}\r\n\r\n{response_body}"  
        else:  
            try:  
                response_body = render_template("contacts.html")  
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {len(response_body.encode('utf-8'))}\r\n\r\n{response_body}"  
            except FileNotFoundError:  
                response_body = "<h1>404 Not Found</h1>"  
                response = f"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: {len(response_body.encode('utf-8'))}\r\n\r\n{response_body}"  
        client_socket.send(response.encode("utf-8"))  
        client_socket.close()  
  
if __name__ == "__main__":  
    run_server() 
