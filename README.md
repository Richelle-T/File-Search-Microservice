# Communication Contract 

## A. REQUEST Data from search_keywords.py
### Step 1: Install the Python package for ZeroMQ 
`pip install pyzmq`

### Step 2: Set up context and socket in your main program
`import zmq`  
`context = zmq.Context()`  
`socket = context.socket(zmq.REQ)`  
`socket.connect("tcp://localhost:5555")`

If you need to change the port number `5555`, make sure you also change the port number in search_keywords.py on line 52 to match the number used in your main program.  
Line 52: `socket.bind("tcp://*:5555")`

### Step 3: Initialize folder_path and keyword variables
Set `folder_path` to the path of the folder containing text files you wish to search through.  
Set `keyword` to the word you're searching for.

`folder_path = r"YOUR FOLDER PATH"`  
`keyword = "YOUR WORD"`

Please make sure to include the r (for "raw string") in front of the folder path's string. Otherwise, Python might interpret any backslashes \ as escape sequences. 

### Step 4: Send the request using socket.send_json(message)
Create the message dictionary containing `folder_path` and `keyword`  
`message = {`  
`  "folder_path": folder_path,`  
`   "keyword": keyword`  
`}`  

Send the message  
`socket.send_json(message)`

## B. RECEIVE Data from search_keywords.py
 Assign `socket.recv_json()` to a variable  
`result = socket.recv_json()`

The result is a list of dictionaries. Each dictionary has a key-value pair for file_name and occurrences.  
`file_name` is a string for the text file's name.  
`occurrences` is an int representing the number of times the keyword appeared in the file.

An example of how you could display the results:  
`print(f"Search results for '{keyword}'")`  
`for result in search_results:`  
`   print(f"{result['file_name']}: {result['occurrences']}")`


## C. UML Sequence Diagram
