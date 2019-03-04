# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  

setup(
        name='name10x',     # 包名字
        version='0.0.1',   # 包版本
        description='This is a python tool detecting index information for 10x data',   # 简单描述
        author='Sijie Chen',  # 作者
        author_email='chansigit@gmail.com',  # 作者邮箱
        url='https://github.com/chansigit/name10x',      # 包的主页
        scripts=['n10', 'name10x.py']
)
