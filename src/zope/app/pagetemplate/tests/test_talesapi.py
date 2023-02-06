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
"""Tales API Tests
"""


import unittest
from datetime import datetime

from zope.dublincore.interfaces import IZopeDublinCore
from zope.interface import implementer
from zope.size.interfaces import ISized
from zope.traversing.interfaces import IPhysicallyLocatable

from zope.app.pagetemplate.talesapi import ZopeTalesAPI


@implementer(IZopeDublinCore,  # not really, but who's checking. ;)
             IPhysicallyLocatable,  # not really
             ISized)
class TestObject:

    description = "This object stores some number of apples"
    title = "apple cart"
    created = datetime(2000, 10, 1, 23, 11, 00)
    modified = datetime(2003, 1, 2, 3, 4, 5)

    def sizeForSorting(self):
        return 'apples', 5

    def sizeForDisplay(self):
        return '5 apples'

    def getName(self):
        return 'apples'


class TestAPI(unittest.TestCase):

    def test_title(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject.title, api.title)

    def test_description(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject.description, api.description)

    def test_name(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject().getName(), api.name())

    def test_title_or_name(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject.title, api.title_or_name())

        testObject2 = TestObject()
        testObject2.title = ""
        api = ZopeTalesAPI(testObject2)
        self.assertEqual('apples', api.title_or_name())

    def test_size(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject().sizeForDisplay(), api.size())

    def test_modified(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject.modified, api.modified)

    def test_created(self):
        api = ZopeTalesAPI(TestObject())
        self.assertEqual(TestObject.created, api.created)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
