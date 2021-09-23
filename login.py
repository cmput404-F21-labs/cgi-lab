#!/usr/bin/env python3

import cgi
import cgitb
import secret
from templates import after_login_incorrect

form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

print(f"Context-type: text/html")
if (username == secret.username and password == secret.password):

    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
    print()
    print("<html>")
    print("<head>")
    print("<title>Some title</title>")
    print("</head>")
    print("<body>")

    print("<p><b>Username:</b> %s </p>" % (username))
    print("<p><b>Password:</b> %s </p>" % (password))
    print("<body>")
    print("<html>")
else: 
    print(after_login_incorrect())

