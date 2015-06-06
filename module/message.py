# encode = utf-8
__author__ = 'haifwu@ebay.com'

import urllib2, urllib
from init_op import Config
import json
import web
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class Message:

    def __init__(self, xml):
        self.dic = self.parse(xml)

    def parse(self, xml):
        xml_dic = {}
        items = ET.fromstring(xml)
        for item in items:
            xml_dic[item.tag] = item.text
        return xml_dic

    def controller(self):
        if(self.dic['MsgType'] == 'event'):
            print 'it is a event'
        elif(self.dic['MsgType'] == 'text'):
            print 'it is a text'
        else:
            print "I can not recoginize"


def _test():
    test_sample  = '''
<xml>
<ToUserName><![CDATA[{TO_USER}]]></ToUserName>
<FromUserName><![CDATA[{FROM_USER}]]></FromUserName>
<CreateTime>{TIME_STEMP}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{RESPONSE_CONTENT}]]></Content>
</xml>
'''
    message = Message()
    response_dic = message.parse(test_sample)
    print response_dic
    print response_dic['FromUserName']

if __name__ == '__main__':
    _test()
