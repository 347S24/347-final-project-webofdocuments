"""
    Name: Ahron Pollak

    An extension to the markdown extension which is based on the following tutorial: 
    https://github.com/Python-Markdown/markdown/wiki/Tutorial-1---Writing-Extensions-for-Python-Markdown
    The goal of this extension is to add the ability to link other files using [[]], which is done by adding to the markdown parser.
"""


from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


# https://stackoverflow.com/questions/24040965/regular-expression-double-brackets-text
LINK_PATTERN = r"(?<=\[\[)([^\[\]]*)(?=\]\])"


class LinkPattern(Pattern):
    def handleMatch(self, m):
        # capture the matched text inside the double bracket [[]] (and remove whitespace)
        file_name = m.group(2).strip()
        # convert the file into a url or db reference
        # TODO: implement
        url = self.transform_file_to_url(file_name)
        # create the element
        el = etree.Element("a")
        el.set("href", url)  # transform the text into a link
        el.text = url
        return el

    def transform_file_to_url(self, file_name):
        # TODO: implement
        # This function should convert some file name to its url
        # The url can be an entry in our db or an actual url
        return f"http://doesnotexistyet.com/{file_name}.html"


class LinkExtension(Extension):
    def extendMarkdown(self, md):
        link = LinkPattern(LINK_PATTERN)
        # not sure if this priority is correct
        md.inlinePatterns.register(link, "link_extra", 175)
