import socket 

# open port, connect to port, check open port, check route

# making a http request with TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("starwit.de", 80))
s.sendall(b'GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n')
data = s.recv(4096)
print(data)
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1099))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True:
    try:
        data = conn.recv(1024)
        if not data: 
            break
        
        try:
            data = str(data, "utf-8")
        except UnicodeDecodeError:
            print("Can' parse utf8.")
            break            

        print("Client Says: " + data)
        conn.sendall(bytes("RE: " + data + "\n", "utf-8"))
        if data == "q":
            conn.close()
            break

    except socket.error:
        print("Error Occured.")
        break

conn.close()
s.close()