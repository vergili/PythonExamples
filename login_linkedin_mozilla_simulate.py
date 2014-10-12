import cookielib
import os
import urllib
import urllib2
import re
import string
from BeautifulSoup import BeautifulSoup

username = "teset@email.com"
password = "xxxxxxxx"

cookie_filename = "parser.cookies.txt"  #bu isim ayn? kal?nca hata veriyor

class LinkedInParser(object):

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        # Simulate browser with cookies enabled
        self.cj = cookielib.MozillaCookieJar(cookie_filename)
        if os.access(cookie_filename, os.F_OK):
            self.cj.load()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # Login
        self.loginPage()

        title = self.loadTitle()
        print title

        self.cj.save()


    def loadPage(self, url, data=None):
        """
        Utility function to load HTML from URLs for us with hack to continue despite 404
        """
        # We'll print the url in case of infinite loop
        # print "Loading URL: %s" % url
        try:
            if data is not None:
                response = self.opener.open(url, data)
            else:
                response = self.opener.open(url)
            return ''.join(response.readlines())
        except:
            # If URL doesn't load for ANY reason, try again...
            # Quick and dirty solution for 404 returns because of network problems
            # However, this could infinite loop if there's an actual problem
            return self.loadPage(url, data)

    def loginPage(self):
        """
        Handle login. This should populate our cookie jar.
        """
        html = self.loadPage("https://www.linkedin.com/")
        soup = BeautifulSoup(html)
        csrf = soup.find(id="loginCsrfParam-login")['value']

        login_data = urllib.urlencode({
            'session_key': self.login,
            'session_password': self.password,
            'loginCsrfParam': csrf,
        })

        html = self.loadPage("https://www.linkedin.com/uas/login-submit", login_data)
        return

    def loadTitle(self):
        html = self.loadPage("http://www.linkedin.com/nhome/")
        soup = BeautifulSoup(html)
        return soup.find("title")

parser = LinkedInParser(username, password)

