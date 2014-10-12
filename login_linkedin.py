import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html)
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'test@email.com',
    'session_password':'xxxxxx',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

test = client.get('https://www.linkedin.com/profile/view?id=162313837').content

soup1 = BeautifulSoup(test)

print soup1.find("title")

