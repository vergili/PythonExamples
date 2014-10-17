import re


def find(selector, text):
    
    match = re.search(selector,text)
    
    if match:
	print match.group()
    else:
	print "not found"
	

find('...g','called piiig')
#iiig


find('...g','called piiig much better: xyzg')
#iiig

find('x..g','called piiig much better: xyzg')
#xyzg

find('..gs','called piiig much better: xyzgs')
#yzgs

find('c\.l','c.lled piiig much better: xyzgs')
#c.l

find(r':\w\w\w','blah :cat blah blah')
#:cat

find(':\w\w\w','blah :cat blah blah')
#:cat

find('\d\d\d','blah :123xxx')
#123

find(r'\d\d\d','blah :123xxx')
#123

find(r'\d\s\d\s\d','blah :1 2 3')
#1 2 3

find(r'\d\s+\d\s+\d','blah :1     2                 3')
#1     2                 3

find(r':\w+','blah blah :kitten blah blah')
#:kitten

find(r':\w+','blah blah :kitten123 blah blah')
#:kitten123

find(r':\w+','blah blah :kitten123& blah blah')
#:kitten123

find(r':.+','blah blah :kitten123& blah blah')
#:kitten123& blah blah

find(r':\w+','blah blah :kitten123123 blah blah')
#:kitten123123

find(r':\S','blah blah :kitten123123&a=123&yatta blah bla')
#:k

find(r':\S+','blah blah :kitten123123&a=123&yatta blah bla')
#:kitten123123&a=123&yatta


find(r'\w+@\w+','blah blah nick.p@gmail.com  yatta @')
#p@gmail

find(r'[\w.]+@\w+','blah blah nick.p@gmail.com  yatta @')
#nick.p@gmail

find(r'[\w.]+@[\w.]+','blah blah nick.p@gmail.com  yatta @')
#nick.p@gmail.com


find(r'[\w.]+@[\w.]+','blah blah .nick.p@gmail.com  yatta @')
#.nick.p@gmail.com

find(r'\w[\w.]+@[\w.]+','blah blah .nick.p@gmail.com  yatta @')
#nick.p@gmail.com

find(r'\w[\w.]*@[\w.]+','blah blah .nick.p@gmail.com  yatta @')
#nick.p@gmail.com


m = re.search(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com  yatta @')

m.group()
#'nick.p@gmail.com'

m.group(1)
#'nick.p'

m.group(2)
#'gmail.com'


re.findall(r'[\w.]+@[\w.]+','blah nick.p@gmail.com  yatta @')
#['nick.p@gmail.com']

re.findall(r'[\w.]+@[\w.]+','blah nick.p@gmail.com  foo@bar')
#['nick.p@gmail.com', 'foo@bar']

re.findall(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com  foo@bar')
#[('nick.p', 'gmail.com'), ('foo', 'bar')]



