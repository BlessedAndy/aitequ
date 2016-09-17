'''
Created on Sep 17, 2016

@author: Andy Zhang
'''

'''
$ mkdir pycon-scraper
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install requests beautifulsoup4
If you are using Microsoft Windows, note that the virtual environment activation command above 
is different, you should use venv\Scripts\activate.
'''

import requests
response = requests.get('http://pyvideo.org/category/50/pycon-us-2014')