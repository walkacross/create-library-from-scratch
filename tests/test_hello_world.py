#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import datetime
from my_library.functions import hello_world


class TestFundamentalFunction(unittest.TestCase):
    
    def test_hello_world(self):
        param = 2
        output = hello_world(param=param)
        
        today = datetime.date.today()
        to_string = "hello world to {} in {}".format(param, today)
        self.assertEqual(output, to_string)

#if __name__ == "__main__":
#    unittest.main()
