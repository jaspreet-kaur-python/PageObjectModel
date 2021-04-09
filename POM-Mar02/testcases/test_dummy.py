from pages.page1 import Page1


class TestDummy:
    def test_dummy(self):
        a = 10
        p1 = Page1(a)
        p2 = p1.page1()
        p3 = p2.page2()
        p3.page3()
