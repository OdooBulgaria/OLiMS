from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from lims import logger
from lims.permissions import *
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from dependencies.dependency import BadRequest


def upgrade(tool):
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    portal_catalog = getToolByName(portal, 'portal_catalog')

    proxies = portal_catalog(portal_type="AnalysisRequest")
    ars = [proxy.getObject() for proxy in proxies]
    for ar in ars:
        if not ar.getPriority():
            ar.setDefaultPriority()


    return True
