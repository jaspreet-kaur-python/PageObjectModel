from pages.page3 import Page3


class Page2:
    def __init__(self, a):
        self.a = a

    def page2(self):
        print("in page 2")
        self.a = self.a + 5
        print("Updated value from page2 : " + str(self.a))
        return Page3(self.a)