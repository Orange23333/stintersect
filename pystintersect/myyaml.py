# -*- coding: UTF-8 -*-

# https://pyyaml.org/wiki/PyYAMLDocumentation

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
