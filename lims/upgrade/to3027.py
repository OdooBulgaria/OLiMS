from OLiMS.dependencies.dependency import aq_inner
from OLiMS.dependencies.dependency import aq_parent


def upgrade(tool):
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from OLiMS.lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))

    portal.portal_actions.portal_tabs.queries.visible = False

    return True