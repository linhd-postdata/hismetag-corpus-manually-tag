"""
Try to read test-corpus files as xml to note and correct syntax errors
"""


__author__ = 'prf'
__date__ = '27/12/17'


import codecs
from lxml import etree
import re
import sys
#from xml.sax.saxutils import escape


ini = '<?xml version="1.0"?><text>'
fin = '</text>'

infn = sys.argv[1]


def myescape(txt):
    """
    Preprocess the HSMS markup so that text can be parsed as XML
    """
    # remove comments
    txt = re.sub(r"(\r?\n).*-->(\r?\n)$", r"\1\2", txt)
    txt = re.sub(r"(\r?\n)<!--.*(\r?\n)", r"\1\2", txt)
    # will give errors if not replace
    txt = txt.replace("<<", "<")
    txt = txt.replace(">>", ">")
    # for xml escaping
    txt = txt.replace("&", "&amp;")
    # escape all brackets not part of a HisMeTag tag
    txt = re.sub(r"<(?!(?:/|persN|addN|roleN|orgN|geogN|placeN|name))([^>]+)>", r"&lt;\1&gt;", txt)
    return txt


# parse as xml: if lxml shows no error messages, file is fine
txt = ini + myescape(codecs.open(infn, "r", "utf8").read()) + fin
tree = etree.fromstring(txt)
print etree.tostring(tree, pretty_print=True, with_tail=True)

