import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))

s.listen(1)
conn, addr = s.accept()
print("Connected to " + str(addr))
print("\nLet\'s talk")

def snd():
	text = input("YOU: ")
	if text =="-quit":
		conn.close()
	else:
		conn.send(text.encode())
		
def rcv():
	receive = conn.recv(1024).decode("utf-8")
	print("CLIENT: " + receive) 
	
		

		
def main():
	while True:
		rcv()
		print("\n\n")
		snd()
main()


