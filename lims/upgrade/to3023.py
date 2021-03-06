from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent
from dependencies.dependency import getToolByName
from dependencies.dependency import REFERENCE_CATALOG
from lims.permissions import AddStorageLocation

def upgrade(tool):
    """ Add Storage locacations to ARs and Samples.
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
    setup.runImportStepFromProfile('profile-bika.lims:default', 'propertiestool')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'factorytool')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'controlpanel')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'cssregistry')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'content')

    setup.runImportStepFromProfile('profile-bika.lims:default', 'workflow')
    setup.runImportStepFromProfile('profile-bika.lims:default', 'workflow-csv')

    wf = getToolByName(portal, 'portal_workflow')
    wf.updateRoleMappings()

    mp = portal.manage_permission
    mp(AddStorageLocation, ['Manager', 'Owner', 'LabManager', ], 1)

    at = getToolByName(portal, 'archetype_tool')
    at.setCatalogsByType('StorageLocation', ['bika_setup_catalog', 'portal_catalog'])

    bika_setup = portal._getOb('bika_setup')
    obj = bika_setup._getOb('bika_storagelocations')
    obj.unmarkCreationFlag()
    obj.reindexObject()
