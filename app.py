from sre_constants import SUCCESS
from turtle import goto
from books import Book
import bookSDK

"""
CONSOLE APPLICATION TO MANAGE A READING LIST
BY BEN ADENLE // datapitch@gmail.com // 08099999928
"""



#START PROGRAM
print("""

        ############################
        WELCOME TO YOUR READING LIST
        ############################
        """)

def start_menu():
    def print_menu():
        print (
        """
        What would you like to do?
        ------------------------------
        Select a number to proceed...
        ------------------------------
        1. View your reading list
        2. Add a book to your list
        3. Update a book in your list
        4. Remove a book from your list
        0. QUIT this app!

        ##############################

        """)
    def print_sub_menu():
        print("""
                        Press 1 to return to the main menu, 
                        0 to quit the app...""")
    def context_menu():
        while(True):
                print_sub_menu()
                sub_menu_selection = int(input())
                if sub_menu_selection == 1:
                    start_menu()
                else:
                    print("THANKS FOR USING THIS APP")
                break

    while(True):
        print_menu()
        selection = int(input())
        
        #SHOW BOOKS BLOCK
        if selection == 1:
            print("""
            ---------------------------------------
            Here are the books in your reading list
            ---------------------------------------
            Press 1 to return to the main menu, 
            0 to quit the app..."""
            )

            books = bookSDK.get_book()
            sn = 1
            for item in books:
                print(f"""
                -
                {sn}. {item} """)
                sn += 1
            context_menu()

        #ADD BOOK BLOCK
        elif selection == 2:
            print("""
            ------------------------------------
            Adding a book to your reading list
            ------------------------------------""")
            
            title = input("""
            What is the title of the book? \n""")

            pages = int(input("""
            How many pages is the book?\n"""))
        
            
            print(f"""
            ----------------------SUCCESS!
            {title} with {pages} pages have been successfully added to your reading list""")
            
            context_menu()
        
        # UPDATE BOOK BLOCK
        elif selection == 3:
            print("""
            ------------------------------------
            Updating a book in your reading list
            ------------------------------------""")
            
            current_title = input("""
            Current title? \n""")

            current_pages= int(input("""
            Current pages \n"""))

        
            new_title = input("New title, [enter s for same]\n")
            if str.lower(new_title) == 's':
                new_title = current_title

            new_pages= input("New pages [enter s for same]\n")
            if str.lower(new_title) == "s":
                new_pages = current_pages

            book = bookSDK.update_a_book(Book(current_title, current_pages), new_title, new_pages)
            
            print(book, " has been updated!")
            context_menu()

        elif selection == 4:
            print("""
            ------------------------------------
            Removing a book to your reading list
            ------------------------------------""")
            title = input("""
            What is the title of the book would like to remove? \n""")
            
            if print(bookSDK.delete_a_book(title)):
                print(f"""
                ----------------------SUCCESS!
                {title} have been successfully removed from your reading list""")
                context_menu()

        else:
            print("""
            ------------------------------------
            HAVE A NICE TIME READING...
            ----------------------------
            This app is made with love by
            Ben Adenle to teaching purposes

            """)
        break

start_menu()

