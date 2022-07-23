import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def cnnct():
  try:
    s.connect(("127.0.0.1", 9999))
    print("Connected to Server!")
  except socket.error as err:
    print("Conneceting error")

def rcv():
  print("SERVER: " + s.recv(1024).decode())


def snd():
  text = input("YOU: ")
  if text == "-quit" :
    s.close()
  else:
    s.send(text.encode())
 

def main():
  cnnct()

  while True:
    snd()
    rcv()
    print("\n\n")
    
main()

