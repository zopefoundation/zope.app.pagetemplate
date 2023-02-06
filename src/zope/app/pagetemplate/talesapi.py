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
"""Implementation of the Zope TALES API

$Id$
"""

__docformat__ = 'restructuredtext'

from zope.dublincore.interfaces import IDCDescriptiveProperties
from zope.dublincore.interfaces import IDCTimes
from zope.dublincore.interfaces import IZopeDublinCore
from zope.interface import implementer
from zope.security.interfaces import Unauthorized
from zope.size.interfaces import ISized
from zope.tales.interfaces import ITALESFunctionNamespace
from zope.traversing.api import getName


@implementer(IDCTimes,
             IDCDescriptiveProperties,
             ITALESFunctionNamespace)
class ZopeTalesAPI:

    def __init__(self, context):
        self.context = context

    def setEngine(self, engine):
        self._engine = engine

    @property
    def title(self):
        a = IZopeDublinCore(self.context, None)
        if a is None:
            raise AttributeError('title')
        return a.title

    @property
    def description(self):
        a = IZopeDublinCore(self.context, None)
        if a is None:
            raise AttributeError('description')
        return a.description

    @property
    def created(self):
        a = IZopeDublinCore(self.context, None)
        if a is None:
            raise AttributeError('created')
        return a.created

    @property
    def modified(self):
        a = IZopeDublinCore(self.context, None)
        if a is None:
            raise AttributeError('modified')
        return a.modified

    def name(self):
        return getName(self.context)

    def title_or_name(self):
        try:
            return getattr(self, 'title', '') or getName(self.context)
        except Unauthorized:
            return getName(self.context)

    def size(self):
        a = ISized(self.context, None)
        if a is None:
            raise AttributeError('size')
        return a.sizeForDisplay()
