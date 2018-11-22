"""Main test."""

import time
import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    """HomePage testcase."""

    def setUp(self):
        """Initiate test."""
        self.browser = webdriver.Firefox()

    def test_home_page(self):
        """Test admin page."""
        self.browser.get('http://localhost:8046/admin/login/')
        self.assertIn('Log in', self.browser.title)
        legend = self.browser.find_element_by_tag_name('legend')
        self.assertIn("Django administration - Log in", legend.text)
        username_input = self.browser.find_element_by_id("id_username")
        paswd_input = self.browser.find_element_by_id("id_password")
        username_input.send_keys("hr")
        paswd_input.send_keys("UploadExcel@123")
        form = self.browser.find_element_by_id("login-form")
        form.submit()
        time.sleep(3)
        headding = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Site administration',headding.text, 'Not Login.')


    def tearDown(self):
        """Quit test."""
        # self.browser.quit()
        pass


if __name__ == '__main__':
    unittest.main()
