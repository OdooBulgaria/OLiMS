from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from lims.permissions import *


def upgrade(tool):
    """Added bika.lims.loader.js and bika.lims.artemplate.edit.js
    Also fix LIMS-1352 (would have been 3042, but metadata.xml is not up to date!).
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup

    # update affected tools
    setup.runImportStepFromProfile('profile-bika.lims:default', 'jsregistry')

    # LIMS-1352
    proxies = portal.bika_catalog(portal_type='Sample')
    for brain in proxies:
        sample = brain.getObject()
        sample.setSamplingWorkflowEnabled(sample.getSamplingWorkflowEnabledDefault())

    return True
