# encode = utf-8
__author__ = 'haifwu@ebay.com'

import urllib2, urllib
from init_op import Config
import json
import web
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


class WeChat:
    def __init__(self):
        app_config = Config("app.ini")
        self.appid = app_config.get("baseconf", "appid")
        self.secret = app_config.get("baseconf", "secret")
        self.token = self.get_token()
        self.render = web.template.render("../templates")

    def get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + self.appid \
              + "&secret=" + self.secret
        response = urllib2.urlopen(url)
        html = response.read()
        return json.loads(html)['access_token']

    def delete_menu(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=' + self.token
        return urllib2.urlopen(url).read()

    def get_menu(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=' + self.token
        return urllib2.urlopen(url).read()

    def create_menu(self):
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + self.token
        post = str(self.render.menu())
        request = urllib2.urlopen(url, post)
        return request.read()


if __name__ == '__main__':
    robot = WeChat()
    # print robot.create_menu()
    print robot.get_menu()
    # print robot.delete_menu()
    # print robot.get_token()
