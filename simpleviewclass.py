##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: simpleviewclass.py,v 1.9 2003/06/06 20:44:31 stevea Exp $
"""

import sys
from zope.publisher.browser import BrowserView
from zope.publisher.interfaces.browser import IBrowserPublisher
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.context import ContextMethod
from zope.publisher.interfaces import NotFound
from zope.interface import implements

class simple(BrowserView):

    implements(IBrowserPublisher)

    def browserDefault(self, request):
        return self, ()
    browserDefault = ContextMethod(browserDefault)

    def publishTraverse(self, request, name):
        if name == 'index.html':
            return self.index

        raise NotFound(self, name, request)
    publishTraverse = ContextMethod(publishTraverse)

    # XXX: we need some unittests for this !!!
    def __getitem__(self, name):
        return self.index.macros[name]

    def __call__(self, template_usage=u'', *args, **kw):
        return self.index(template_usage, *args, **kw)
    __call__ = ContextMethod(__call__)

def SimpleViewClass(src, offering=None, used_for=None, bases=(), usage=u''):
    if offering is None:
        offering = sys._getframe(1).f_globals

    bases += (simple, )

    class_ = type("SimpleViewClass from %s" % src, bases,
                  {'index': ViewPageTemplateFile(src, offering, usage)})

    if used_for is not None:
        class_.__used_for__ = used_for

    return class_
