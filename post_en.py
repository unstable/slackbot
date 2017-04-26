#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime
import os
import subprocess
import urllib.request

response = urllib.request.urlopen('http://hq.sinajs.cn/list=sz002131')
html = response.read()
stock_list = str(html, encoding = "gb2312").replace(";\n",'').replace("var hq_str_",'').replace("=",',').replace('"','').split(",")
#content = 'code: %s, open: %s, close: %s, current: %s, high: %s, low: %s, TIME: %s' % (stock_list[0], stock_list[2], stock_list[3], stock_list[4], stock_list[5],
#                          stock_list[6], stock_list[31] + ' ' + stock_list[32])
content = '利欧股份: %s, 今日开盘: %s, 昨日收盘: %s, 当前: %s, 最高: %s, 最低: %s, time: %s' % (stock_list[0], stock_list[2], stock_list[3], stock_list[4], stock_list[5], stock_list[6], stock_list[31] + ' ' + stock_list[32])
print(content)

content_json = '{"code": "%s", \n"open": %s, \n"close": %s, \n"current": %s, \n"high": %s, \n"low": %s, ' \
                          '\n"time": "%s"}\n' % (stock_list[0], stock_list[2], stock_list[3], stock_list[4], stock_list[5],
                          stock_list[6], stock_list[31] + ' ' + stock_list[32])
print(content_json)


#file_object = open('002131.txt')
#file_context = file_object.read().rstrip('\n')
#pprint(file_context)


#curl -X POST --data-urlencode 'payload={"channel":"test","text":"[' + data_file + ']", "icon_emoji":":ghost:"}' https://hooks.slack.com/services/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

#postcmd = 'curl -X POST --data-urlencode \'payload={"channel":"test","text":"CNMarket", "attachments":[' + content_json + ']}\' https://hooks.slack.com/services/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'
postcmd = 'curl -X POST --data-urlencode \'payload={"channel":"behappy","text":"[' + content + ']"}\' https://hooks.slack.com/services/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'
subprocess.call(postcmd, shell=True)


#postcmd_k = 'curl -X POST --data-urlencode \'payload={"channel":"behappy","text":"http://image.sinajs.cn/newchart/min/n/sz002131.gif"}\' https://hooks.slack.com/services/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'
#subprocess.call(postcmd_k, shell=True)

