import sys
import json 

class functions: # <------ this is a class for the functions group that the library manager will perform
    def __init__(self):
        filename = "Library_Books.txt"
        self.books_list = []
        with open (filename, 'r') as f:
            self.books_list = json.load(f)


    def add_book(self): # <------ this function will register new books in the library
        while True:
            try:
                name = input("enter the name of the book : ")
                author = input("enter the name of the author of the book : ")
                genre = input("enter the name of genre/category of the book : ")
                price = float(input("enter the price of the book (In dollars Please): "))
                self.books_list.append({"name":name,"author":author,"genre":genre,"price":price})
                with open ("Library_Books.txt", "w") as f:
                    json.dump(self.books_list,f)
                print(f"The Book {name} added to the Library Records!")
                another_book = input("Do you want to add another book(y/n): ").lower()
                if another_book not in ("y","yes"):
                    break

            except ValueError:
                print("Invalid price format please enter a valid numerical Value!")

    def remove_books(self):
        while True:
            try:
                num = int(input("enter the number of books you want to remove: "))
                if num > len(self.books_list):
                    raise ValueError("Invalid number of books. There are only {} books in the library.".format(len(self.books_list)))
                for i in range(num):
                    name = input("enter the name of the book to remove: ")
                    book_index = -1
                    for i,book in enumerate(self.books_list):
                        if book["name"] == name:
                            book_index = i
                            break
                    if book_index != -1:
                        del self.books_list[book_index]
                        with open("Library.txt","w") as f:
                            json.dump(self.books_list, f)
                        print(f"The Book {name} is removed successfully!")
                    else:
                        print(f"The Book {name} not found in the Library Records!")
                break    
            except ValueError as e:
                print(e)
                break


    def total_books(self): # <------ this function will count the total number of books present in the library 
        for book in self.books_list:
            print("| Book-Name |" + " Author |" + " Genre |" + " Price |")
            print(f'{book["name"]} + {book["author"]} + {book["genre"]} + ${book["price"]} ')
    def author_collection(): # <------ this function will tell the count of books that are of a specific author
        pass
    def genre_collection(): # <------ this function will tell the count of books that are of a specific genre
        pass
    def price_changer(): # <------ this function will change the price of the books present in the library
        pass
    def about(): # <------ this function will tell the instructions to use this program
        pass






Func = functions() # <------ Initialisation of functions as an object

def main(): # <------ the main function that will perform all the tasks
    print("_____________________LIBRARY MANAGER_____________________")
    # print("| Book-Name |" + " Author |" + " Genre |" + " Price |")
    # print(f"{book_name}" + f"{author_name}" + f"{genre}" + f"{price}")
    print()
    # print()
    print("_____________________LIBRARY FUNCTIONS_____________________")
    print(" (1) Add a Book \n (2) Total Books \n (3) Author's Collection \n (4) Genre Wise Collection \n (5) Price Changer \n (6) Remove a Book \n (7) About/Instructions \n (8) Exit \n ")
    choice = int(input(": ")) # <------ Interacting to the choices via user
    if choice == 1:
        Func.add_book()
    elif choice == 2:
        Func.total_books()
    elif choice == 3:
        Func.author_collection()
    elif choice == 4:
        Func.genre_collection()
    elif choice == 5:
        Func.price_changer()
    elif choice == 6:
        Func.remove_books()
    elif choice == 7:
        Func.about()
    elif choice == 8:
        sys.exit()
    else:
        print("Wrong Input Try Again!")
        main() # <------ reinitiating of the function so that the user can input again   

    

if __name__ == "__main__":
    main() # <------ The main function running separately 