#!/bin/env python
import string
import mmap
import re

__doc__ = """This class helps user generate html code from within your python \
        code"""

__doctype__ = "<!DOCTYPE html>"


class pyhtml:
    def __init__(self, title="My Web Page"):
        self.title = title
        self.html()

    def html(self):
        """This function generates 4 tags & end tags that are always there\
                in an html file namely <html>, <head>, <title>, <body>"""

        with open("file", "w") as f:
            f.write("%s\n\
                    <html>\n\
                    <head>\n\
                    <title>%s</title>\n\
                    </head>\n\
                    <body>\n\
                    </body>\n\
                    </html>" % (__doctype__, self.title))

    def external_css(self, **kwargs):
        """ This function adds an external CSS to the html file. An external\
                CSS is ideal when a style is to be applied to multiple pages"""

        with open("file", "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</head>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<link  ")
            for key in kwargs:
                f.write("%s='%s' " % (key, kwargs[key]))
            f.write("/>\n")
            f.write(temp)
            map.close()

    def internal_css(self, **kwargs):
        """ This functions adds an internal CSS to the html file. It helps\
            to give unique style to the html page."""

        with open("file", "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("<title>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<style type=\"text/css\" media=\"screen\">\n ")
            for key in kwargs:
                if key == "divwrapper":
                    f.write("div#wrapper %s" % (kwargs[key]))
                else:
                    f.write("%s %s \n" % (key, kwargs[key]))
            f.write("</style>\n")
            f.write(temp)
            map.close()

    def a(self, content, path):
        """ This function creates an a tag. It takes content and path to the \
                file as parameters."""
        with open("file", "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<a href='%s'>%s</a><br />\n" % (path, content))
            f.write(temp)
            map.close()

    def hr(self):
        """ This function simply creates a horizontal bar. It takes no\
            arguments """

        with open("file", "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<hr>\n")
            f.write(temp)
            map.close()

    def printOut(self):
        output = ''
        with open("file", "r") as f:
            html_output = f.readline()
            while html_output:
                output += html_output.lstrip()
                html_output = f.readline()
            f.close()
        return output
