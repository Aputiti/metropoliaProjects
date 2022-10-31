class Release:
    def __init__(self, release_name):
        self.release_name = release_name


class Book(Release):
    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_details(self):
        print(f"Book details:\nNAME: {self.release_name}\nAUTHOR: {self.author}\nPAGECOUNT: {self.pagecount}\n")


class Magazine(Release):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_details(self):
        print(f"Magazine details:\nNAME: {self.release_name}\nEDITOR: {self.editor}\n")


book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)
magazine1 = Magazine("Aku Ankka", "Aki Hyyppä")

book1.print_details()
magazine1.print_details()
