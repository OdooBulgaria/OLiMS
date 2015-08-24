import warnings
import pkg_resources
__version__ = pkg_resources.get_distribution("bika.lims").version

# import this to create messages in the bika domain.
from dependencies.dependency import MessageFactory
bikaMessageFactory = MessageFactory('bika')
from dependencies.dependency import PloneMessageFactory as PMF

# import this to log messages
import logging
logger = logging.getLogger('Bika')

from bika.lims.validators import *
from bika.lims.config import *
from bika.lims.permissions import *

from dependencies.dependency import ModuleSecurityInfo, allow_module
from dependencies.dependency import process_types, listTypes
from dependencies.dependency import utils
from dependencies.dependency import registerDirectory
from dependencies.dependency import ContentInit, ToolInit, getToolByName
from dependencies.dependency import PloneMessageFactory
from dependencies.dependency import IPloneSiteRoot
from dependencies.dependency import EXTENSION, profile_registry

allow_module('AccessControl')
allow_module('bika.lims')
allow_module('bika.lims.config')
allow_module('bika.lims.permissions')
allow_module('bika.lims.utils')
allow_module('json')
allow_module('pdb')
allow_module('zope.i18n.locales')
allow_module('zope.component')
allow_module('plone.registry.interfaces')

def initialize(context):

    from dependencies.dependency import Analysis
    from dependencies.dependency import AnalysisCategory
    from dependencies.dependency import AnalysisRequest
    from dependencies.dependency import AnalysisRequestsFolder
    from dependencies.dependency import AnalysisService
    from dependencies.dependency import AnalysisSpec
    from dependencies.dependency import ARImport
    from dependencies.dependency import ARImportItem
    from dependencies.dependency import ARPriority
    from dependencies.dependency import AnalysisProfile
    from dependencies.dependency import ARReport
    from dependencies.dependency import ARTemplate
    from dependencies.dependency import Attachment
    from dependencies.dependency import AttachmentType
    from dependencies.dependency import Batch
    from dependencies.dependency import BatchFolder
    from dependencies.dependency import BatchLabel
    from dependencies.dependency import BikaSchema
    from dependencies.dependency import BikaSetup
    from dependencies.dependency import Calculation
    from dependencies.dependency import Client
    from dependencies.dependency import ClientFolder
    from dependencies.dependency import Contact
    from dependencies.dependency import Container
    from dependencies.dependency import ContainerType
    from dependencies.dependency import Department
    from dependencies.dependency import DuplicateAnalysis
    from dependencies.dependency import Instrument
    from dependencies.dependency import InstrumentCalibration
    from dependencies.dependency import InstrumentCertification
    from dependencies.dependency import InstrumentMaintenanceTask
    from dependencies.dependency import InstrumentScheduledTask
    from dependencies.dependency import InstrumentValidation
    from dependencies.dependency import InstrumentType
    from dependencies.dependency import Invoice
    from dependencies.dependency import InvoiceBatch
    from dependencies.dependency import InvoiceFolder
    from dependencies.dependency import LabContact
    from dependencies.dependency import Laboratory
    from dependencies.dependency import LabProduct
    from dependencies.dependency import Manufacturer
    from dependencies.dependency import Method
    from dependencies.dependency import Methods
    from dependencies.dependency import Multifile
    from dependencies.dependency import Organisation
    from dependencies.dependency import Person
    from dependencies.dependency import Preservation
    from dependencies.dependency import Pricelist
    from dependencies.dependency import PricelistFolder
    from dependencies.dependency import QueryFolder
    from dependencies.dependency import Query
    from dependencies.dependency import ReferenceAnalysis
    from dependencies.dependency import ReferenceDefinition
    from dependencies.dependency import ReferenceSample
    from dependencies.dependency import ReferenceSamplesFolder
    from dependencies.dependency import RejectAnalysis
    from dependencies.dependency import Report
    from dependencies.dependency import ReportFolder
    from dependencies.dependency import Sample
    from dependencies.dependency import SampleCondition
    from dependencies.dependency import SampleMatrix
    from dependencies.dependency import SamplePartition
    from dependencies.dependency import SamplePoint
    from dependencies.dependency import StorageLocation
    from dependencies.dependency import SamplesFolder
    from dependencies.dependency import SampleType
    from dependencies.dependency import SamplingDeviation
    from dependencies.dependency import SRTemplate
    from dependencies.dependency import SubGroup
    from dependencies.dependency import Supplier
    from dependencies.dependency import SupplierContact
    from dependencies.dependency import SupplyOrderFolder
    from dependencies.dependency import SupplyOrder
    from dependencies.dependency import Worksheet
    from dependencies.dependency import WorksheetFolder
    from dependencies.dependency import WorksheetTemplate

    from dependencies.dependency import AnalysisCategories
    from dependencies.dependency import AnalysisServices
    from dependencies.dependency import AnalysisSpecs
    from dependencies.dependency import AnalysisProfiles
    from dependencies.dependency import ARTemplates
    from dependencies.dependency import ARPriorities
    from dependencies.dependency import AttachmentTypes
    from dependencies.dependency import BatchLabels
    from dependencies.dependency import Calculations
    from dependencies.dependency import Containers
    from dependencies.dependency import ContainerTypes
    from dependencies.dependency import Departments
    from dependencies.dependency import Instruments
    from dependencies.dependency import InstrumentTypes
    from dependencies.dependency import LabContacts
    from dependencies.dependency import LabProducts
    from dependencies.dependency import Manufacturers
    from dependencies.dependency import Preservations
    from dependencies.dependency import ReferenceDefinitions
    from dependencies.dependency import SampleConditions
    from dependencies.dependency import SampleMatrices
    from dependencies.dependency import SamplePoints
    from dependencies.dependency import StorageLocations
    from dependencies.dependency import SampleTypes
    from dependencies.dependency import SamplingDeviations
    from dependencies.dependency import SRTemplates
    from dependencies.dependency import SubGroups
    from dependencies.dependency import Suppliers
    from dependencies.dependency import WorksheetTemplates

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    # Register each type with it's own Add permission
    # use ADD_CONTENT_PERMISSION as default
    allTypes = zip(content_types, constructors)
    for atype, constructor in allTypes:
        kind = "%s: Add %s" % (config.PROJECTNAME, atype.portal_type)
        perm = ADD_CONTENT_PERMISSIONS.get(atype.portal_type,
                                           ADD_CONTENT_PERMISSION)
        ContentInit(kind,
                    content_types      = (atype,),
                    permission         = perm,
                    extra_constructors = (constructor,),
                    fti                = ftis,
                    ).initialize(context)


def deprecated(comment=None, replacement=None):
    """ A decorator which can be used to mark functions as deprecated.
        Emits a DeprecationWarning showing the module and method being flagged
        as deprecated. If replacement is set, the warn will also show which is
        the function or class to be used instead.
    """
    def old(oldcall):
        def new(*args, **kwargs):
            message = "Deprecated: '%s.%s'" % \
                (oldcall.__module__,
                 oldcall.__name__)
            if replacement is not None:
                message += ". Use '%s.%s' instead" % \
                (replacement.__module__,
                 replacement.__name__)
            if comment is not None:
                message += ". %s" % comment
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return oldcall(*args, **kwargs)
        return new
    return old


class _DeprecatedClassDecorator(object):
    """ A decorator which can be used to mark symbols as deprecated.
        Emits a DeprecationWarning showing the symbol being flagged as
        deprecated. For add comments, use deprecated() instead of it
    """
    def __call__(self, symbol):
        message = "Deprecated: '%s.%s'" % \
            (symbol.__module__,
             symbol.__name__)
        warnings.warn(message, category=DeprecationWarning, stacklevel=2)
        return symbol

deprecatedsymbol = _DeprecatedClassDecorator()
del _DeprecatedClassDecorator


def enum(**enums):
    return type('Enum', (), enums)
