=======
Changes
=======

5.1 (unreleased)
----------------

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


5.0 (2023-02-07)
----------------

- Drop support for Python 2.7, 3.4, 3.5, 3.6.

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.


4.0.0 (2017-04-22)
------------------

- Add support for Python 3 and PyPy.
- Do not explicitly require ``zope.security [untrustedpython]``. Older
  ``zope.pagetemplate`` versions require it, newer ones do not.

3.11.2 (2010-09-25)
-------------------

- Declared test dependency on ``zope.component [test]`` as it is needed to
  run the tests.

3.11.1 (2010-09-01)
-------------------

- Added metaconfigure.registerType BBB import because some packages use it.
- Using doctest from standard library instead of `zope.testing.doctest`.

3.11.0 (2010-04-26)
-------------------

- Moved tales:expressiontype directive down into zope.browserpage.

3.10.1 (2010-01-04)
-------------------

- Fixed the `zope.browserpage` imports in the ``namedtemplate`` module.

3.10.0 (2009-12-22)
-------------------

- Moved named template implementation to zope.browserpage.

3.9.0 (2009-12-22)
------------------

- Moved viewpagetemplatefile, simpleviewclass and metaconfigure.registerType
  into the zope.browserpage package, reversing the dependency.

3.8.0 (2009-12-16)
------------------

- Refactored nested macro test from a functional test into a unit test. This
  allowed to remove the last outside zope.app dependencies.

- Fixed undeclared testing dependency on zope.app.component.

- Copy trivial NoTraverser class from zope.app.publication to avoid a ZCML
  dependency on that package.

- Correct testing dependency to point to zope.securitypolicy instead of its
  zope.app variant. The app version is no longer required since 3.4.1.

- Removed the ``inline-evaluation`` extra referring to zope.app.interpreter.
  There's no code or ZCML left pointing to that package.

3.7.1 (2009-05-27)
------------------

- Restored ``zope.app.pagetemplate.engine`` module, using BBB imports from
  ``zope.pagetemplate.engine``.

3.7.0 (2009-05-25)
------------------

- Moved the ``engine`` module and associated testing machinery to
  ``zope.pagetemplate`` (version 3.5.0).

3.6.0 (2009-05-18)
------------------

* Moved ``namedtemplate.*`` from ``zope.formlib`` here as it is more
  about a page template engine than a formular library. This also
  breaks some dependencies on ``zope.formlib``.

* Added doctests to long_description to show up on pypi.

3.5.0 (2009-02-01)
------------------

* Use ``zope.container`` instead of ``zope.app.container``.

3.4.1 (2008-07-30)
------------------

* Substitute zope.app.zapi by direct calls to its wrapped apis.
  See http://launchpad.net/bugs/219302

* Fix deprecation warning in ftesting.zcml: ZopeSecurityPolicy now lives in
  zope.securitypolicy.

3.4.0 (2007-09-28)
------------------

* Initial release as standalone package.

* Dependency on zope.app.interpreter moved to an extra
  [inline-evaluation].  It is only needed by zope.app.pythonpage,
  which is an oddity.
