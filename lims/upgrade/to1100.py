import logging

from dependencies.dependency import aq_base
from dependencies.dependency import aq_inner
from dependencies.dependency import aq_parent

from dependencies.dependency import permissions
from lims.permissions import *

from dependencies.dependency import getToolByName


def upgrade(tool):
    """
    """
    # Hack prevent out-of-date upgrading
    # Related: PR #1484
    # https://github.com/bikalabs/Bika-LIMS/pull/1484
    from lims.upgrade import skip_pre315
    if skip_pre315(aq_parent(aq_inner(tool))):
        return True

    portal = aq_parent(aq_inner(tool))
    portal_catalog = getToolByName(portal, 'portal_catalog')
    typestool = getToolByName(portal, 'portal_types')
    workflowtool = getToolByName(portal, 'portal_workflow')
    setup = portal.portal_setup

    # Changes to the catalogs
    at = getToolByName(portal, 'archetype_tool')
    at.setCatalogsByType('Batch', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('AnalysisRequest', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('Sample', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('SamplePartition', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('ReferenceSample', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('Report', ['bika_catalog', 'portal_catalog'])
    at.setCatalogsByType('Worksheet', ['bika_catalog', 'portal_catalog'])

    at.setCatalogsByType('AnalysisService', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('SampleType', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('SamplePoint', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('Instrument', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('Method', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('Calculation', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('AnalysisProfile', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('ARTemplate', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('LabProduct', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('LabContact', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('ReferenceManufacturer', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('ReferenceSupplier', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('ReferenceDefinition', ['bika_setup_catalog', 'portal_catalog'])
    at.setCatalogsByType('WorksheetTemplate', ['bika_setup_catalog', 'portal_catalog'])

    portal_catalog.clearFindAndRebuild()

    return True
