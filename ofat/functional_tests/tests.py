from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up(self):
        #When a user arrives at the OFAT homepage the following
        #information should be available: OFAT in title and header,
        #signup/login, tabs for about, contact

        self.browser.get(self.live_server_url)
        self.assertIn('OFAT', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('OFAT', header_text)
        
        #The user is not yet registered and signs up
        #User goes to the registration page

        #User looks for the inputbox for his name
        inputbox = self.browser.find_element_by_id('id_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Your name'
        )
        #User types his name
        inputbox.send_keys('Test User')
        inputbox.send_keys(Keys.ENTER)

        #After signing up and logging in it no longer displays the
        #informational login, but the standard webapp layout for logged in
        #users

        #After signing up and having a first view of the full web app the user
        #quits OFAT

    def test_layout_and_styling(self):
        #User goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        #User notices input box
        inputbox = self.browser.find_element_by_id('id_username')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
        
