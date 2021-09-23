#!/usr/bin/env python3
import os,json
from http.cookies import SimpleCookie
import secret

from templates import secret_page

print("Content-type:text/html\r\n\r\n")
print()
print("<title>Test CGI</title>")
print("<p>Hello World</p>")


# print(os.environ)
json_str = json.dumps(dict(os.environ), indent = 4)
resp = json.loads(json_str)

# print query param
print("<p>" + resp['QUERY_STRING'] + "</p>")
# print user agent
user_agent = str.split(resp['HTTP_USER_AGENT'], " ")
print("<p>" + user_agent[0] + "</p>")

# decode cookie and print secret if logged in
cookie = SimpleCookie()
cookie.load(resp["HTTP_COOKIE"])
if (cookie['username'].value == secret.username and cookie['password'].value == secret.password):
    print(secret_page(secret.username, secret.password))

