#Implement Stack using list, insert and delete from front of the list

stack = []

def push(item):
    stack.insert(0,item)
    print(f"Pushed {item}")

def pop():
    if is_empty():
        print("Stack is empty. Cannot pop.")
        return None
    popped = stack.pop(0)
    print(f"Popped {popped}")
    return popped


def is_empty():
    return len(stack) == 0

def display():
    print("Current Stack:", stack)

while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        val = input("Enter value to push: ")
        push(val)
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!")

