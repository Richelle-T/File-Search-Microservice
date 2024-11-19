# Communication Contract 

## A. REQUEST Data
### Step 1
Install the Python package for ZeroMQ: `pip install pyzmq`

### Step 2
Set up the context and socket in your main program \n
`context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")`

### Step 3
Change the `folder_path` to the path of the folder which you're searching through.
Change `keyword` to the word you're searching for. 


## B. RECEIVE Data

## C. UML Sequence Diagram
