class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None  # (name, id)

    def __str__(self):
        status = f"Lent to {self.borrowed_by[0]} (ID: {self.borrowed_by[1]})" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name.strip()
        self.id = member_id

    def __str__(self):
        return f"{self.name} (ID: {self.id})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.next_member_id = 1

    def register_member(self, name):
        name = name.strip()
        for member in self.members:
            if member.name.lower() == name.lower():
                print("This person is already a member.")
                return
        member = Member(name, self.next_member_id)
        self.members.append(member)
        print(f"Member {member.name} registered with ID {member.id}")
        self.next_member_id += 1

    def get_member(self, name, member_id):
        name = name.strip()
        for member in self.members:
            if member.name.strip() == name and member.id == member_id:
                return member
        return None

    def add_book(self, title, author):
        self.books.append(Book(title.strip(), author.strip()))
        print(f"Book {title} by {author} is added...")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n Books in the library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")

    def lend_book(self, title, name, member_id):
        member = self.get_member(name, member_id)
        if not member:
            print("You are not a member of this library.")
            return

        for book in self.books:
            if book.title.lower() == title.strip().lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrowed_by = (member.name, member.id)
                    print(f"Book '{book.title}' lent to {member}.")
                else:
                    print(f"Book already lent to {book.borrowed_by[0]} (ID: {book.borrowed_by[1]}).")
                return
        print("Book not found...")

    def return_book(self, title, name, member_id):
        member = self.get_member(name, member_id)
        if not member:
            print("You are not a member of this library.")
            return

        for book in self.books:
            if book.title.lower() == title.strip().lower():
                if book.is_borrowed and book.borrowed_by == (member.name, member.id):
                    book.is_borrowed = False
                    book.borrowed_by = None
                    print(f"Book '{book.title}' returned by {member}.")
                elif book.is_borrowed:
                    print(f"This book was lent to someone else: {book.borrowed_by[0]} (ID: {book.borrowed_by[1]}).")
                else:
                    print("This book is not currently lent out.")
                return
        print("Book not found...")


def main():
    library = Library("Library")

    while True:
        print("\n--- Library Menu ---")
        print("1. Register Member")
        print("2. Add Book")
        print("3. Display Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Enter member name: ")
            library.register_member(name)

        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == '3':
            library.display_books()

        elif choice == '4':
            title = input("Enter book title to Borrow: ")
            name = input("Enter your name: ")
            member_id = int(input("Enter your member ID: "))
            library.lend_book(title, name, member_id)

        elif choice == '5':
            title = input("Enter book title to Return: ")
            name = input("Enter your name: ")
            member_id = int(input("Enter your member ID: "))
            library.return_book(title, name, member_id)

        elif choice == '6':
            print("Exiting... Thank you for using the library system.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
