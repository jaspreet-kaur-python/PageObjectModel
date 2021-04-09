class Page3:
    def __init__(self,a):
        self.a = a

    def page3(self):
        print("in page 3")
        self.a = self.a + 5
        print("Updated value from page3 : " + str(self.a))