
queue = [] 

def enqueue():
    item = input("Enter value to enqueue: ")
    queue.insert(0,item)
    print(f"Enqueued: {item}")

def dequeue():
    if is_empty():
        print("Queue is empty. Cannot dequeue.")
    else:
        removed = queue.pop()
        print(f"Dequeued: {removed}")

def is_empty():
    return len(queue) == 0

def display():
    print("Current Queue :", queue)
while True:
    print("\n--- Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1 to 4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting")
        break
    else:
        print("Invalid choice. Try again.")
