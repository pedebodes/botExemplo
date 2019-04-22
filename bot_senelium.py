from seleniumbase import BaseCase
import time
class MyTestClass(BaseCase):

    # def test_basic(self):
    #     self.open("https://xkcd.com/353/")
    #     self.assert_element('img[alt="Python"]')
    #     self.click('a[rel="license"]')
    #     self.assert_text("free to copy", "div center")
    #     self.open("https://xkcd.com/1481/")
    #     title = self.get_attribute("#comic img", "title")
    #     self.assert_true("86,400 seconds per day" in title)
    #     self.click("link=Blag")
    #     self.assert_text("The blag of the webcomic", "h2")
    #     self.update_text("input#s", "Robots!\n")
    #     self.assert_text("Hooray robots!", "#content")
    #     self.open("https://xkcd.com/1319/")
    #     self.assert_exact_text("Automation", "#ctitle")   

    def test_basic(self):
        
        self.open("https://xkcd.com/1481/")
        # time.sleep(15)
        self.click("link=Blag")
        self.assert_text("The blag of the webcomic", "h2")
        self.update_text("input#s", "Robots!\n")
        self.assert_text("Hooray robots!", "#content")
        self.open("https://xkcd.com/1319/")
        self.assert_exact_text("Automation", "#ctitle")

    # def test_delayed_asserts(self):
    #     self.open('https://xkcd.com/993/')
    #     self.wait_for_element('#comic')
    #     self.delayed_assert_element('img[alt="Brand Identity"]')
    #     self.delayed_assert_element('img[alt="Rocket Ship"]')  # Will Fail
    #     self.delayed_assert_element('#comicmap')
    #     self.delayed_assert_text('Fake Item', '#middleContainer')  # Will Fail
    #     self.delayed_assert_text('Random', '#middleContainer')
    #     self.delayed_assert_element('a[name="Super Fake !!!"]')  # Will Fail
    #     self.process_delayed_asserts()