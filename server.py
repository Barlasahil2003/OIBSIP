import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    try:
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")

            response = input("You: ")
            conn.send(response.encode())
            if response.lower() == "exit":
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()
