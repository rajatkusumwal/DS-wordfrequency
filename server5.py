import socket
import os
import threading
from SocketServer import ThreadingMixIn
import xmlrpclib

dic={}
node_list=[]
#threadLock = threading.Lock()
threads = []

class ClientThread(threading.Thread):
    def __init__(self,address,file_name):
        threading.Thread.__init__(self)
        self.address = address
        self.file_name = file_name
        print " New thread started for "+address+"and file "+file_name

    def run(self):
        #threadLock.acquire()
        global dic
        global node_list
        client=xmlrpclib.Server('http://'+self.address+':9000')
        with open(self.file_name,"rb") as handle:
            binary_data=xmlrpclib.Binary(handle.read())
        handle.close()
        val=client.node_mapper(binary_data)
        for temp in val.keys():
            if(dic.has_key(temp)==True):
                dic[temp]=dic[temp]+val[temp]
            else:
                    dic[temp]=val[temp]
        node_list.append(str(self.address))
        #threadLock.release()


def mapper(i):
    f=open('map'+str(i)+'.txt','wb')
    for val in dic:
        f.write(val+":"+str(dic[val])+"\r\n")
    f.close


node=int(raw_input("Enter number of nodes."))
for x in range(0,node):
    adr=raw_input("Enter node address.")
    node_list.append(adr)
page_size=raw_input("Enter memory block size in kb.")
print("Server is running. :)")
i=0
s=socket.socket()
host="192.168.43.6"
port=12345
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    i=i+1
    f=open('rec'+str(i)+'.txt','wb')
    print 'Got connection from', addr
    print "Receiving..."
    l = "1"
    while (l):
        print "Receiving..."
        l = c.recv(1024)
	f.write(l)
    f.close()
    print "Done Receiving"
    c.shutdown(socket.SHUT_RD)
    print("Splitting files.")
    spl=str("split -b "+page_size+"k rec"+str(i)+".txt rec"+str(i))
    os.system(spl)
    fv=ord('a')
    file_name="rec"+str(i)+"a"+str(chr(fv))
    while (os.path.isfile(file_name)):
            if (node_list):
                newthread=ClientThread(node_list.pop(),file_name)
                newthread.start()
                threads.append(newthread)
                fv+=1
                file_name="rec"+str(i)+"a"+str(chr(fv))
    for t in threads:
        t.join()
    #print dic
    mapper(i)   
    f=open('map'+str(i)+'.txt','rb')
    print 'Sending the mapped file to client.'
    l ="1"
    while (l):
        print 'Sending...'
        l = f.read(1024)
        c.send(l)
    f.close()
    print "Done Sending"
    c.shutdown(socket.SHUT_WR)
    print "Connection Completed Succesfully!"
    c.close()            
    dic.clear()
