============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/GRG-Projects/grg-sphinx-theme/issues.

If you are reporting a bug, please include:

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

GRG-Sphinx-Theme could always use more documentation, whether
as part of the official GRG-Sphinx-Theme docs, in docstrings,
or even on the web in blog posts, articles, and such.
GRG-Sphinx-Theme uses `Sphinx <http://www.sphinx-doc.org/en/stable/index.html) to generate documentation>`_.
Please follow the `numpy coding style <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_ and `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_
for docstring documentation.



Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/GRG-Projects/grg-sphinx-theme/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `GRG-Sphinx-Theme` for local development.

1. Fork the `GRG-Sphinx-Theme` repo on GitHub.
2. Clone your fork locally::

    $ git clone https://github.com/your_name_here/grg-sphinx-theme.git

3. Add a tracking branch which can always have the last version of `grg-sphinx-theme`::

    $ git remote add upstream https://github.com/GRG-Projects/grg-sphinx-theme.git
    $ git fetch upstream
    $ git branch upstream-master --track upstream/master
    $ git checkout upstream-master
    $ git pull

4. Create a branch from the last dev version of your tracking branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

5. Install it locally::

    $ pip install --user -e .

6. Now you can make your changes locally::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Install the required packages for running the unittests::

    $ pip install -e .

8. When you're done making changes, check that your changes pass flake8 and pytest::

    $ flake8 grg_sphinx_theme
    $ pytest -svv grg_sphinx_theme

   To get flake8 and pytest, just pip install them into your virtualenv.

9. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.8, 3.9, 3.10, 3.11 and for PyPy. Check
   https://github.com/GRG-Projects/grg-sphinx-theme/actions
   and make sure that the tests pass for all supported Python versions.

Publishing Releases
--------------------

Checklist before Releasing
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Review the open list of `grg-sphinx-theme issues <https://github.com/GRG-Projects/grg-sphinx-theme/issues>`_.  Check whether there are
  outstanding issues that can be closed, and whether there are any issues that
  should delay the release.  Label them !

* Check whether there are no build failing on `Travis`.

* Review and update the release notes. Get a partial list of contributors with something like::

      git shortlog -nse v0.1.0..

  where ``v0.1.0`` was the last release tag name.

  Then manually go over ``git shortlog v0.1.0..`` to make sure the release notes
  are as complete as possible and that every contributor was recognized.

* Use the opportunity to update the ``.mailmap`` file if there are any duplicate
  authors listed from ``git shortlog -ns``.

* Add any new authors to the ``AUTHORS`` file.

* Check the copyright years in ``LICENSE``

* The release should now be ready.

Doing the release
~~~~~~~~~~~~~~~~~


* Type git status and check that you are on the master branch with no uncommitted code.

* Now it's time for the source release. Mark the release with an empty commit, just to leave a marker.
  It makes it easier to find the release when skimming through the git history::

    git commit --allow-empty -m "REL: vX.Y.Z"

* Tag the commit::

    git tag -am 'Second public release' vX.Y.Z  # Don't forget the leading v

  This will create a tag named vX.Y.Z. The -a flag (strongly recommended) opens up a text editor where
  you should enter a brief description of the release.

* Verify that the __version__ attribute is correctly updated::

    import grg_sphinx_theme
    grg_sphinx_theme.__version__  # should be 'X.Y.Z'

  Incidentally, once you resume development and add the first commit after this tag, __version__ will take
  on a value like X.Y.Z+1.g58ad5f7, where +1 means “1 commit past version X.Y.Z” and 58ad5f7 is the
  first 7 characters of the hash of the current commit. The letter g stands for “git”. This is all managed
  automatically by versioneer and in accordance with the specification in PEP 440.

* Push the new commit and the tag to master::

    git push origin master
    git push origin vX.Y.Z

* Github Action should care of uploading packages to PyPI as soon as you push the tag

* Check how everything looks on pypi - the description, the packages.  If
  necessary delete the release and try again if it doesn't look right.


Other stuff that needs doing for the release
============================================

* Announce to the mailing lists.  With fear and trembling.