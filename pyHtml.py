#!/bin/env python
import string
import mmap
import re
import sys
import os

__doc__ = """This class helps user generate html code from within your python \
        code"""

__doctype__ = "<!DOCTYPE html>"


class pyhtml:
    def __init__(self, title="My Web Page"):
        self.title = title
        #print str(self.title)
        #self.fil = open(self.title, "w+")
        #self.fil.close()
        self.html(self.title)

    def html(self, title):
        """This function generates 4 tags & end tags that are always there\
                in an html file namely <html>, <head>, <title>, <body>"""

        with open(title, "w") as f:
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

        with open(self.title, "r+b") as f:
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

        with open(self.title, "r+b") as f:
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
        with open(self.title, "r+b") as f:
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

        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<hr>\n")
            f.write(temp)
            map.close()

    def br(self):
        """ This function insert a single line break each time it is called.\
            It doesn't take any arguemnts."""
        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<br />")
            f.write(temp)
            map.close()

    def comment(self, comm):
        """ This function adds a comment to the html page and takes one \
            argument which is the comment itself."""
        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.write("<!-- %s -->" % comm)
            f.write(temp)
            map.close()

    def b(self, data):
        """ This function makes the data passed to it appear in bold text.\
            That is it inserts the <b> tag around the data passed to it."""
        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<b>%s</b><br />" % data)
            f.write(temp)
            map.close()

    def i(self, data):
        """ This function makes the data passed to it appear in italics text.\
            That is it inserts the <i> tag around the data passed to it."""
        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<i>%s</i><br />" % data)
            f.write(temp)
            map.close()

    def u(self, data):
        """ This function makes the data passed to it appear in underlined.\
            That is it inserts the <i> tag around the data passed to it."""
        with open(self.title, "r+b") as f:
            map = mmap.mmap(f.fileno(), 0)
            m = re.search("</body>", map)
            start = m.start()
            f.seek(start)
            temp = f.read()
            f.seek(start)
            f.write("<u>%s</u><br />" % data)
            f.write(temp)
            map.close()

    def printOut(self):
        output = ''
        with open(self.title, "r") as f:
            html_output = f.readline()
            while html_output:
                output += html_output.lstrip()
                html_output = f.readline()
            f.close()
        return output

def generate_html(path, parent = None):
    listing = os.listdir(path)
    listing = [l for l in listing if l[0] != '.']
    full_path_listing = []

    for i in listing:
        full_path_listing.append(path + '/' + i)

    title = os.path.abspath(path + "/index.html")
    page = pyhtml(str(title))
    page.internal_css(body="{ width: 500px; margin: 0 auto; }")
    if parent != None:
        page.a("Parent Directory", parent + '/index.html')
    page.b("Directory listing for %s" % os.path.abspath(path))
    page.br()
    page.hr()

    for i in full_path_listing:
        if os.path.isdir(i):
            generate_html(os.path.abspath(i), path)
            page.a(i.split('/')[-1], i + '/index.html')
        else:
            #page.a(listing[i], full_path_listing[i])
            page.a(i.split('/')[-1], i)
            #page.a(full_path_listing[i], 'bogus')

    return page.printOut()

if __name__ == "__main__":
    to_print = generate_html(sys.argv[1])
    print to_print
    #return to_print
