import zmq

# set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# data to be passed to the microservice
# IMPORTANT NOTE: need to have an r (for "raw string") in front of the folder path
# to prevent Python from interpreting \ as escape sequences
folder_path = r"C:\Users\Richelle\OSU\Microservice Test\CS 361 Notes\Example Folder"
keyword = "HELLO"

# send the request to the microservice
message = {
    "folder_path": folder_path,
    "keyword": keyword
}
socket.send_json(message)

# receive the search results from the microservice
# this is a list containing dictionaries with the keys 'file_name' and 'occurrences'
search_results = socket.recv_json()

# show the structure of search_results
for result in search_results:
    print(result)
print()

# display the results nicely
print(f"Search results for '{keyword}'")
for result in search_results:
    print(f"{result['file_name']}: {result['occurrences']}")

