class StudentNode:
    def __init__(self,student_id,marks,name):
        self.student_id = student_id
        self.marks = marks
        self.name = name
        self.link = None
class StudentQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def enqueue(self,student_id,marks,name):
        new_node = StudentNode(student_id,marks,name)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.link = new_node
            self.tail = new_node
            print(f"Enqueued: {student_id}, {name}, {marks}")
    def dequqe(self,student_id,marks,name):
         if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
         removed_node = self.head
         self.head = self.head.next
         if self.head is None:
            self.tail = None
         print(f"Dequeued: {removed_node.student_id}, {removed_node.name}, {removed_node.marks}")
         return removed_node
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.head
        print("Student Queue:")
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Marks: {current.marks}")
            current = current.next
def main():
    queue = StudentQueue()

    while True:
        print("\n--- Student Queue Menu ---")
        print("1. Enqueue Student")
        print("2. Dequeue Student")
        print("3. Display Queue")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ")
                marks = float(input("Enter Student Marks: "))
                queue.enqueue(student_id, name, marks)
            except ValueError:
                print(" Invalid input. Please enter numeric values for ID and Marks.")
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Exiting... ")
            break
        else:
            print(" Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

