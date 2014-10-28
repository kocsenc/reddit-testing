#!/usr/bin/env python2

import hashlib
import requests
import time
import unittest

base_url = 'http://zbox.student.rit.edu'

class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.session()

    def test_register(self):
        hash = hashlib.sha1()
        hash.update(str(time.time()))
        self.user_name = hash.hexdigest()[:10]
        payload = { 'user': self.user_name, 'passwd': 'password', 'passwd2': 'password' }
        response = self.session.post("{0}/api/register".format(base_url), data=payload)
        self.assertEquals(requests.codes.ok, response.status_code)

    def tearDown(self):
        payload = { 'user': self.user_name, 'passwd': 'password' }
        res = self.session.post("{0}/api/login".format(base_url), data=payload)

        payload = { 'user': self.user_name, 'passwd': 'password', 'confirm': True }
        res = self.session.post("{0}/api/delete_user".format(base_url), data=payload)

if __name__ == '__main__':
    unittest.main()
