##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
See ViewPageTemplateFile

$Id$
"""
__metaclass__ = type # All classes are new style when run with Python 2.2+

from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.component import getView
from zope.app.pagetemplate.engine import AppPT

class ViewPageTemplateFile(AppPT, PageTemplateFile):
    """Page Templates used as methods of views defined as Python classes.
    """

    def __init__(self, filename, _prefix=None, content_type=None):
        _prefix = self.get_path_from_prefix(_prefix)
        super(ViewPageTemplateFile, self).__init__(filename, _prefix)
        if content_type is not None:
            self.content_type = content_type

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
            instance=instance, args=args, options=keywords)
        debug_flags = instance.request.debug
        return self.pt_render(namespace, showtal=debug_flags.showTAL,
                              sourceAnnotations=debug_flags.sourceAnnotations)

    def __get__(self, instance, type):
        return BoundPageTemplate(self, instance)

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

    macros = property(lambda self: self.im_func.macros)
    filename = property(lambda self: self.im_func.filename)

    def __call__(self, *args, **kw):
        if self.im_self is None:
            im_self, args = args[0], args[1:]
        else:
            im_self = self.im_self
        return self.im_func(im_self, *args, **kw)

    def __setattr__(self, name, v):
        raise AttributeError("Can't set attribute", name)

    def __repr__(self):
        return "<BoundPageTemplateFile of %r>" % self.im_self

