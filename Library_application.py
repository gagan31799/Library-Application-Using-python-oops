
#  Create class LibraryAdmin and add constructor
class LibraryAdmin:
  def __init__(self,list_books):
    list_books=list_books
    borrowers_dict={}

# Create Functions inside 'Library' class.

class LibraryAdmin:
  def __init__(self,list_books):
    self.list_books=list_books
    self.borrowers_dict={} 
  def display_books(self):
    #print(self.list_books)
    for i in self.list_books:
      print(i)
  def lend_book(self,book,borrower):
    if book not in self.borrowers_dict.keys():
        self.borrowers_dict.update({book:borrower})
        print('Book issued')        
    else:
        print("Sorry, this book is already Issued")

  def add_book(self,book):
    self.list_books.append(book)
    print("Book is sucessfully added in library")

  def collect_book(self,book):
    if(book not in self.borrowers_dict.keys()):
      print(f"{book} is Not in Borrower Dict")
    else:
      self.borrowers_dict.pop(book)
      print(f"{book} is successfully removed from library")

# Create an object of Library class and pass a list of books as a parameter
demo=LibraryAdmin(['C','Python','OOPs'])
# Call the functions
demo=LibraryAdmin(['C','Python','OOPs','java'])
while True:
  print('Enter:\n\t1 to Display Books.\n\t2 to lend a Book\n\t3 to add a book.\n\t4 to collect a Book.\n\t9 to quit the application. ')
  user_choice=int(input())
  if(user_choice  not in [1,2,3,4,9]):
    print('Please enter valid Input')
  if(user_choice==1):
    demo.display_books()
  elif(user_choice==2):
    book = input("Enter the name of the book to be lent:\n")
    borrower = input("Enter the name of the borrower:\n")
    demo.lend_book(book,borrower)
  elif(user_choice==3):
    book = input("Enter the name of the book you want to add:\n")
    demo.add_book(book)
  elif(user_choice==4):
    book = input("Enter the name of the book to be collected:\n")
    demo.collect_book(book)
  elif(user_choice==9):
    break
