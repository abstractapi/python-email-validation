import unittest
import os, sys

from python_email_validation import AbstractEmailValidation
from dotenv import load_dotenv

load_dotenv()

EMAIL_VAL_API_KEY = os.getenv('EMAIL_VAL_API_KEY')


class TestAbstractEmailValidation(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestAbstractEmailValidation, self).__init__(*args, **kwargs)
        self.api = AbstractEmailValidation()

    def test_no_config(self):

        with self.assertRaises(Exception):
            # tests aren't always run in order, so make sure to
            # clear api_key
            AbstractEmailValidation.api_key = None
            AbstractEmailValidation.verify("contact.email@gmail.com")

    def test_config(self):

        AbstractEmailValidation.configure(EMAIL_VAL_API_KEY)
        AbstractEmailValidation.verify("contact.email@gmail.com")


if __name__ == '__main__':
    unittest.main()