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
See ViewPageTemplateFile

$Id%
"""
__metaclass__ = type # All classes are new style when run with Python 2.2+

from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.component import getView
from zope.app.pagetemplate.engine import AppPT

class ViewPageTemplateFile(AppPT, PageTemplateFile):
    """Page Templates used as methods of views defined as Python classes.
    """

    def pt_getContext(self, instance, request, **_kw):
        # instance is a View component
        namespace = super(ViewPageTemplateFile, self).pt_getContext(**_kw)
        namespace['request'] = request
        namespace['view'] = instance
        namespace['context'] = context = instance.context
        namespace['views'] = ViewMapper(context, request)
        return namespace

    def __call__(self, instance, *args, **keywords):
        namespace = self.pt_getContext(
            request=instance.request,
            instance=instance,
            args=args, options=keywords)
        return self.pt_render(namespace)

    def __get__(self, instance, type=None):
        return BoundPageTemplate(self, instance)

    # Instances of this class are pretending to be methods.
    # In general, they need to be ContextMethods.
    __Zope_ContextWrapper_contextful_get__ = True

class ViewMapper:
    def __init__(self, ob, request):
        self.ob = ob
        self.request = request

    def __getitem__(self, name):
        return getView(self.ob, name, self.request)


class BoundPageTemplate:
    def __init__(self, pt, ob):
        object.__setattr__(self, 'im_func', pt)
        object.__setattr__(self, 'im_self', ob)

    def __call__(self, REQUEST=None, **kw):
        return self.im_func(self.im_self, REQUEST, **kw)

    def __getattr__(self, name):
        return getattr(self.im_func, name)

    def __setattr__(self, name, v):
        raise AttributeError("Can't set attribute", name)

    def __repr__(self):
        return "<BoundPageTemplateFile of %r>" % self.im_self