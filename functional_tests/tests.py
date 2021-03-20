import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import config
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=config('webdriver_path'))

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id("list_user_info")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_submit_attendance(self):
        # Edith has heard about a cool new online barcode attendance system.
        # she goes to check out its homepage.
        self.browser.get(self.live_server_url)

        # she notices the page title and header mentions Attendance.
        self.assertIn('Attendance', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Attendance', header_text)
        # she is invited to input her identity number straight away.
        input_box = self.browser.find_element_by_id('id_number')
        # she types "0909" into the text box and clicks enter
        input_box.send_keys('0909')
        # when she hits enter, the page sends a post request to the mark attendance end-point,
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('0909')
        self.check_for_row_in_list_table('Edith')
        # self.assertIn('Edith', [row.text for row in rows])
        # if the number is correct it redirects her to marked attendance page,
        # and shows her her information containing [full_name, id_number, phone_number]
        # "Her Full name
        self.fail('Finish the test ✔️')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
