#25:SMTP:EMAIL
#23:TELNET Login
#22:SSH
#80:http
#443:https:
#109/110 POP Mail Retrival
#143/220/993 IMAP Mail Retrival
#53-DNS
#21-FTP


import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
#mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
#mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode())


while True:
    data=mysock.recv(512)
    if len(data) < 1:
        break
    print(data)
mysock.close()


#req res cycle
#Browser makes network connection
#href hot links or hyper links
#www.dr-chuck.com
#http://www.dr-chuck.com/page1.htm HTTP/1.0
#GET http://www.dr-chuck.com/page1.htm HTTP/1.0
#www.mlive.com/ann-arbor
#telnet is unencrypted not to use login



