# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:33:57 2018

@author: yao
"""

import sqlite3

test = sqlite3.connect('spider.sqlite')

create_table = 'create table novel (title varchar(128),author varchar(32),detail varchar(256))'

test.execute(create_table)

test.close()

