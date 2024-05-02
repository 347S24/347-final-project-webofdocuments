from markdown import Markdown
from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
from django.urls import reverse
from matrix.models import Document

# This regex is taken straight from this stack overflow post
# This is the regex that captures the link to another file
# https://stackoverflow.com/questions/24040965/regular-expression-double-brackets-text
LINK_PATTERN = r"(?<=\[\[)([^\[\]]*)(?=\]\])"

class LinkPattern(Pattern):
    """Define a LinkPattern class to use our LINK_PATTERN regular experssion."""
    def handleMatch(self, m):
        file_name = m.group(2).strip() # group(2) is the first group captured from the regex

        url = self.transform_file_to_url(file_name) # link to other file w/in db

        # TODO gracefully handle with try/except 
        if url is None:
            return None

        el = etree.Element("a") # <a>
        el.set("href", url)
        el.text = file_name
        return el

    def transform_file_to_url(self, file_name):
        try:
            # try to find the document via file name
            doc = Document.objects.get(file_name=file_name)
            return reverse("document_detail", args=[doc.pk])
        except Document.DoesNotExist:
            return None

class LinkExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        link_pattern = LinkPattern(LINK_PATTERN, md)
        # TODO check if priority level is correct
        md.inlinePatterns.register(link_pattern, "link_extra", 175)