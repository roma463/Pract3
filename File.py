
from watchdog.events import FileSystemEventHandler

numbers = ['0','1','2','3','4','5','6','7','8','9']
global xy
def on_create(path: str):
    global my_file
    my_file = open(path, "w+")

def main():
    i = input("Введите имя файла: ")
    if len(i) < 3:
        print('"Введите строку с кол-вом символов больше 3')
        main()
    for a in i:
        if a in numbers:
            print ("Введите строку без чисел")
            main()
        else: 
            path   =  "files/" + i + ".txt"
            on_create(path)
            return i , path
                  
xy = main()
