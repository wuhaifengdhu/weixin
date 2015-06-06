# coding: utf-8
import sys, os, time
import ConfigParser
import web
from module.init_op import Config

import os

def main(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)

    s = cf.sections()
    print 'section:', s

    o = cf.options("baseconf")
    print 'options:', o

    v = cf.items("baseconf")
    print 'items:', v

    appid = cf.get("baseconf", "appid")
    print "appid:", appid

    config = Config("./config/app.ini")
    config.set("baseconf", "author", "wu haifeng")
    author = config.get("baseconf", "author")
    print "author:", author


if __name__ == '__main__':
    app_root = os.path.dirname(__file__)
    template_root = os.path.join(app_root, 'templates')
    render = web.template.render(template_root)
    reply = str(render.menu(u"吴海峰"))
    print reply.decode('utf-8').encode('gbk')
