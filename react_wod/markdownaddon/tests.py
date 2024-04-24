from django.test import TestCase
from markdown import markdown
from markdownaddon.extension import LinkExtension
from matrix.models import Document
from unittest.mock import patch

class MarkdownExtensionTestCase(TestCase):

    @patch('matrix.models.Document.objects.get')
    def test_link_conversion(self, mock_get):
        # Setup a mock document object with the necessary attributes
        mock_document = Document()
        mock_document.id = 1
        mock_document.file_name = "ExampleDoc"
        # Configure the mock to return the mock_document when .get() is called
        mock_get.return_value = mock_document

        input_md = 'This is a test for [[ExampleDoc]].'
        expected_html = 'This is a test for <a href="/document/1/">ExampleDoc</a>.'

        # Use the markdown library to convert input_md with your custom extension
        output_html = markdown(input_md, extensions=[LinkExtension()])

        # Assert the output is as expected
        self.assertEqual(output_html, expected_html)
