from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from lims.permissions import *
from dependencies.dependency import BaseContent
from lims.upgrade import stub


def upgrade(tool):
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    setup = portal.portal_setup

    setup.runImportStepFromProfile('profile-bika.lims:default', 'typeinfo')

    stub('bika.lims.content.pricelistlineitem', 'PricelistLineItem',
        BaseContent)
    for pl in portal['pricelists'].objectValues():
        pl.pricelist_lineitems = []
        for pli in pl.objectValues():
            item = dict(
                title=pli.title,
                ItemDescription=pli.ItemDescription,
                Accredited=pli.Accredited,
                Subtotal="%d.%d" % (pli.Subtotal[0], pli.Subtotal[1]),
                VATAmount="%d.%d" % (pli.VATAmount[0], pli.VATAmount[1]),
                Total="%d.%d" % (pli.Total[0], pli.Total[1]),
                CategoryTitle=pli.CategoryTitle,
            )
            pl.pricelist_lineitems.append(item)
    return True
