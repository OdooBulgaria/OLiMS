from OLiMS.dependencies.dependency import aq_inner
from OLiMS.dependencies.dependency import aq_parent
from OLiMS.lims.permissions import *


def upgrade(tool):
    """ JS structure refactoring
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from OLiMS.lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup

    setup.runImportStepFromProfile('profile-bika.lims:default', 'jsregistry')

    return True