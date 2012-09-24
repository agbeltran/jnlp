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

with open('./templates/template.jnlp', 'r') as f:
    JNLP_TEMPLATE = f.read()

def main():
    from string import Template

    #### parse arguments
    fs = cgi.FieldStorage()
    args = ""

    for key in fs.keys():
        args =  args+"<argument>--"+key+"</argument>\n <argument>"+fs[key].value+"</argument>"

    codebase = '"http://toad.oerc.ox.ac.uk:8080/ISAcreator/"'
    href = '"ISAcreator.jnlp"'
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
    jnlp = jnlp.substitute(codebase=codebase,
                           href=href,
                           title=title,
                           vendor=vendor,
                           homepage=homepage,
                           description=description,
                           version=version,
                           icon=icon,
                           submenu=submenu,
                           j2se_version=j2se_version,
                           mainclass=mainclass,
                           jar=jar,
                           arguments=args)

    filename = "ISAcreator.jnlp"

    print "Content-Type:application/x-download\nContent-Disposition:attachment;filename=%s\n\n%s" % (filename,jnlp)

main()