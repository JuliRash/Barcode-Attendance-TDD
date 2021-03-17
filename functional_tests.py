import unittest
from selenium import webdriver
from decouple import config


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=config('webdriver_path'))

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online barcode attendance system.
        # she goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # she notices the page title and header mentions attendance.
        self.assertIn('Attendance', self.browser.title)
        self.fail('Finish the test ✔️')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

