
# LIBRARY MANAGEMENT SYSTEM
# Using Functions and File Handling

books = []
issued_books = []


# FUNCTION 1: SAVE DATA INTO FILE

def save_data():

    file = open("library.txt", "w")

    for book in books:
        file.write("B|" + book["id"] + "|" +
                   book["name"] + "|" + book["author"] + "|" +
                   str(book["total"]) + "|" +
                   str(book["available"]) + "\n")

    for issued in issued_books:
        file.write("I|" + issued["book_id"] + "|" +
                   issued["student"] + "\n")

    file.close()


# FUNCTION 2: LOAD DATA FROM FILE

def load_data():

    try:
        file = open("library.txt", "r")

        for line in file:

            data = line.strip().split("|")

            if data[0] == "B":

                book = {
                    "id": data[1],
                    "name": data[2],
                    "author": data[3],
                    "total": int(data[4]),
                    "available": int(data[5])
                }

                books.append(book)

            elif data[0] == "I":

                issued = {
                    "book_id": data[1],
                    "student": data[2]
                }

                issued_books.append(issued)

        file.close()

    except FileNotFoundError:
        file = open("library.txt", "w")
        file.close()


# FUNCTION 3: ADD BOOK

def add_book():

    book_id = input("Enter Book ID: ")

    if book_id == "":
        print("Book ID cannot be empty!")
        return

    for book in books:

        if book["id"] == book_id:

            book_name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")

            if (book_name.lower() != book["name"].lower()
                    or author.lower() != book["author"].lower()):
                print("Book ID belongs to another book!")
                return

            quantity = input("Enter Additional Quantity: ")

            if not quantity.isdigit() or int(quantity) <= 0:
                print("Enter a valid positive quantity!")
                return

            book["total"] += int(quantity)
            book["available"] += int(quantity)

            save_data()

            print("Book Quantity Updated Successfully!")
            return

    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = input("Enter Quantity: ")

    if book_name == "" or author == "":
        print("Book Name and Author cannot be empty!")
        return

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Enter a valid positive quantity!")
        return

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "total": int(quantity),
        "available": int(quantity)
    }

    books.append(book)

    save_data()

    print("Book Added Successfully!")


# FUNCTION 4: DISPLAY BOOKS

def display_books():

    if len(books) == 0:
        print("No Books Available!")
        return

    print("\n------ BOOK DETAILS ------")

    for book in books:

        print("Book ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        print("Total Quantity:", book["total"])
        print("Available Quantity:", book["available"])
        print("Issued Quantity:",
              book["total"] - book["available"])

        print("--------------------------")


# FUNCTION 5: SEARCH BOOK

def search_book():

    search = input("Enter Book Name: ")
    found = False

    for book in books:

        if book["name"].lower() == search.lower():

            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Total Quantity:", book["total"])
            print("Available Quantity:", book["available"])

            found = True

    if found == False:
        print("Book Not Found!")


# FUNCTION 6: ISSUE BOOK

def issue_book():

    book_id = input("Enter Book ID to Issue: ")
    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            if book["available"] > 0:

                student = input("Enter Student Name: ")

                if student == "":
                    print("Student Name cannot be empty!")
                    return

                book["available"] -= 1

                issued = {
                    "book_id": book_id,
                    "student": student
                }

                issued_books.append(issued)

                save_data()

                print("Book Issued Successfully!")
                print("Issued to:", student)
                print("Remaining Copies:", book["available"])

            else:
                print("Sorry! No Copies Available!")

            break

    if found == False:
        print("Book ID Not Found!")


# FUNCTION 7: RETURN BOOK

def return_book():

    book_id = input("Enter Book ID to Return: ")
    student = input("Enter Student Name: ")

    found = False

    for issued in issued_books:

        if (issued["book_id"] == book_id and
                issued["student"].lower() == student.lower()):

            found = True

            for book in books:

                if book["id"] == book_id:
                    book["available"] += 1
                    break

            issued_books.remove(issued)

            save_data()

            print("Book Returned Successfully!")
            break

    if found == False:
        print("No Matching Issue Record Found!")


# FUNCTION 8: VIEW ISSUED BOOKS

def view_issued_books():

    if len(issued_books) == 0:
        print("No Books Have Been Issued!")
        return

    print("\n------ ISSUED BOOK DETAILS ------")

    for issued in issued_books:

        print("Book ID:", issued["book_id"])
        print("Student Name:", issued["student"])
        print("---------------------------------")


# FUNCTION 9: DELETE BOOK

def delete_book():

    book_id = input("Enter Book ID to Delete: ")
    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            if book["available"] == book["total"]:

                books.remove(book)

                save_data()

                print("Book Deleted Successfully!")

            else:
                print("Cannot Delete! Some Copies Are Issued.")

            break

    if found == False:
        print("Book ID Not Found!")


# MAIN PROGRAM

def main():
    load_data()

    while True:

        print("\n================================")
        print("     LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Issued Books")
        print("7. Delete Book")
        print("8. Exit")
        print("================================")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            view_issued_books()

        elif choice == "7":
            delete_book()

        elif choice == "8":
            save_data()
            print("Thank You for Using Library Management System!")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
