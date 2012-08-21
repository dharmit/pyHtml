#!/bin/env python

from pyHtml import pyhtml
import os
import sys

if __name__ == "__main__":
    listing = os.listdir(sys.argv[1])
    listing = [l for l in listing if l[0] != '.' ]
    realpath = os.path.realpath(sys.argv[1]) + '/'
    full_path_listing = []

    for i in range(0, len(listing)):
        full_path_listing.append(realpath + listing[i])

    title = os.path.abspath(sys.argv[1]) + "/listing_%s" \
            % sys.argv[1].split('/')[-1]
    page = pyhtml(str(title))
    page.internal_css(body="{ width: 500px; margin: 0 auto; }")
    for i in range(0, 5):
        page.br()
    page.comment("Comment is here")

    page.hr()

    for i in range(0, len(listing)):
        page.a(listing[i], full_path_listing[i])

    print page.printOut()
    os.remove(title)
