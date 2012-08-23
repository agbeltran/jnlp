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

JNLP_TEMPLATE = """
<?xml version="1.0" encoding="utf-8"?>

<!DOCTYPE jnlp PUBLIC "-//Sun Microsystems, Inc//DTD JNLP Descriptor 6.0//EN" "http://java.sun.com/dtd/JNLP-6.0.dtd">
<!-- doctype points to Sun, not Oracle for compatibility. -->
<jnlp spec="6.0+" codebase="http://isatab.sourceforge.net/jnlp/" href="ISAcreator.jnlp" version="1.6">

	<information>
 		<title>ISAcreator 1.6</title>
 		<vendor>ISA team, Oxford e-Research Centre, University of Oxford, Oxford, UK</vendor>
 		<homepage href="http://isa-tools.org" />
 		<description>ISAcreator tool</description>
 		<version>1.6</version>
 		<icon href="http://isatab.sourceforge.net/jnlp/isacreator_logo.png"/>
 		 <shortcut online="true">
     		 <desktop />
    		  <menu submenu="ISAcreator" />
   		 </shortcut>
 		<offline-allowed/>
 	</information>

 	<security>
 		<all-permissions/>
 	</security>

 	<update check="always" policy="always" />

 	<resources>
 		<j2se version="1.5+" />
 		<jar href="http://isatab.sourceforge.net/jnlp/ISAcreator-1.6.jar" />
 	</resources>
	<application-desc main-class="org.isatools.isacreator.gui.modeselection.ModeSelector"/>
	$arguments
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
#    tmpl = loader.load('ISAcreator.jnlp')
#    fs = cgi.FieldStorage()
#    return tmpl.generate(title='ISAcreator 1.6',description='ISAcreator tool',submenu='ISAcreator',jar='http://isatab.sourceforge.net/jnlp/ISAcreator-1.6.jar').render('html', doctype='html')


def main():
    #print "Content-Type: text/plain;charset=utf-8"
    #print
    #print "Hello World!"

    from string import Template

    #### parse arguments
    fs = cgi.FieldStorage()
    args = ""

    for key in fs.keys():
        args =  args+"<argument>--"+key+"</argument>\n <argument>"+fs[key].value+"</argument>"
    jnlp = Template(JNLP_TEMPLATE)
    jnlp_file = open("/tmp/ISAcreator-parameters.jnlp", "w")
    jnlp_file.write(jnlp.substitute(arguments=args))
    jnlp_file.close()



main()