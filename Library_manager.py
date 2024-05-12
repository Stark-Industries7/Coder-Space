import sys

class functions: # <------ this is a class for the functions group that the library manager will perform
    def add_book(self,Book_name,Author,Genre,Price): # <------ this function will register new books in the library
    #     self.Book_name = Book_name
    #     self.Author = Author
    #     self.Genre = Genre
    #     self.Price = Price
        pass
    def total_books(): # <------ this function will count the total number of books present in the library 
        pass
    def author_collection(): # <------ this function will tell the count of books that are of a specific author
        pass
    def genre_collection(): # <------ this function will tell the count of books that are of a specific genre
        pass
    def price_changer(): # <------ this function will change the price of the books present in the library
        pass






Func = functions() # <------ Initialisation of functions as an object

def main(): # <------ the main function that will perform all the tasks
    print("_____________________LIBRARY MANAGER_____________________")
    print("Book-Name " + " Author " + " Genre " + " Price ")
    # print(f"{book_name}" + f"{author_name}" + f"{genre}" + f"{price}")
    print()
    print()
    print("_____________________LIBRARY FUNCTIONS_____________________")
    print(" (1) Add a Book \n (2) Total Books \n (3) Author's Collection \n (4) Genre Wise Collection \n (5) Price Changer \n (6) About/Instructions \n ")
    choice = int(input(": ")) # <------ Interacting to the choices via user
    if choice == 1:
        pass
    elif choice == 2:
        pass 
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        sys.exit()
    else:
        print("Wrong Input Try Again!")
        main() # <------ reinitiating of the function so that the user can input again   

    

if __name__ == "__main__":
    main() # <------ The main function running separately 