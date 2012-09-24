#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import the CGI module
import cgi

# Import Template module
from string import Template

# enable debugging
# TODO remove in production version
import cgitb
cgitb.enable()

import os.path

JNLP_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>

<!DOCTYPE jnlp PUBLIC "-//Sun Microsystems, Inc//DTD JNLP Descriptor 6.0//EN" "http://java.sun.com/dtd/JNLP-6.0.dtd">
<!-- doctype points to Sun, not Oracle for compatibility. -->
<jnlp spec="6.0+" codebase=$codebase href=$href version="1.6">

    <information>
        <title>$title</title>
        <vendor>ISA team, Oxford e-Research Centre, University of Oxford, Oxford, UK</vendor>
        <homepage href="http://isa-tools.org" />
        <description>$description</description>
        <version>1.6</version>
        <icon href=$icon/>
        <shortcut online="true">
            <desktop />
            <menu submenu=$submenu />
        </shortcut>
        <offline-allowed/>
    </information>

    <security>
        <all-permissions/>
    </security>

    <update check="always" policy="always" />

    <resources>
        <j2se version="1.5+" />
        <jar href=$jar />
    </resources>
    <application-desc main-class=$mainclass/>
</jnlp>
"""

#import cherrypy
#from Genshi.template import TemplateLoader

#loader = TemplateLoader(
#    os.path.join(os.path.dirname(__file__), 'templates'),
#    auto_reload=True
#)

#@cherrypy.expose
#def index(self):
#    tmpl = loader.load('template.jnlp')
#    fs = cgi.FieldStorage()
#    return tmpl.generate(title='ISAcreator 1.6',description='ISAcreator tool',submenu='ISAcreator',jar='http://isatab.sourceforge.net/jnlp/ISAcreator-1.6.jar').render('html', doctype='html')


def main():
    from string import Template

    #### parse arguments
    fs = cgi.FieldStorage()
    args = ""

    for key in fs.keys():
        args =  args+"<argument>--"+key+"</argument>\n <argument>"+fs[key].value+"</argument>"

    codebase = '"http://isatab.sourceforge.net/jnlp/"'
    href = '"template.jnlp"'
    title = '"ISAcreator 1.7"'
    vendor = '"ISA team, Oxford e-Research Centre, University of Oxford, Oxford, UK"'
    homepage = '"http://isa-tools.org"'
    description = '"ISAcreator tool"'
    version = '"1.7"'
    icon = '"http://isatab.sourceforge.net/jnlp/isacreator_logo.png"'
    submenu = '"ISAcreator"'
    j2se_version = '"1.5+"'
    jar = '"http://toad.oerc.ox.ac.uk:8080/ISAcreator/ISAcreator-1.6.jar"'
    mainclass = '"org.isatools.isacreator.launch.ISAcreatorApplication"'




    jnlp = Template(JNLP_TEMPLATE)
    jnlp = jnlp.substitute(title=title,
                           vendor=vendor,
                           description=description,
                           icon=icon,
                           submenu=submenu,
                           mainclass=mainclass,
                           codebase=codebase,
                           href=href,
                           jar=jar,
                           arguments=args)

    filename = "template.jnlp"

    print "Content-Type:application/x-download\nContent-Disposition:attachment;filename=%s\n\n%s" % (filename,jnlp)
    #print "Content-Length:%s\n\n%s" %   jnlp, len(jnlp), jnlp#(os.path.split(jnlp)[-1], len(buff), buff)

main()