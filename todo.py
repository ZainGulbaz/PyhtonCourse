# Adding some thing
#print the list

todoList=[];


def addTodoToList(text):
    todoList.append(text);

def printTodoList():
    print(" ");
    for element in todoList:
        print(element);


print("Our todo app has been started");
print("Just Use Ctrl+C to quit the app");

def func():
    command=input("IF you want to add text press = 1, IF you want to print the list press=2");
    if(command=="1"):
        text= input("Enter the text: ");
        addTodoToList(text);
    if(command=="2"):
        printTodoList();
    func();

# When we call a function inside a function, this technique is called "Recursion"

func();









