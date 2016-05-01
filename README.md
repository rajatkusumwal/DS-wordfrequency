# DS-wordfrequency
This is a word frequency counter python script on distributed systems for low power devices with less memory eg. raspberry pi.

##How to set up.
1. Run server5.py on the main server . It is the master node script which handles managment of data , splitting of data and fault handling[Not yet included].<br>
2. Run node_server.py on slave nodes which are on the same network as the master server and they comunicate using RPC protocols with main server.<br>
3. Run client.py script on the client device which gives client an interface to send a file to the master server for frequency counting.

##Future Works:
1. Fault handling of the slave nodes.<br>
2. Performance enhancement by caching word count dictionary on slave nodes of each client seperatly.<br>
3. Encrypting the data for securing clients privacy.<br>
4. Memory managment on low memory and low power devices like raspberry pi.
5. Socket timeout handling by acknowledging client on regular intervals.

##Sample data:
These mb sample files are tested on raspberry pi with a difference of 20 sec for computation for single node to multiple node server inclusive of network overhead.
