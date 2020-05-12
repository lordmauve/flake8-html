#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the flake8 HTML plugin."""
import codecs
import os.path
import tempfile
import shutil
import contextlib

import pytest
from flake8.main.cli import main


def create_tmpdir(filename, content):
    """Create a temporary directory, plus a file with the given content."""
    tmpdir = tempfile.mkdtemp()
    pyfile = os.path.join(tmpdir, filename)
    with codecs.open(pyfile, 'w', encoding='utf8') as f:
        f.write(content)
    return tmpdir


@pytest.fixture()
def bad_sourcedir(tmpdir_factory):
    """A fixture to create a Python file with errors."""
    tmpdir = create_tmpdir('bad.py', 'import os\n')
    yield tmpdir
    shutil.rmtree(tmpdir)


@pytest.fixture()
def good_sourcedir(tmpdir_factory):
    """A fixture to create a Python file without errors."""
    tmpdir = create_tmpdir('good.py', '"""Example of addition."""\n\n1 + 1\n')
    yield tmpdir
    shutil.rmtree(tmpdir)


@contextlib.contextmanager
def chdir(dest):
    """Chdir into the given directory within a context."""
    cwd = os.getcwd()
    os.chdir(dest)
    try:
        yield
    finally:
        os.chdir(cwd)


def test_report(bad_sourcedir, tmpdir):
    """Test that a report on a bad file creates the expected files."""
    with chdir(bad_sourcedir), pytest.raises(SystemExit) as excinfo:
        main(['--exit-zero', '--format=html', '--htmldir=%s' % tmpdir, '.'])
    assert excinfo.value.code == 0
    names = ('index.html', 'styles.css', 'bad.report.html', 'bad.source.html')
    written = os.listdir(str(tmpdir))
    for n in names:
        assert n in written, "File %s not written" % n
