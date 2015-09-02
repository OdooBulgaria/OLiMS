import logging

from dependencies.dependency import aq_base
from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent

from dependencies.dependency import permissions
from lims.permissions import *

from dependencies.dependency import getToolByName


def upgrade(tool):
    """
    issue #615: missing configuration for some add permissions
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))

    # batch permission defaults
    mp = portal.manage_permission
    mp(AddAnalysisSpec, ['Manager', 'Owner', 'LabManager', 'LabClerk'], 1)
    mp(AddSamplingDeviation, ['Manager', 'Owner', 'LabManager', 'LabClerk'], 1)
    mp(AddSampleMatrix, ['Manager', 'Owner', 'LabManager', 'LabClerk'], 1)
    portal.reindexObject()

    return True
