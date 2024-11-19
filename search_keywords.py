import zmq
import os


def count_keyword_in_files(folder_path, keyword):
    """
    Counts the number of times a keyword shows up in each text file in a folder.

    Sorts the files in descending order by number of occurrences. File names
    containing the keyword will be first in the list. If there are multiple
    file names containing the keyword, they will also be sorted in descending
    order by number of occurrences.

    Returns a sorted list of dictionaries containing the file name and
    number of occurrences of the keyword in that file.
    """
    results = []

    # iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # only want to process .txt files
        if not file_name.endswith('.txt'):
            continue

        # count the number of times the keyword shows up in the text file, regardless of case
        with open(file_path, "r") as infile:
            content = infile.read()
            keyword_count = content.lower().count(keyword.lower())

        # store the file name (string), occurrences (int), and keyword_in_name (True/False)
        results.append({
            "file_name": file_name,
            "occurrences": keyword_count,
            "keyword_in_name": keyword.lower() in file_name.lower()
        })

    # sort the results list
    search_results = sorted(results, key=lambda x: (-x["keyword_in_name"], -x["occurrences"]))

    # delete keyword_in_name from each dictionary, since it just to help sort the list
    for result in search_results:
        del result["keyword_in_name"]

    return search_results


# set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Ready to receive requests...\n")

while True:
    # receive a message from the client
    message = socket.recv_json()
    folder_path = message["folder_path"]
    keyword = message["keyword"]

    print(f"Received request for keyword '{keyword}' in folder '{folder_path}'")
    search_results = count_keyword_in_files(folder_path, keyword)
    print(f"Returned search results for keyword '{keyword}' in folder '{folder_path}'")
    for result in search_results:
        print(result)
    print()

    socket.send_json(search_results)

