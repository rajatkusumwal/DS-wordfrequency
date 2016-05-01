from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

server= SimpleXMLRPCServer(("192.168.43.3",9000))

def node_mapper(arg):
    with open("rec_data.txt","wb") as handle:
        handle.write(arg.data)
    handle.close()
    dic={}
    c=0
    f=open('rec_data.txt','rb')
    for line in f:
        temp=""
        for letter in str(line):
            if((ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122)):
                temp=temp+letter
            elif(temp!=""):
                if(dic.has_key(temp)==True):
                    dic[temp]=dic[temp]+1
                else:
                    dic[temp]=1
		temp=""
		print "Mapping...."
    f.close()
    #print dic
    return dic

server.register_function(node_mapper, 'node_mapper')
server.serve_forever() 
