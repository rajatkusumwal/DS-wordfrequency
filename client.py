import socket              
import time

s = socket.socket()         
port = 12345    
file_name=raw_input("Enter the file name you want to send.\n")
host=raw_input("Enter the mapreduce host address(IPv4).\n")            
s.setblocking(1)
time1=time.time()
s.connect((host, port))
f = open(file_name,'rb')
print 'Sending...'
l ="1"
while (l):
    print 'Sending...'
    l = f.read(1024)
    s.send(l)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR) #closes the write end of the connection only rec is allowed now.
f=open('ans.txt','wb')
f.write("Frequency of words.\r\n")
print "Receiving..."
l = "1"
while (l):
    print "Receiving..."
    l = s.recv(1024)
    f.write(l)
f.close()
time2=time.time()
print "Done Receiving"
print "TIme taken by the server %0.5fsec" % (time2-time1)
print("Succesfull Termination of connection.")
s.close()              
