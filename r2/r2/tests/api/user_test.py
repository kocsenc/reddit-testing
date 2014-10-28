#!/usr/bin/env python2

import hashlib
import requests
import time
import unittest

base_url = 'http://zbox.student.rit.edu'

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()

    def test_login(self):
        payload = { 'user': 'test_user', 'passwd': 'password' }
        response = self.session.post("{0}/api/login".format(base_url), data=payload)
        self.assertEqual(requests.codes.ok, response.status_code)

    def test_me(self):
        response = self.session.get("{0}/api/me.json".format(base_url))
        self.assertEqual(requests.codes.ok, response.status_code)

if __name__ == '__main__':
    unittest.main()
