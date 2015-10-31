#!/usr/bin/python
# coding: utf-8

#  _ __ _  _ __ _ ___ __ _ _ _
# | '_ \ || / _` / -_) _` | '_|
# | .__/\_, \__, \___\__,_|_|
# |_|   |__/|___/
#
# The python gear generator

__version__ = (0, 24, 0, 'alpha', 0)
__author__ = 'Guillaume Florent (florentsailing@gmail.com)'
__license__ = 'GPL v2'

get_version = lambda: __import__('pygear.utils.version', fromlist=['get_version']).get_version(__version__)
