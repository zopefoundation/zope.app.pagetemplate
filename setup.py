##############################################################################
#
# Copyright (c) 2006-2009 Zope Foundation and Contributors.
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
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
from setuptools import setup, find_packages
import os.path

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

version = '4.0.0'


setup(name='zope.app.pagetemplate',
      version=version,
      url='http://github.com/zopefoundation/zope.app.pagetemplate',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='PageTemplate integration for Zope 3',
      long_description=(
        read('README.rst')
        + '\n\n.. contents::\n\n' +
        read('CHANGES.rst')
        ),
      license='ZPL 2.1',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'
      ],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      include_package_data=True,
      install_requires=[
          'setuptools',
          'zope.browserpage>=3.12.0',
          'zope.component [hook]',
          'zope.configuration',
          'zope.dublincore',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.pagetemplate>=3.5.1',
          'zope.schema',
          'zope.security',
          'zope.size',
          'zope.tales',
          'zope.traversing',
          ],
      extras_require={
          "test": [
              'zope.component [hook,test]',
              'zope.container',
              'zope.publisher',
              'zope.testrunner',
              ],
          },
      zip_safe=False,
      )
