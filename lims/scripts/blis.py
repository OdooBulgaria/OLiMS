"""
Usage:
bin/zopectl run blis.py <ploneSiteId>
"""

from sys import argv
from dependencies import transaction

plone = app[argv[1]]



transaction.commit()
