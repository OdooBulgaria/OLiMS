from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from dependencies.dependency import getToolByName
from lims.permissions import *
from lims.setuphandlers import BikaGenerator
from lims import logger

def upgrade(tool):
    """  stickers
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup

    setup.runImportStepFromProfile('profile-bika.lims:default', 'typeinfo')

    prt = portal.bika_setup.AutoPrintLabels
    portal.bika_setup.setAutoPrintStickers(prt)

    size = portal.bika_setup.AutoLabelSize
    portal.bika_setup.setAutoStickerTemplate('bika.lims:sticker_%s.pt' %size)

    return True
