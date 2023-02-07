##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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
"""Binding Tests

$Id$
"""
import unittest

from zope.component import provideAdapter
from zope.component.testing import PlacelessSetup
from zope.container.interfaces import ISimpleReadContainer
from zope.container.traversal import ContainerTraversable
from zope.traversing.interfaces import ITraversable

from zope.app.pagetemplate.tests.testpackage.content import Content
from zope.app.pagetemplate.tests.testpackage.content import PTComponent


def setUpTraversal():
    from zope.traversing.testing import setUp
    setUp()
    provideAdapter(ContainerTraversable, (ISimpleReadContainer,), ITraversable)


class BindingTestCase(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super().setUp()
        setUpTraversal()

    def test_binding(self):
        from zope.publisher.browser import TestRequest
        comp = PTComponent(Content(), TestRequest())
        self.assertEqual(comp.index().replace("\r\n", "\n"), "42\n")
        self.assertEqual(comp.nothing().replace("\r\n", "\n"), "\n")
        self.assertEqual(comp.default().replace("\r\n", "\n"), "42\n")


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromTestCase(BindingTestCase)
