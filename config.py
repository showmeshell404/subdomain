# coding=utf-8
import sys
import random

# 是否开启https服务的证书校验
allow_ssl_verify = False
# 线程数
thread_count = 20
# timeout
timeout = 10
# 是否允许重定向
allow_redirects = True
# 是否允许继承http Request类的session支持，在发出的所有请求之间保存cookies
allow_http_session = True
# 是否允许随机useragent
allow_random_useragent = False
# 是否允许随机x_forward_for头
allow_random_x_forward = False

USER_AGENTS = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
]


def random_useragent(condition=False):
    if condition:
        return random.choice(USER_AGENTS)
    else:
        return USER_AGENTS[0]


def random_x_forward_for(condition=False):
    if condition:
        return '%d.%d.%d.%d' % (
            random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
    else:
        return '8.8.8.8'


headers = {
    'User-Agent': random_useragent(allow_random_useragent),
    'X_FORWARDED_FOR': random_x_forward_for(allow_random_x_forward),
    'Referer': 'http://www.baidu.com',
    'Cookie': "",
}
