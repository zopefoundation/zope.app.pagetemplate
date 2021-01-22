##############################################################################
#
# Copyright (c) 2017 Zope Foundation and Contributors.
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
"""
Tests for deprecated/backwards-compatibility imports.
"""


import unittest


class TestBWC(unittest.TestCase):

    def test_viewpagetemplatefile(self):
        from zope.app.pagetemplate import viewpagetemplatefile
        self.assertIsNotNone(viewpagetemplatefile.ViewPageTemplateFile)

    def test_i18n(self):
        from zope.app.pagetemplate import i18n
        self.assertIsNotNone(i18n.ZopeMessageFactory)

    def test_metaconfigure(self):
        from zope.app.pagetemplate import metaconfigure
        self.assertIsNotNone(metaconfigure.clear)

    def test_simpleviewclass(self):
        from zope.app.pagetemplate import simpleviewclass
        self.assertIsNotNone(simpleviewclass.simple)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
