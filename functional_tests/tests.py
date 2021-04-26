import unittest
import time
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from decouple import config
# from django.test import

from barcode.tests.test_models import generate_demo_person_data, generate_demo_setup_data


class NewVisitorTestBeforeConfiguration(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=config('webdriver_path'))
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_guest_visits_application_not_configured(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Application Not Configured', self.browser.page_source)


class NewVisitorTestAfterConfiguration(StaticLiveServerTestCase):
    MAX_WAIT = 10

    def setUp(self):
        self.person = generate_demo_person_data('0909')
        self.browser = webdriver.Chrome(executable_path=config('webdriver_path'))
        self.site_setup = generate_demo_setup_data()

    def tearDown(self):
        self.browser.quit()

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices there is no input box but an instruction
        # for her to use the barcode scanner to mark her attendance.
        input_box = self.browser.find_element_by_id("code")
        self.assertTrue(input_box.get_attribute('autofocus'))

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("user_info")
                rows = table.find_elements_by_tag_name("h5")
                self.assertIn(row_text, str([row.text for row in rows]))
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_submit_attendance_and_is_successful(self):
        # Edith previously used barcode attendance system.
        # she goes to check out its homepage and enter her the code of her account.
        self.browser.get(self.live_server_url)

        # she notices the page title and header mentions Attendance.
        self.assertIn('Attendance', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(self.site_setup.organization_name, header_text)
        # she is invited to input her identity number straight away.
        input_box = self.browser.find_element_by_id('code')
        # she types "0909" which is a correct code into the text box and clicks enter
        input_box.send_keys('0909')
        # when she hits enter, the page sends a post request to the mark attendance end-point,
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('0909')
        self.wait_for_row_in_list_table('julipels')
        # if the number is correct it redirects her to marked attendance page,
        # and shows her her information containing [full_name, id_number, phone_number]
        # "Her Full name
        # self.fail('Finish the test ✔️')

    def test_can_submit_attendance_and_is_not_successful(self):
        # Edith has heard about a cool new online barcode attendance system.
        # she goes to check out its homepage but has no account.
        self.browser.get(self.live_server_url)

        # she notices the page title and header mentions Attendance.
        self.assertIn('Attendance', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(self.site_setup.organization_name, header_text)
        # she is invited to input her identity number straight away.
        input_box = self.browser.find_element_by_id('code')
        # she types "0908" which is a wrong code into the text box and clicks enter
        input_box.send_keys('0908')
        # when she hits enter, the page sends a post request and display the user information as output.
        input_box.send_keys(Keys.ENTER)
        self.assertIn('Error', self.browser.find_element_by_id('error').text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
