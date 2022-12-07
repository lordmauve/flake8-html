# -*- coding: utf-8 -*-
"""flake8-html - a flake8 plugin to generate HTML reports."""

__author__ = """Daniel Pope"""
__email__ = 'mauve@mauveweb.co.uk'
__version__ = '0.4.3'


from .plugin import HTMLPlugin, find_severity

__all__ = (
    'HTMLPlugin', 'find_severity'
)
