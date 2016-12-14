#http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

txt = urllib2.urlopen(url).read()

t2 = pickle.loads(txt)

print t2

print ('\n'.join([''.join([p[0] * p[1] for p in row]) for row in t2]))


#channel