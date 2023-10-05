from app import create_app
from selenium import webdriver
import unittest

class SeleniuemTestCase(unittest.TestCase):
    client = None
    
    @classmethod
    def setUpClass(cls):
        #start chrome
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        try:
            cls.client = webdriver.Chrome(chrome_options=options)
        except:
            pass
        
        #skip these tests if the browser could not be started
        if cls.client:
            #create the application
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()
            
            #suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel('ERROR')