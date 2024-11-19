## Communication Contract 

# A. REQUEST Data
## Step 1: Set up ZeroMQ

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")




# B. RECEIVE Data

# C. UML Sequence Diagram
