import warnings
import pkg_resources
__version__ = pkg_resources.get_distribution("bika.lims").version

# import this to create messages in the bika domain.
from OLiMS.dependencies.dependency import MessageFactory
bikaMessageFactory = MessageFactory('bika')
from OLiMS.dependencies.dependency import PloneMessageFactory as PMF

# import this to log messages
import logging
logger = logging.getLogger('Bika')

from OLiMS.lims.validators import *
from OLiMS.lims.config import *
from OLiMS.lims.permissions import *

from OLiMS.dependencies.dependency import ModuleSecurityInfo, allow_module
from OLiMS.dependencies.dependency import process_types, listTypes
from OLiMS.dependencies.dependency import utils
from OLiMS.dependencies.dependency import registerDirectory
from OLiMS.dependencies.dependency import ContentInit, ToolInit, getToolByName
from OLiMS.dependencies.dependency import PloneMessageFactory
from OLiMS.dependencies.dependency import IPloneSiteRoot
from OLiMS.dependencies.dependency import EXTENSION, profile_registry

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

    from OLiMS.dependencies.dependency import Analysis
    from OLiMS.dependencies.dependency import AnalysisCategory
    from OLiMS.dependencies.dependency import AnalysisRequest
    from OLiMS.dependencies.dependency import AnalysisRequestsFolder
    from OLiMS.dependencies.dependency import AnalysisService
    from OLiMS.dependencies.dependency import AnalysisSpec
    from OLiMS.dependencies.dependency import ARImport
    from OLiMS.dependencies.dependency import ARImportItem
    from OLiMS.dependencies.dependency import ARPriority
    from OLiMS.dependencies.dependency import AnalysisProfile
    from OLiMS.dependencies.dependency import ARReport
    from OLiMS.dependencies.dependency import ARTemplate
    from OLiMS.dependencies.dependency import Attachment
    from OLiMS.dependencies.dependency import AttachmentType
    from OLiMS.dependencies.dependency import Batch
    from OLiMS.dependencies.dependency import BatchFolder
    from OLiMS.dependencies.dependency import BatchLabel
    from OLiMS.dependencies.dependency import BikaSchema
    from OLiMS.dependencies.dependency import BikaSetup
    from OLiMS.dependencies.dependency import Calculation
    from OLiMS.dependencies.dependency import Client
    from OLiMS.dependencies.dependency import ClientFolder
    from OLiMS.dependencies.dependency import Contact
    from OLiMS.dependencies.dependency import Container
    from OLiMS.dependencies.dependency import ContainerType
    from OLiMS.dependencies.dependency import Department
    from OLiMS.dependencies.dependency import DuplicateAnalysis
    from OLiMS.dependencies.dependency import Instrument
    from OLiMS.dependencies.dependency import InstrumentCalibration
    from OLiMS.dependencies.dependency import InstrumentCertification
    from OLiMS.dependencies.dependency import InstrumentMaintenanceTask
    from OLiMS.dependencies.dependency import InstrumentScheduledTask
    from OLiMS.dependencies.dependency import InstrumentValidation
    from OLiMS.dependencies.dependency import InstrumentType
    from OLiMS.dependencies.dependency import Invoice
    from OLiMS.dependencies.dependency import InvoiceBatch
    from OLiMS.dependencies.dependency import InvoiceFolder
    from OLiMS.dependencies.dependency import LabContact
    from OLiMS.dependencies.dependency import Laboratory
    from OLiMS.dependencies.dependency import LabProduct
    from OLiMS.dependencies.dependency import Manufacturer
    from OLiMS.dependencies.dependency import Method
    from OLiMS.dependencies.dependency import Methods
    from OLiMS.dependencies.dependency import Multifile
    from OLiMS.dependencies.dependency import Organisation
    from OLiMS.dependencies.dependency import Person
    from OLiMS.dependencies.dependency import Preservation
    from OLiMS.dependencies.dependency import Pricelist
    from OLiMS.dependencies.dependency import PricelistFolder
    from OLiMS.dependencies.dependency import QueryFolder
    from OLiMS.dependencies.dependency import Query
    from OLiMS.dependencies.dependency import ReferenceAnalysis
    from OLiMS.dependencies.dependency import ReferenceDefinition
    from OLiMS.dependencies.dependency import ReferenceSample
    from OLiMS.dependencies.dependency import ReferenceSamplesFolder
    from OLiMS.dependencies.dependency import RejectAnalysis
    from OLiMS.dependencies.dependency import Report
    from OLiMS.dependencies.dependency import ReportFolder
    from OLiMS.dependencies.dependency import Sample
    from OLiMS.dependencies.dependency import SampleCondition
    from OLiMS.dependencies.dependency import SampleMatrix
    from OLiMS.dependencies.dependency import SamplePartition
    from OLiMS.dependencies.dependency import SamplePoint
    from OLiMS.dependencies.dependency import StorageLocation
    from OLiMS.dependencies.dependency import SamplesFolder
    from OLiMS.dependencies.dependency import SampleType
    from OLiMS.dependencies.dependency import SamplingDeviation
    from OLiMS.dependencies.dependency import SRTemplate
    from OLiMS.dependencies.dependency import SubGroup
    from OLiMS.dependencies.dependency import Supplier
    from OLiMS.dependencies.dependency import SupplierContact
    from OLiMS.dependencies.dependency import SupplyOrderFolder
    from OLiMS.dependencies.dependency import SupplyOrder
    from OLiMS.dependencies.dependency import Worksheet
    from OLiMS.dependencies.dependency import WorksheetFolder
    from OLiMS.dependencies.dependency import WorksheetTemplate

    from OLiMS.dependencies.dependency import AnalysisCategories
    from OLiMS.dependencies.dependency import AnalysisServices
    from OLiMS.dependencies.dependency import AnalysisSpecs
    from OLiMS.dependencies.dependency import AnalysisProfiles
    from OLiMS.dependencies.dependency import ARTemplates
    from OLiMS.dependencies.dependency import ARPriorities
    from OLiMS.dependencies.dependency import AttachmentTypes
    from OLiMS.dependencies.dependency import BatchLabels
    from OLiMS.dependencies.dependency import Calculations
    from OLiMS.dependencies.dependency import Containers
    from OLiMS.dependencies.dependency import ContainerTypes
    from OLiMS.dependencies.dependency import Departments
    from OLiMS.dependencies.dependency import Instruments
    from OLiMS.dependencies.dependency import InstrumentTypes
    from OLiMS.dependencies.dependency import LabContacts
    from OLiMS.dependencies.dependency import LabProducts
    from OLiMS.dependencies.dependency import Manufacturers
    from OLiMS.dependencies.dependency import Preservations
    from OLiMS.dependencies.dependency import ReferenceDefinitions
    from OLiMS.dependencies.dependency import SampleConditions
    from OLiMS.dependencies.dependency import SampleMatrices
    from OLiMS.dependencies.dependency import SamplePoints
    from OLiMS.dependencies.dependency import StorageLocations
    from OLiMS.dependencies.dependency import SampleTypes
    from OLiMS.dependencies.dependency import SamplingDeviations
    from OLiMS.dependencies.dependency import SRTemplates
    from OLiMS.dependencies.dependency import SubGroups
    from OLiMS.dependencies.dependency import Suppliers
    from OLiMS.dependencies.dependency import WorksheetTemplates

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
