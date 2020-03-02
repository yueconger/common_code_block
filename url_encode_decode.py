# -*- encoding: utf-8 -*-
"""
@File    : url_encode_decode.py
@Time    : 2020/3/2 10:52
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""

from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode


def url_encode(url):
    """
    URL转码
    :param url:
    :return: 转码后的url链接
    """
    url_encode_name = quote(url)
    return url_encode_name


def url_decode(url):
    """
    URL解码
    :param url:
    :return: 解码后的url
    """
    url_decode_name = unquote(url)
    return url_decode_name


def urlencode_process(url_data):
    """
    含有参数的类json结构处理
    :param url_data:   如:   url_data = {'name': 'iphone X', 'color': 'black'}
    :return: url链接
    """
    return urlencode(url_data)


if __name__ == '__main__':
    url_data = {'name': '小米手机10 pro', 'color': '星空蓝'}
    url = 'https://item.mi.com/product/' + urlencode_process(url_data)
    print(url)
