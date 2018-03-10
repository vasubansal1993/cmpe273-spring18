import zmq
import sys
from threading import Thread

host = sys.argv[1]

# ZeroMQ Context
def output():
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:5678")
    while True:
        sock.send_string("["+host+"]: "+ input("["+host+"]>"))
        mess= (sock.recv().decode())


# TODO: change this to PUB pattern.
# Define the socket using the "Context"
def subscribe():
    context1 = zmq.Context()
    sock1 = context1.socket(zmq.SUB)
    sock1.setsockopt_string(zmq.SUBSCRIBE, "")
    sock1.connect("tcp://127.0.0.1:5680")
    while True:
        message= sock1.recv().decode()
        if message.find("["+host+"]: "):
                print("\n"+message+"\n["+host+"] ") 

# Send a "message" using the socket

print("User["+sys.argv[1]+"] Connected to the chat server.")


output_sent = (Thread(target=output, args=( )))
output_sent.start()

receive_sent = (Thread(target=subscribe, args=( )))
receive_sent.start()