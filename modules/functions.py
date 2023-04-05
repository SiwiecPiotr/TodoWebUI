import os, re, pathlib

current_directory = os.getcwd()
FILEPATH = pathlib.Path(current_directory, 'todos.txt')
regex = re.compile(r'(\d+.)(.*)')

def change_order(index1, index2, container):
    if index1 < 1 or index1 > len(container) or index2 < 1 or index2 > len(container):
        pass
    else:
        temp = container[index1-1]
        del container[index1-1]
        container.insert(index2-1, temp)

def get_todos(directory=FILEPATH, FORMAT=0):
    """ Opens the file mentioned by 'directory' argument
    and returns a list of lines from that file.
    """
    with open(directory, 'r') as file:
        list = file.readlines()
    if FORMAT == 1:
        list = [str(list.index(i)+1) + ". "+i for i in list]
    return list

def save_todos(data, directory=FILEPATH):
    """ Saves the list passed in 'data' argument
    to the file refered by 'directory' argument.
    """
    with open(directory, 'w') as file:
        file.writelines(data)

def strip_string(text, FORMAT = 0):
    match = regex.findall(text)
    if FORMAT == 1:
        match = [match[0][0].strip("."), match[0][1].strip()]
    else:
        match = match[0][1]
        match = match.strip()
    return match
# print(__name__)                                       Sprawdz co sie dzieje jak odpalasz skrypt bezposrednio i co sie dzieje jak odpalasz przez main
if __name__ == "__main__":
    print("Hello from the functions.")
    temp = strip_string("2231. Blaldala")
    temp2 = strip_string('7. :/\n', FORMAT=1)
    print(temp)
    print(temp2)