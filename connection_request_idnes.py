#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 08:48:49 2019

@author: martingrossman

This module uses Jizdni rady for finding connections. 
Result is pyquery object.
Copied from : https://forum.root.cz/index.php?topic=18466.30

#ToDo:
* parse res_d using pyrequest


Requirement: pip install requests-html

"""

from requests_html import HTMLSession

MESTO = 'praha'
ODKUD, KAM = 'dunajecka', 'radlicka'
URL = 'https://jizdnirady.idnes.cz/%s/spojeni/' % MESTO

def fill_form(d, odkud, kam):
    d('label:contains("Odkud")').parent().find('input').val(odkud)
    d('label:contains("Kam")').parent().find('input').val(kam)
    return d

def form_data(d):
    return {e.name:e.value for e in d('form input')}

session = HTMLSession()
d = session.get(URL).html.pq
data = form_data(fill_form(d, ODKUD, KAM))
res_d = session.post(URL, data=data).html.pq
print(res_d,file=open("response.html", "a"))

