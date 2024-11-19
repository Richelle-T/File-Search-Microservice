## Communication Contract 

# A. REQUEST Data
## Step 1
Install the Python package for ZeroMQ: pip install pyzmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")




# B. RECEIVE Data

# C. UML Sequence Diagram
