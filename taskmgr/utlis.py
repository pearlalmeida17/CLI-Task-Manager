#validation basics
def validate():
    while True : 
        title = input("Task:")

        if title.strip():
            break
        else:
            print("Enter the task to be completed!")