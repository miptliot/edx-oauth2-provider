"""
Util methods for testing.
"""


import os.path
import urllib.parse


def normpath(url):
    """Get the normalized path of a URL"""
    return os.path.normpath(urllib.parse.urlparse(url).path)
