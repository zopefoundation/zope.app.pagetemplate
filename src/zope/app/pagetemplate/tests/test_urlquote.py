##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""URLQuote Tests

I kept the tests quite small, just covering that the functions actually do
something (and don't really scramble stuff). We are relying on the python
urllib to be functional to avoid test duplication.

"""

import unittest
from doctest import DocTestSuite

from zope.app.pagetemplate.urlquote import URLQuote


class TestObject:

    def __str__(self):
        return "www.google.de"


class TestQuote(unittest.TestCase):

    def test_quote_simple(self):
        q = URLQuote("www.google.de")
        self.assertEqual('www.google.de', q.quote())
        self.assertEqual('www.google.de', q.unquote())
        self.assertEqual('www.google.de', q.quote_plus())
        self.assertEqual('www.google.de', q.unquote_plus())

    def test_quote_cast_needed(self):
        q = URLQuote(TestObject())
        self.assertEqual('www.google.de', q.quote())
        self.assertEqual('www.google.de', q.unquote())
        self.assertEqual('www.google.de', q.quote_plus())
        self.assertEqual('www.google.de', q.unquote_plus())


def test_suite():
    return unittest.TestSuite((
        unittest.defaultTestLoader.loadTestsFromTestCase(TestQuote),
        DocTestSuite('zope.app.pagetemplate.urlquote'),
    ))
