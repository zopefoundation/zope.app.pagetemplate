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
"""URL quoting for ZPT
"""

__docformat__ = 'restructuredtext'

import six
from six.moves import urllib_parse as urllib

from zope.interface import implementer
from zope.traversing.interfaces import IPathAdapter
from zope.app.pagetemplate.interfaces import IURLQuote

def _safe_as_text(s):
    if isinstance(s, six.text_type):
        return s

    try:
        return six.text_type(s, 'utf-8')
    except UnicodeDecodeError:
        return s

@implementer(IPathAdapter, IURLQuote)
class URLQuote(object):
    r"""An adapter for URL quoting.

    It quotes unicode strings according to the recommendation in RFC 2718.
    Before the unicode string gets quoted, it gets encoded with UTF-8.

        >>> quoter = URLQuote(u'Roki\u0161kis')
        >>> quoter.quote()
        'Roki%C5%A1kis'

        >>> quoter.quote_plus()
        'Roki%C5%A1kis'

    And when unquoting, it assumes the unquoted string is encoded with
    UTF-8, and tries to convert it to unicode.

        >>> quoter = URLQuote('Roki%C5%A1kis')
        >>> isinstance(quoter.unquote(), six.text_type)
        True

        >>> isinstance(quoter.unquote_plus(), six.text_type)
        True

    If the unquoted string can't be converted to unicode, the unquoted
    string is returned. On Python 2, this will be a byte str, but under Python 3,
    the returned string is always going to be unicode.

        >>> quoter = URLQuote('S%F6derk%F6ping')
        >>> isinstance(quoter.unquote(), str)
        True

        >>> isinstance(quoter.unquote_plus(), str)
        True
    """


    def __init__(self, context):
        if not isinstance(context, six.string_types):
            context = str(context)
        elif six.PY2 and isinstance(context, six.text_type):
            context = context.encode('utf-8')
        self.context = context

    def quote(self):
        """Return the object's URL quote representation."""
        return urllib.quote(self.context)

    def quote_plus(self):
        """Return the object's URL quote_plus representation."""
        return urllib.quote_plus(self.context)

    def unquote(self):
        """Return the object's URL unquote representation."""
        return _safe_as_text(urllib.unquote(self.context))

    def unquote_plus(self):
        """Return the object's URL unquote_plus representation."""
        return _safe_as_text(urllib.unquote_plus(self.context))
