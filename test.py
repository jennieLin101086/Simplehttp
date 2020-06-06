#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-
import sys,os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
# print(BASE_DIR)
# sys.path.append(BASE_DIR)

import unittest
from simplehttp.simplehttp import get_json,post_json
import json



class TestSimpleHttp(unittest.TestCase):
    def test_get_json_1(self):
        r = get_json('https://httpbin.org/get',None)
        self.assertTrue( r['args'] == {})


    def test_get_json_2(self):
        r = get_json(
            'https://httpbin.org/get?debug=true',
             params={'name': u'常⾒問題 Q&A'})

        self.assertTrue( r['args'] == {'debug': 'true', 'name': u'常⾒問題 Q&A'})


    def test_post_json_1(self):
        data = {'isbn': '9789863479116', 'title': u'流暢的 Python'}
        r = post_json(
            'https://httpbin.org/post',
            params={'debug':'true'}, 
            data=data)
       
        self.assertTrue( r['args'] ==  {'debug': 'true'})


    def test_post_json_2(self):
        data = {'isbn': '9789863479116', 'title': u'流暢的 Python'}
        r = post_json(
            'https://httpbin.org/post',
            params={'debug':
            'true'}, 
            data=data)
        self.assertTrue( json.loads(r['json']) == data)


# class TestException(unittest.TestCase):   

#     def test_assert_raises(self):                    
#         with self.assertRaises(ValueError):
#             get_json('https://httpbin.org/status/400',None)
            # sys.last_value.status_code = 400
            # self.assertTrue(sys.last_value.status_code == 400) 
        


if __name__ == '__main__':
    unittest.main()


