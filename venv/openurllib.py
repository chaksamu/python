from urllib import *
from urllib.request import *
import http.client
import email.parser
from email.feedparser import FeedParser, BytesFeedParser
from email._policybase import compat32
from email.utils import _has_surrogates
from email._parseaddr import quote
import time, calendar

#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print(line.strip())
