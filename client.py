import socket

def start_client():
    host = '127.0.0.1'  # Server's IP
    port = 12345        # Server's port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server. Type 'exit' to end the chat.")

    try:
        while True:
            message = input("You: ")
            client_socket.send(message.encode())
            if message.lower() == "exit":
                break

            response = client_socket.recv(1024).decode()
            if not response:
                break
            print(f"Server: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
