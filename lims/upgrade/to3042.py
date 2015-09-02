from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from lims.permissions import *


def upgrade(tool):
    """Added bika.lims.client.view.js
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup

    # reread jsregistry with the new data
    setup.runImportStepFromProfile('profile-bika.lims:default', 'jsregistry')

    return True
