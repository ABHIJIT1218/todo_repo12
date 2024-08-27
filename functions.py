def get_todos(filepath="todos.txt"):   #default parameter
    """ Read a text file and return the list of to-do items"""   #doc strings
    with open(filepath, 'r') as file:  # it makes the code shorter
        todos = file.readlines()
        return todos

def write_todos(todos_arg,filepath="todos.txt"): #default parameter
    """write the to-do items list in the text file"""
    with open(filepath, 'w') as file1:  # it makes the code shorter
        file1.writelines(todos_arg)

# print(__name__)
if __name__ == "__main__":
    print("hello11")
    print(get_todos())
