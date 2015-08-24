from OLiMS.dependencies.dependency import aq_inner
from OLiMS.dependencies.dependency import aq_parent
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.permissions import *
from OLiMS.lims.setuphandlers import BikaGenerator
from OLiMS.lims import logger

def upgrade(tool):
    """Add the bika-frontpage view to the selectable views.  This will not
    set the default, but all new sites will have the 'properties.xml' loaded,
    which does set the default.
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from OLiMS.lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup
    setup.runImportStepFromProfile('profile-bika.lims:default', 'typeinfo')

    return True
