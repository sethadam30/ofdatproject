from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_sign_up(self):
        #When a user arrives at the OFAT homepage the following information
        #should be available: OFAT in title, signup/login, tabs for about,
        #contact

        self.browser.get('http://localhost:8000')
        self.assertIn('OFAT', self.browser.title)
        self.fail('Finish the test!')
        
        #The user is not yet registered and signs up

        #After signing up and logging in it no longer displays the
        #informational login, but the standard webapp layout for logged in
        #users

        #After signing up and having a first view of the full web app the user
        #quits OFAT

if __name__ == '__main__':
    unittest.main(warnings='ignore')
