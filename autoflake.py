#!/usr/bin/env python
"""Run flake8-html with a livereload server."""
import shlex
import shutil
import tempfile
import subprocess
from livereload import Server


TMPDIR = tempfile.mkdtemp()

cmd = shlex.split('flake8 --format=html --htmldir=%s --exit-zero' % TMPDIR)


def run_flake8():
    """Run flake8."""
    subprocess.check_call(cmd)


run_flake8()
server = Server()
server.watch('flake8_html/', run_flake8)
server.watch('tests/', run_flake8)
try:
    server.serve(root=TMPDIR, open_url_delay=2)
finally:
    shutil.rmtree(TMPDIR)
