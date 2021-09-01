from unittest import TestCase


class Test(TestCase):
    def test_draw(self):
        self.assertTrue(1, 2)


class Test(TestCase):
    def test_main_window(self):
        self.assertTrue(640, 480)


class Test(TestCase):
    def test_new_window(self):
        self.assertTrue(540, 380)


class Test(TestCase):
    def test_login_form(self):
        self.assertTrue(35,5)
