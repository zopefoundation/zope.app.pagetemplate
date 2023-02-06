"""Test that nested macro references do the right thing.
"""
__docformat__ = "reStructuredText"

import unittest

from zope.browserpage import ViewPageTemplateFile
from zope.component.testing import PlacelessSetup
from zope.publisher.browser import TestRequest


class Context:
    pass


class View:
    def __init__(self, context, request):
        self.context = context
        self.request = request


EXPECTED = """\
<html>
<head>
<title>Example: outer</title>
</head>
<body>
hello
<div>
<div>
inner body slot content
</div>
intermediate body slot stuff
</div>
</body>
</html>
"""


class Test(PlacelessSetup, unittest.TestCase):

    def testMacroExtension(self):
        # This test demonstrates how macro extension allows a macro to extend
        # and re-offer a slot for a client template to fill.
        outer = ViewPageTemplateFile('outer.pt')
        intermediate = ViewPageTemplateFile('intermediate.pt')
        inner = ViewPageTemplateFile('inner.pt')

        context = Context()
        request = TestRequest()
        view = View(context, request)
        self.assertIn('outer body slot', outer(view))

        namespace = inner.pt_getContext(view, request)
        namespace['outer'] = outer
        namespace['intermediate'] = intermediate
        result = inner.pt_render(namespace)
        self.assertEqual(result.replace("\r\n", "\n"), EXPECTED)


def test_suite():
    loader = unittest.TestLoader()
    return loader.loadTestsFromTestCase(Test)
