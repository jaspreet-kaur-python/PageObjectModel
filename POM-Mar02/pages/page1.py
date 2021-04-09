from pages.page2 import Page2


class Page1:
    def __init__(self, a):
        self.a = a

    def page1(self):
        print("in page 1")
        self.a = self.a+5
        print("Updated value from page1 : "+str(self.a))
        return Page2(self.a)