class Library:
  def __init__(self):
    self.nobooks = 0
    self.books = []

  def addbook(self, book):
    self.books.append(book)
    self.nobooks = len(self.books)


  def showInfo(self):
    print(f"the library has {self.nobooks} books ")



l1 = Library()
l1.addbook("harrypotter1")  
l1.addbook("harrypotter2")
l1.addbook("harrypotter3")
l1.addbook("harrypotter4")
l1.showInfo()

