#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import the CGI module
import cgi

# enable debugging
# TODO remove in production version
import cgitb
cgitb.enable()


def main():
    #print "Content-Type: text/plain;charset=utf-8"
    #print
    #print "Hello World!"
    fs = cgi.FieldStorage()
    print "Content-type: text/plain\n\n"
    for key in fs.keys():
        print "%s = %s" % (key, fs[key].value)


main()