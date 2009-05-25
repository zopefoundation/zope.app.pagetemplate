##############################################################################
#
# Copyright (c) 2005-2009 Zope Corporation and Contributors.
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

$Id$
"""
import os
import os.path
import zope.component.testing
import zope.traversing.adapters


def pageSetUp(test):
    zope.component.testing.setUp(test)
    zope.component.provideAdapter(
        zope.traversing.adapters.DefaultTraversable,
        [None],
        )


def test_suite():
    from zope.testing import doctest
    return doctest.DocFileSuite(
        os.path.join(os.pardir, 'namedtemplate.txt'),
        setUp=pageSetUp, tearDown=zope.component.testing.tearDown,
        )
