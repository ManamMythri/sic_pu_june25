#stack using single linked list insertion and deletion at begining 

class StudentNode:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.link = None

class StudentStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, student_id, name, marks):
        new_node = StudentNode(student_id, name, marks)
        new_node.link = self.head
        self.head = new_node
        print(f" Pushed: ID={student_id}, Name={name}, Marks={marks}")

    def pop(self):
        if self.is_empty():
            print(" Stack Underflow: No student to remove.")
            return
        removed = self.head
        self.head = self.head.link
        print(f" Popped: ID={removed.student_id}, Name={removed.name}, Marks={removed.marks}")

   
    def display(self):
        if self.is_empty():
            print(" Stack is empty.")
            return
        current = self.head
        print(" Student Stack :")
        while current:
            print(f"ID={current.student_id}, Name={current.name}, Marks={current.marks}")
            current = current.link


def menu():
    stack = StudentStack()
    while True:
        print("\n====== Student Stack Menu ======")
        print("1. Push (Insert Student)")
        print("2. Pop (Remove Student)")
        print("3. Display Stack")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                marks = float(input("Enter Marks: "))
                stack.push(student_id, name, marks)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print(" Exiting program.")
            break
        else:
            print("Invalid choice. Try 1-4.") 


menu()
