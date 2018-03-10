import zmq
import time
import sys
from threading  import Thread
# ZeroMQ Context

l1=[]
# Define the socket using the "Context"
# sock = context.socket(zmq.REP)
def inputmessage(l1):
    context_1 = zmq.Context()
    sock_1 = context_1.socket(zmq.REP)
    sock_1.bind("tcp://127.0.0.1:5678")
    while True:
        mess = str(sock_1.recv().decode())
        sock_1.send_string("Echo: " + mess)
        l1.append(mess)
        # print sock_1.recv()
        print(l1)
def publish(l1):
    context = zmq.Context()
    sock = context.socket(zmq.PUB)
    sock.bind("tcp://127.0.0.1:5680")
# Run a simple "Echo" server
    while True:
        while len(l1)!=0:
            message=l1.pop()
            sock.send_string(message)

output_ser = (Thread(target=inputmessage, args=(l1, )))
output_ser.start()

receive_ser = (Thread(target=publish, args=(l1, )))
receive_ser.start()        