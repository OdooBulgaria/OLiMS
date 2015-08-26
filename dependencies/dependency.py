class IPloneSiteRoot: # (ISiteRoot, INavigationRoot):
    """
    Marker interface for the object which serves as the root of a
    Plone site.
    """
    
class DirectoryRegistry:
    
    ignore=None
    
    def __init__(self):
        pass

    def registerFileExtension(self, ext, klass):
        pass

    def registerMetaType(self, mt, klass):
        pass

    def getTypeByExtension(self, ext):
        pass

    def getTypeByMetaType(self, mt):
        pass
    
    def registerDirectory(self, name, _prefix, subdirs=1, ignore=ignore):
        # This what is actually called to register a
        # file system directory to become a FSDV.
        pass

    def registerDirectoryByKey(self, filepath, reg_key, subdirs=1,
                               ignore=ignore):
        pass

    def reloadDirectory(self, reg_key):
        pass

    def getDirectoryInfo(self, reg_key):
        # This is called when we need to get hold of the information
        # for a minimal path. Can return None.
        pass

    def listDirectories(self):
        pass
    
_dirreg = DirectoryRegistry()
registerDirectory = _dirreg.registerDirectory

def process_types(types, pkg_name):
    
    pass

def listTypes(package=None):
    
    pass

class Service:

    def __init__(self):
        pass

    def validate(self, name_or_validator, value, *args, **kwargs):
        pass

    def validatorFor(self, name_or_validator):
        pass

    def register(self, validator): #XXX
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def unregister(self, name_or_validator):
        pass

validation = Service()

def providedByFallback(ob):

    # Here we have either a special object, an old-style declaration
    # or a descriptor

    # Try to get __providedBy__
    
        # Not set yet. Fall back to lower-level thing that computes it
        

    
        # We might have gotten a descriptor from an instance of a
        # class (like an ExtensionClass) that doesn't support
        # descriptors.  We'll make sure we got one by trying to get
        # the only attribute, which all specs have.
        

    

        # The object's class doesn't understand descriptors.
        # Sigh. We need to get an object descriptor, but we have to be
        # careful.  We want to use the instance's __provides__, if
        # there is one, but only if it didn't come from the class.

        
            # No __provides__, so just fall back to implementedBy
            

        # We need to make sure we got the __provides__ from the
        # instance. We'll do this by making sure we don't get the same
        # thing from the class:

        
            # The ob doesn't have a class or the class has no
            # provides, assume we're done:
            

        
            # Oops, we got the provides from the class. This means
            # the object doesn't have it's own. We should use implementedBy
            
    pass

providedBy = providedByFallback


class QuerystringRegistryReader(object):
    """Adapts a registry object to parse the querystring data."""

    def __init__(self, context, request=None):
        pass

    def parseRegistry(self):
        """Make a dictionary structure for the values in the registry"""

        pass

    def getVocabularyValues(self, values):
        """Get all vocabulary values if a vocabulary is defined"""

        pass

    def mapOperations(self, values):
        """Get the operations from the registry and put them in the key
           'operators' with the short name as key
        """
        pass

    def mapSortableIndexes(self, values):
        """Map sortable indexes"""
        pass

    def __call__(self):
        """Return the registry configuration in JSON format"""

        pass

def getEmptyTitle(context, translated=True):
    """Returns string to be used for objects with no title or id"""
    # The default is an extra fancy unicode elipsis
    pass

class router:
    """
    https://github.com/collective/plone.jsonapi.core/blob/master/src/plone/jsonapi/core/browser/router.py
    
    """
    @staticmethod
    def url_for(endpoint, **options):
        """ method to retrieve the API URL of an endpoint
        Example::
        >>> from plone.jsonapi import router
        >>> router.url_for("hello", values={"name": "jsonapi"}, force_external=True)
        """
        pass

class interface:
    pass


class IRouteProvider(interface.Interface):
    """ utlitiy which provides an api route
    """
    @staticmethod
    def initialize(context, request):
        """ get's called by the API Framework
        """
        pass
    
    @staticmethod
    def routes(self):
        """ needs to return a tuple of tuples containing
            rule, endpoint, view_func and additional options
        """
        pass

class WebIntelligentToHtmlConverter(object):

    def __init__(self, orig, tab_width=4):
        pass

    def __call__(self):
        pass

    @staticmethod
    def abbreviateUrl(url, max = 60, ellipsis = "[&hellip;]"):
        """very long urls are abbreviated to allow nicer layout
        """
        pass

    @classmethod
    def replaceURL(cls, match):
        """Replace hyperlinks with clickable <a> tags
        """
        pass

    @staticmethod
    def replaceEmail(match):
        """Replace email strings with mailto: links
        """
        pass

    def indentWhitespace(self, match):
        """Make leading whitespace on a line into &nbsp; to preserve indents
        """
        pass
    
def convertWebIntelligentPlainTextToHtml(orig, tab_width=4):
    """Converts text/x-web-intelligent to text/html
    """
    pass

def convertHtmlToWebIntelligentPlainText(orig):
    """Converts text/html to text/x-web-intelligent.
    """
    @staticmethod
    def savePres(match):
        pass
    @staticmethod
    def fixTagWhitespace(match):
        """Make whitespace-tag-whitespace into whitespace-tag.
        Repeat this in case there are directly nested tags.
        """
        # Remove any superfluous whitespace, but preserve one leading space
        pass


class tableview:
    pass


class Table(object):
    """
    The table renders a table with sortable columns etc.
    It is meant to be subclassed to provide methods for getting specific table
    info.
    """

    def __init__(self, request, base_url, view_url, items,
                 show_sort_column=False, buttons=None, pagesize=20,
                 show_select_column=True, show_size_column=True,
                 show_modified_column=True, show_status_column=True):
        pass
    
    def msg_select_item(self, item):
        pass

    def within_batch_size(self):
        pass

    def set_checked(self, item):
        pass

    
    def batch(self):
        pass

    def batching(self):
        pass

    def _get_select_currentbatch(self):
        pass

    def _set_select_currentbatch(self, value):
        pass

    def _get_select_all(self):
        pass

    def _set_select_all(self, value):
        pass

    def show_select_all_items(self):
        pass

    def get_nosort_class(self):
        """
        """
        pass

    def selectall_url(self):
        pass

    def selectscreen_url(self):
        pass

    def selectnone_url(self):
        pass

    def show_all_url(self):
        pass

    def selected(self, item):
        pass

    def viewname(self):
        return self.view_url.split('?')[0].split('/')[-1]

    def quote_plus(self, string):
        pass
    
    
class Lazy(object):
    """Lazy Attributes.
    """

    def __init__(self, func, name=None):
        pass

    def __get__(self, inst, class_):
        pass
    
    
class PropertyMapping:

    def __init__(self):
        pass

    def register(self, property, type, klass=None):
        pass

    def getType(self, property, klass):
        pass

propertyMapping = PropertyMapping()
registerPropertyType = propertyMapping.register


class DateTimeError(Exception):
    pass
class PersistentMapping: #(Persistent, PersistentMapping):
    """Legacy persistent mapping class
    This class mixes in ExtensionClass Base if it is present.
    Unless you actually want ExtensionClass semantics, use
    persistent.mapping.PersistentMapping instead.
    """

    def __setstate__(self, state):
        pass
        
def check(request, extra='', name="_authenticator"):
    pass

def postonly(request):
    pass
        
class PropertyManager: #(Base):
    """
    https://github.com/zopefoundation/Zope/blob/master/src/OFS/PropertyManager.py
    """
    pass


class ExtensibleMetadata: #(Persistence.Persistent):
    """ A DC metadata implementation for Plone Archetypes
    """
    """
    https://github.com/plone/Products.Archetypes/blob/master/Products/Archetypes/ExtensibleMetadata.py
    """
    pass


class BaseContentMixin: #(CatalogMultiplex,
#                        BaseObject,
#                        PortalContent,
#                        Historical):
    """A not-so-basic CMF Content implementation that doesn't
    include Dublin Core Metadata"""

    def manage_afterAdd(self, item, container):
        pass

    def manage_afterClone(self, item):
        pass

    def manage_beforeDelete(self, item, container):
        pass

    def _notifyOfCopyTo(self, container, op=0):
        """OFS.CopySupport notify
        """
        pass

class BaseContent(BaseContentMixin,
                  ExtensibleMetadata,
                  PropertyManager):
    """A not-so-basic CMF Content implementation with Dublin Core
    Metadata included"""


    schema = BaseContentMixin.schema + ExtensibleMetadata.schema

    def __init__(self, oid, **kwargs):
        BaseContentMixin.__init__(self, oid, **kwargs)
        ExtensibleMetadata.__init__(self)
        
BaseSchema = BaseContent.schema

ATContentTypeSchema = BaseSchema.copy()

ATDocumentSchema = ATContentTypeSchema.copy()

CollectionSchema = ATDocumentSchema.copy()

class permissions:
    def __init__(self):
        pass
    
    View = 'view'
    ModifyPortalContent = 'Modify portal content'
    
class event:
    """
    https://github.com/zopefoundation/zope.event/blob/master/src/zope/event/__init__.py
    
    """
    """ Base event system implementation
    """
    
    #: Applications may register for notification of events by appending a
    #: callable to the ``subscribers`` list.
    #: 
    #: Each subscriber takes a single argument, which is the event object
    #: being published.
    #:
    #: Exceptions raised by subscribers will be propagated.
    @staticmethod
    def notify(event):
        """ Notify all subscribers of ``event``.
        """
        pass

def mg(v, unit='', ounit=''):
    """Builds a Magnitude from a number and a units string"""
    pass

class schemata:
    """
    https://github.com/plone/Products.ATContentTypes/blob/master/Products/ATContentTypes/content/schemata.py
    
    """
    @staticmethod
    def finalizeATCTSchema(schema, folderish=False, moveDiscussion=True):
        """Finalizes an ATCT type schema to alter some fields
        """
        pass
    
    
class ATFolder: #(ATCTFolderMixin, BaseBTreeFolder):
    """ a folder suitable for holding a very large number of items """
    
    def getNextPreviousParentValue(self):
        """ If the parent node is also an IATFolder and has next/previous
            navigation enabled, then let this folder have it enabled by
            default as well """
        pass
    
class SpecificationBasePy(object):

    def providedBy(self, ob):
        """Is the interface implemented by an object
        """
        pass

    def implementedBy(self, cls):
        """Test whether the specification is implemented by a class or factory.
        Raise TypeError if argument is neither a class nor a callable.
        """
        pass

    def isOrExtends(self, interface):
        """Is the interface the same as or extend the given interface
        """
        pass


SpecificationBase = SpecificationBasePy


class Specification(SpecificationBase):
    """Specifications
    An interface specification is used to track interface declarations
    and component registrations.
    This class is a base class for both interfaces themselves and for
    interface specifications (declarations).
    Specifications are mutable.  If you reassign their bases, their
    relations with other specifications are adjusted accordingly.
    """

    # Copy some base class methods for speed
    

    def __init__(self, bases=()):
        pass

    def subscribe(self, dependent):
        pass

    def unsubscribe(self, dependent):
        pass

    def __setBases(self, bases):
        # Register ourselves as a dependent of our old bases
        pass

    def changed(self, originally_changed):
        """We, or something we depend on, have changed
        """
        pass


    def interfaces(self):
        """Return an iterator for the interfaces in the specification.
        """
        pass


    def extends(self, interface, strict=True):
        """Does the specification extend the given interface?
        Test whether an interface in the specification extends the
        given interface
        """
        pass

    def weakref(self, callback=None):
        pass

    def get(self, name, default=None):
        """Query for an attribute description
        """
        pass
    
_marker = object()


class InterfaceBasePy(object):
    """Base class that wants to be replaced with a C base :)
    """

    def __call__(self, obj, alternate=_marker):
        """Adapt an object to the interface
        """
        pass
    def __adapt__(self, obj):
        """Adapt an object to the reciever
        """
        pass
    
InterfaceBase = InterfaceBasePy
class Element(object):

    # We can't say this yet because we don't have enough
    # infrastructure in place.
    #
    #implements(IElement)

    def __init__(self, __name__, __doc__=''):
        """Create an 'attribute' description
        """
        pass

    def getName(self):
        """ Returns the name of the object. """
        pass

    def getDoc(self):
        """ Returns the documentation for the object. """
        pass

    def getTaggedValue(self, tag):
        """ Returns the value associated with 'tag'. """
        pass

    def queryTaggedValue(self, tag, default=None):
        """ Returns the value associated with 'tag'. """
        pass

    def getTaggedValueTags(self):
        """ Returns a list of all tags. """
        pass

    def setTaggedValue(self, tag, value):
        """ Associates 'value' with 'key'. """
        pass
    
    
class InterfaceClass(Element, InterfaceBase, Specification):
    """Prototype (scarecrow) Interfaces Implementation."""

    # We can't say this yet because we don't have enough
    # infrastructure in place.
    #
    #implements(IInterface)

    def __init__(self, name, bases=(), attrs=None, __doc__=None,
                 __module__=None):

        pass

    def interfaces(self):
        """Return an iterator for the interfaces in the specification.
        """
        pass

    def getBases(self):
        pass

    def isEqualOrExtendedBy(self, other):
        """Same interface or extends?"""
        pass

    def names(self, all=False):
        """Return the attribute names defined by the interface."""
        pass

    def __iter__(self):
        pass

    def namesAndDescriptions(self, all=False):
        """Return attribute names and descriptions defined by interface."""
        pass

    def getDescriptionFor(self, name):
        """Return the attribute description for the given name."""
        pass

    def __contains__(self, name):
        pass

    def direct(self, name):
        pass

    def queryDescriptionFor(self, name, default=None):
        pass

    def validateInvariants(self, obj, errors=None):
        """validate object to defined invariants."""
        pass

    def __repr__(self):  # pragma: no cover
        pass

    def _call_conform(self, conform):
        pass

    def __reduce__(self):
        pass

    def __cmp(self, other):
        # Yes, I did mean to name this __cmp, rather than __cmp__.
        # It is a private method used by __lt__ and __gt__.
        # I don't want to override __eq__ because I want the default
        # __eq__, which is really fast.
        """Make interfaces sortable
        TODO: It would ne nice if:
           More specific interfaces should sort before less specific ones.
           Otherwise, sort on name and module.
           But this is too complicated, and we're going to punt on it
           for now.
        For now, sort on interface and module name.
        None is treated as a pseudo interface that implies the loosest
        contact possible, no contract. For that reason, all interfaces
        sort before None.
        """
        pass

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass


Interface = InterfaceClass("Interface", __module__ = 'zope.interface')

class IQueryField(Interface):
    """Query field interface """
    pass

class IField(Interface):
    """ Interface for fields """

#     required = Attribute('required', 'Require a value to be present when submitting the field')
#     default = Attribute('default', 'Default value for a field')
#     default_method = Attribute('default_method', 'Name of a method on the field ' +
#                                                  'or an actual function instance to return the default')
#     vocabulary = Attribute('vocabulary', 'List of suggested values for the field')
#     vocabulary_factory = Attribute('vocabulary_factory', 'Name of Zope 3 vocabulary factory')
#     enforceVocabulary = Attribute('enforceVocabulary', \
#                                   'Restrict the allowed values to the ones in the vocabulary')
#     multiValued = Attribute('multiValued', 'Allow the field to have multiple values')
#     searchable = Attribute('searchable', 'Make the field searchable')
#     isMetadata = Attribute('isMetadata', 'Is this field a metadata field?')
#     accessor = Attribute('accessor', 'Use this method as the accessor for the field')
#     mutator = Attribute('mutator', 'Use this method as the mutator for the field')
#     mode = Attribute('mode', 'Mode of access to this field')
#     read_permission = Attribute('read_permission', \
#                                 'Permission to use to protect field reading')
#     write_permission = Attribute('write_permission', \
#                                  'Permission to use to protect writing to the field')

#     storage = Attribute('storage', 'Storage class to use for this field')
#     form_info = Attribute('form_info', 'Form Info (?)')
#     generateMode = Attribute('generateMode', 'Generate Mode (?)')
#     force = Attribute('force', 'Force (?)')
#     type = Attribute('type', 'Type of the field')
    @staticmethod
    def Vocabulary(content_instance=None):
        """
        returns a DisplayList
        uses self.vocabulary as source
        1) Dynamic vocabulary:
            precondition: a content_instance is given.
            has to return a:
                * DisplayList or
                * list of strings or
                * list of 2-tuples with strings:
                    '[("key1","value 1"),("key 2","value 2"),]'
            the output is postprocessed like a static vocabulary.
            vocabulary is a string:
                if a method with the name of the string exists it will be called
            vocabulary is a class implementing IVocabulary:
                the "getDisplayList" method of the class will be called.
        2) Static vocabulary
            * is already a DisplayList
            * is a list of 2-tuples with strings (see above)
            * is a list of strings (in this case a DisplayList with key=value
              will be created)
        3) Zope 3 vocabulary factory vocabulary
            - precondition: a content_instance is given
            - self.vocabulary_factory is given
            - a named utility providing zope.schema.interfaces.IVocbularyFactory
              exists for the name self.vocabulary_factory.
        """
        pass

    @staticmethod
    def copy():
        """Return a copy of field instance [PRIVATE]
        Consisting of field name and properties dictionary.
        """
        pass

    @staticmethod
    def validate(value, instance, errors={}, **kwargs):
        """Validate passed-in value using all field validators.
        Return None if all validations pass; otherwise, return failed
        result returned by validator
        """
        pass

    @staticmethod
    def validate_required(instance, value, errors):
        """Validate the required flag for a field [PRIVATE]
        Overwrite it in your field for special case handling like empty files
        """
        pass
    
    @staticmethod
    def checkPermission(mode, instance):
        """
        Check whether the security context allows the given permission on
        the given object.
        Arguments:
        permission -- A permission name
        instance -- The object being accessed according to the permission
        """
        pass

    @staticmethod
    def checkExternalEditor(instance):
        """ Checks if the user may edit this field and if
        external editor is enabled on this instance
        """
    @staticmethod
    def getWidgetName():
        """Return the widget name that is configured for this field as
        a string"""
        pass

    @staticmethod
    def getName():
        """Return the name of this field as a string"""
        pass
    
    @staticmethod
    def getType():
        """Return the type of this field as a string"""
        pass

    @staticmethod
    def getDefault(instance):
        """Return the default value to be used for initializing this
        field"""
        pass
    
    @staticmethod
    def getAccessor(instance):
        """Return the accessor method for getting data out of this
        field"""
        pass

    @staticmethod
    def getEditAccessor(instance):
        """Return the accessor method for getting raw data out of this
        field e.g.: for editing
        """
        pass

    @staticmethod
    def getMutator(instance):
        """Return the mutator method used for changing the value
        of this field"""
        pass

    @staticmethod
    def toString():
        """Utility method for converting a Field to a string [PRIVATE]
        For the purpose of comparing fields.  This comparison is used for
        determining whether a schema has changed in the auto update
        function.  Right now it's pretty crude."""
        pass

    @staticmethod
    def isLanguageIndependent(instance):
        """Get the language independed flag for i18n content (used by LinguaPlon)
        """
        pass
    
    
class IDateTimeField(IField):
    """Marker interface for date/time field
    """
    pass


class LocaleProvider(object):
    """A locale provider that get's its data from the XML data."""


    def __init__(self, locale_dir):
        pass

    def loadLocale(self, language=None, country=None, variant=None):
        """See zope.i18n.interfaces.locales.ILocaleProvider"""
        # Creating the filename
        pass

    def getLocale(self, language=None, country=None, variant=None):
        """See zope.i18n.interfaces.locales.ILocaleProvider"""
        # We want to be liberal in what we accept, but the standard is lower
        # case language codes, upper case country codes, and upper case
        # variants, so coerce case here.
        pass
    
LOCALEDIR = "My Local Directory"
    
locales = LocaleProvider(LOCALEDIR)

_BLANK = None

def getAdapter(object, interface=Interface, name=_BLANK, context=None):
    pass


class _Wrapper:
    pass


class ImplicitAcquisitionWrapper(_Wrapper):
    pass


class IConstrainTypes(Interface):
    """
    Interface for folderish content types supporting restricting addable types
    on a per-instance basis.
    """
    @staticmethod
    def getConstrainTypesMode():
        """
        Find out if add-restrictions are enabled. Returns 0 if they are
        disabled (the type's default FTI-set allowable types is in effect),
        1 if they are enabled (only a selected subset if allowed types will be
        available), and -1 if the allowed types should be acquired from the
        parent. Note that in this case, if the parent portal type is not the
        same as the portal type of this object, fall back on the default (same
        as 0)
        """
        pass

    @staticmethod
    def getLocallyAllowedTypes():
        """
        Get the list of FTI ids for the types which should be allowed to be
        added in this container.
        """
        pass

    @staticmethod
    def getImmediatelyAddableTypes():
        """
        Return a subset of the FTI ids from getLocallyAllowedTypes() which
        should be made most easily available.
        """
        pass
    
    @staticmethod
    def getDefaultAddableTypes():
        """
        Return a list of FTIs which correspond to the list of FTIs available
        when the constraint mode = 0 (that is, the types addable without any
        setLocallyAllowedTypes trickery involved)
        """
        pass

    @staticmethod
    def allowedContentTypes():
        """
        Return the list of currently permitted FTIs.
        """
        pass
    
    
class IVocabularyFactory(Interface):
    """Can create vocabularies."""
    @staticmethod
    def __call__(context):
        """The context provides a location that the vocabulary can make use of.
        """
        pass
    

class ExtensionClass(type):

    def __new__(cls, name, bases=(), attrs={}):
        pass

    def __basicnew__(self):
        """Create a new empty object"""
        pass

    def mro(self):
        """Compute an mro using the 'encapsulated base' scheme"""
        pass

    def inheritedAttribute(self, name):
        """Look up an inherited attribute"""
        pass

    def __setattr__(self, name, value):
        pass
    
Base = ExtensionClass("Base", (object, ), {
#     '__slots__': (),
#     '__getattribute__': Base_getattro,
#     '__getstate__': Base__getstate__,
#     '__setstate__': Base__setstate__,
#     '__reduce__': Base__reduce__,
#     '__new__': Base__new__,
})    

class _Acquirer(ExtensionClass.Base):

    def __getattribute__(self, name):
        pass

    def __of__(self, context):
        pass
    
    
class Implicit(_Acquirer):
    pass


class ProfileRegistry(Implicit):

    """ Track registered profiles.
    """
    BASE = None
    def __init__(self):
        pass

    def getProfileInfo(self, profile_id, for_=None):
        """ See IProfileRegistry.
        """
        pass

    def listProfiles(self, for_=None):
        """ See IProfileRegistry.
        """
        pass

    def listProfileInfo(self, for_=None):
        """ See IProfileRegistry.
        """
        pass

    def registerProfile(self, name, title, description, path, product=None,
                        profile_type=BASE, for_=None):
        """ See IProfileRegistry.
        """
        pass

    def _computeProfileId(self, name, product):
        pass

    def unregisterProfile(self, name, product=None):
        pass

    def clear(self):
        pass
        
_profile_registry = ProfileRegistry()

class SecurityInfo(Implicit):
    """Encapsulate security information."""


    def __init__(self):
        pass

    def _setaccess(self, names, access):
        pass
    
    def declarePublic(self, name, *names):
        """Declare names to be publicly accessible."""
        pass

    
    def declarePrivate(self, name, *names):
        """Declare names to be inaccessible to restricted code."""
        pass

    
    def declareProtected(self, permission_name, name, *names):
        """Declare names to be associated with a permission."""
        pass

    
    def declareObjectPublic(self):
        """Declare the object to be publicly accessible."""
        pass

    
    def declareObjectPrivate(self):
        """Declare the object to be inaccessible to restricted code."""
        pass

    
    def declareObjectProtected(self, permission_name):
        """Declare the object to be associated with a permission."""
        pass

    
    def public(self, func):
        """Decorate a function to be publicly accessible."""
        pass

    
    def private(self, func):
        """Decorate a function to be inaccessible to restricted code."""
        pass

   
    def protected(self, permission_name):
        """Return a decorator to associate a function with a permission."""
        # the decorator returned is remembered in a set and will
        # remove itself upon call. self.apply will check for an empty
        # set and raise an AssertionError otherwise.
        pass
    
    def setPermissionDefault(self, permission_name, roles):
        """Declare default roles for a permission"""
        pass

    
    def setDefaultAccess(self, access):
        """Declare default attribute access policy.
        This should be a boolean value, a map of attribute names to
        booleans, or a callable (name, value) -> boolean.
        """
        pass


class ClassSecurityInfo(SecurityInfo):
    """Encapsulate security information for class objects."""

    def apply(self, classobj):
        """Apply security information to the given class object."""
        pass
        

class Unauthorized: #(zExceptions.Unauthorized):

    def getValueName(self):
        pass
def aq_parent(obj):
    # needs to be safe to call from __getattribute__ of a wrapper
    # and reasonably fast
    pass

def aq_inner(obj):
    pass

_NOT_GIVEN = None
def aq_get(obj, name, default=_NOT_GIVEN, containment=False):

    # Not wrapped. If we have a __parent__ pointer, create a wrapper
    # and go as usual
    pass

def aq_base(obj):
    pass

def getSecurityManager():
    """Get a security manager, for the current thread.
    """
    pass

def ModuleSecurityInfo(module_name=None):
    pass

def allow_module(module_name):
    """Allow a module and all its contents to be used from a
    restricted Script. The argument module_name may be a simple
    or dotted module or package name. Note that if a package
    path is given, all modules in the path will be available."""
    pass

EXTENSION = 2 
ApplyVersionControl = 'CMFEditions: Apply version control'
SaveNewVersion = 'CMFEditions: Save new version'
AccessPreviousVersions = 'CMFEditions: Access previous versions'
AddPortalContent = 'Add portal content'
ManagePortal = 'Manage portal'
nobody = "Anonymous User"
ATCT_TOOLNAME = 'portal_atct'
View = 'view'
ListFolderContents = 'List folder contents'
access_contents_information='Access contents information'
add_database_methods='Add Database Methods'
add_documents_images_and_files='Add Documents, Images, and Files'
add_external_methods='Add External Methods'
add_folders='Add Folders'
add_mailhost_objects='Add MailHost objects'
add_page_templates='Add Page Templates'
add_python_scripts='Add Python Scripts'
add_user_folders='Add User Folders'
add_vocabularies='Add Vocabularies'
add_z_gadfly_database_connections='Add Z Gadfly Database Connections'
add_zcatalogs='Add ZCatalogs'
add_zope_tutorials='Add Zope Tutorials'
change_database_connections='Change Database Connections'
change_database_methods='Change Database Methods'
change_external_methods='Change External Methods'
change_images_and_files='Change Images and Files'
change_python_scripts='Change Python Scripts'
change_configuration='Change configuration'
change_page_templates='Change Page Templates'
change_permissions='Change permissions'
change_proxy_roles='Change proxy roles'
copy_or_move='Copy or Move'
create_class_instances='Create class instances'
define_permissions='Define permissions'
delete_objects='Delete objects'
edit_factories='Edit Factories'
ftp_access='FTP access'
import_export_objects='Import/Export objects'
manage_vocabulary='Manage Vocabulary'
manage_zcatalog_entries='Manage ZCatalog Entries'
manage_zcatalog_indexes='Manage ZCatalogIndex Entries'
manage_properties='Manage properties'
manage_users='Manage users'
open_close_database_connection='Open/Close Database Connection'
open_close_database_connections='Open/Close Database Connections'
query_vocabulary='Query Vocabulary'
search_zcatalog='Search ZCatalog'
take_ownership='Take ownership'
test_database_connections='Test Database Connections'
undo_changes='Undo changes'
use_database_methods='Use Database Methods'
use_factories='Use Factories'
use_mailhost_services='Use mailhost services'
view='View'
view_history='View History'
view_management_screens='View management screens'
webdav_access='WebDAV access'
webdav_lock_items='WebDAV Lock items'
webdav_unlock_items='WebDAV Unlock items'


new_loc = 'DocumentTemplate.permissions'


# class ClassSecurityInfo(SecurityInfo):
#     """Encapsulate security information for class objects."""
#     __roles__ = ACCESS_PRIVATE
# 
#     apply__roles__ = ACCESS_PRIVATE
#     def apply(self, classobj):
#         """Apply security information to the given class object."""
#         pass
    
def newSecurityManager(request, user):
    """Set up a new security context for a request for a user
    """
    pass


def InitializeClass(self):
    pass

class DefaultLayerContainer(Base):

    def __init__(self):
        pass

    
    def registerLayer(self, name, object):
        pass

    
    def registeredLayers(self):
        pass

    
    def hasLayer(self, name):
        pass

    
    def getLayerImpl(self, name):
        pass

class Field(DefaultLayerContainer):
    pass


class ComputedField(Field):
    """A field that always returns a computed."""
    
    def set(self, *ignored, **kwargs):
        pass

    def get(self, instance, **kwargs):
        """Return the computed value."""
        pass

    def get_size(self, instance):
        """Get size of the stored data.
        Used for get_size in BaseObject.
        """
        pass
    
    
class ObjectField(Field):
    """Base Class for Field objects that fundamentaly deal with raw
    data. This layer implements the interface to IStorage and other
    Field Types should subclass this to delegate through the storage
    layer.
    """
    
    def get(self, instance, **kwargs):
        pass
    
    def getRaw(self, instance, **kwargs):
        pass


    def set(self, instance, value, **kwargs):
        pass

    def unset(self, instance, **kwargs):
        pass

    def setStorage(self, instance, storage):
        pass
    
    def getStorage(self, instance=None):
        pass

    
    def getStorageName(self, instance=None):
        """Return the storage name that is configured for this field
        as a string"""
        pass

    
    def getStorageType(self, instance=None):
        """Return the type of the storage of this field as a string"""
        pass

    def setContentType(self, instance, value):
        """Set mimetype in the base unit.
        """
        pass

    def getContentType(self, instance, fromBaseUnit=True):
        """Return the mime type of object if known or can be guessed;
        otherwise, return default_content_type value or fallback to
        'application/octet-stream'.
        """
        pass
    
    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        Should be overwritte by special fields like FileField. It's safe for
        fields which are storing strings, ints and BaseUnits but it won't return
        the right results for fields containing OFS.Image.File instances or
        lists/tuples/dicts.
        """
        pass
 
 
class QueryField(ObjectField):
    """QueryField for storing query"""


    def get(self, instance, **kwargs):
        """Get the query dict from the request or from the object"""
        pass

    def getRaw(self, instance, **kwargs):
        pass   
    

class BooleanField(ObjectField):
    """A field that stores boolean values."""
   
    def get(self, instance, **kwargs):
        pass

    def getRaw(self, instance, **kwargs):
        pass

    def set(self, instance, value, **kwargs):
        """If value is not defined or equal to 0, set field to false;
        otherwise, set to true."""
        pass
    
    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        """
        pass
    
    
class StringField(ObjectField):
    """A field that stores strings"""
    
    def get(self, instance, **kwargs):
        pass

    def set(self, instance, value, **kwargs):
        pass
    
    
class FixedPointField(ObjectField):
    """A field for storing numerical data with fixed points
    Test for fix for Plone issue #9414: '0' and '0.0' should count as values
    when validating required fields.  (A return value of None means validation
    passed.)
    >>> f = FixedPointField()
    >>> f.validate_required(None, '0', [])
    >>> f.validate_required(None, '0.0', [])
    """

    def _to_tuple(self, instance, value):
        """Turn the value into a tuple that we will store.
        We will test some inputs.
        >>> f = FixedPointField()
        >>> instance = object()
        >>> f._to_tuple(instance, '0')
        (0, 0)
        >>> f._to_tuple(instance, '1.0')
        (1, 0)
        >>> f._to_tuple(instance, '-1.0')
        (-1, 0)
        >>> f._to_tuple(instance, '0.5')
        (0, 50)
        >>> f._to_tuple(instance, None)
        Negative numbers between -1 and -0 need to be handled
        differently as there is no difference between +0 and -0.
        >>> f._to_tuple(instance, '-0.5')
        (0, -50)
        Commas are accepted too:
        >>> f._to_tuple(instance, '1,23')
        (1, 23)
        You can also start with a dot or comma:
        >>> f._to_tuple(instance, '.23')
        (0, 23)
        >>> f._to_tuple(instance, ',23')
        (0, 23)
        >>> f._to_tuple(instance, '-.23')
        (0, -23)
        Now for some precision:
        >>> f._to_tuple(instance, '1,2345')
        (1, 23)
        >>> g = FixedPointField(precision=4)
        >>> g._to_tuple(instance, '1,2345')
        (1, 2345)
        >>> g._to_tuple(instance, '10')
        (10, 0)
        >>> g._to_tuple(instance, '9.0001')
        (9, 1)
        """
        
        # XXX :-(
        # Decimal Point is very english. as a first hack
        # we should allow also the more contintental european comma.
        # The clean solution is to lookup:
        # * the locale settings of the zope-server, Plone, logged in user
        # * maybe the locale of the browser sending the value.
        # same should happen with the output.
        pass

    def set(self, instance, value, **kwargs):
        pass

    def get(self, instance, **kwargs):
        pass
    

class IntegerField(ObjectField):
    """A field that stores an integer"""

   
    def validate_required(self, instance, value, errors):
        pass

    def set(self, instance, value, **kwargs):
        pass


class FloatField(ObjectField):
    """A field that stores floats"""

    def validate_required(self, instance, value, errors):
        pass

    def set(self, instance, value, **kwargs):
        """Convert passed-in value to a float. If failure, set value to
        None."""
        pass
    
        
class LinesField(ObjectField):
    """For creating lines objects"""

    def set(self, instance, value, **kwargs):
        """
        If passed-in value is a string, split at line breaks and
        remove leading and trailing white space before storing in object
        with rest of properties.
        """
        pass

    def get(self, instance, **kwargs):
        pass

    def getRaw(self, instance, **kwargs):
        pass

    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        """
        pass    
    
class Interface:
    pass


def sortable_value(value):
    pass

class datepickerconfig: #(BrowserView):

    calendar_type = 'gregorian'

    def __call__(self):
        pass

class WidgetTraverse: #(BrowserView):

    def getConfig(self):
        """get the config"""
        pass
    
    @property
    def macros(self):
        pass

class MultiSelectWidget(WidgetTraverse):

    def getValues(self, index=None):
        pass
    
    def getSortedValuesKeys(self, values):
        # do a lowercase sort of the keys
        pass


class SelectWidget(MultiSelectWidget):

    def getValues(self, index=None):
        pass
    
    def getSortedValuesKeys(self, values):
        # do a lowercase sort of the keys
        pass


# class WidgetTraverse: #(BrowserView):
# 
#     def getConfig(self):
#         """get the config"""
#         pass
#     
#     @property
#     def macros(self):
#         pass
    
    
class QueryWidget: #(TypesWidget):

    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """A custom implementation for the widget form processing."""
        pass
    
    def getConfig(self):
        """get the config"""
        pass
    
    def SearchResults(self, request, context, accessor):
        pass

class ReferenceWidget:
    pass


class InAndOutWidget(ReferenceWidget):
    pass
    
        
class ReferenceBrowserWidget(ReferenceWidget):
    
    def getStartupDirectory(self, instance, field):
        """get widget startup directory
        """
        pass
    
    def getBaseQuery(self, instance, field):
        """Return base query to use for content search
        """
        pass
    
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """Basic impl for form processing in a widget
        """
        pass


def getStartupDirectory(context, directory=''):
    """ Construct a path from `context` and `directory`

        Mapping works as follows:

        directory == ''                  => Current object
        directory == '/absolute/url'     => Portal root + absolute url
        directory == '../relative/url'   => Current object + relative url

        If the object is in the portal_factory, remove the factory from the
        equation.
        This creates an inconsistency with the case when directory is not set,
        because the current object is in the factory and thus not generally
        useful as a starting point for browsing (it won't contain any sub-
        objects, and the parent object is the factory's temporary folder).
        Hence, in this case, the startup directory is the parent folder.

        Similarly, if directory is a relative path starting with '../' and
        the object is in the factory, let the first '../' part of the relative
        URL refer to the destination parent folder, not the factory.

        Default case - if no directory is given, search for a property
        refwidget_startupdirectories in portal_properties/site_properties
        that is a lines field having the following
        form:
            path1:path2
        path1 is the path where all widgets being under it set
        startup_directory to path2 if no startup_directory is set.
    """

    def filterPortalFactory(url):
        """Return context's url + the relative url given, but remove any
        reference to portal_factory.
        """

        pass

    def checkPath(path):
        """ checks if path starts with /

            if, then path is relative to portal root
        """
        pass


def quotestring(s):
    """ Return a double-quoted string

        >>> quotestring('hello world!')
        '"hello world!"'
    """
    pass


def quotequery(s):
    """ Quote a string query

        Quote reserved query words, if they occur on special
        positions:

        >>> quotequery('foo and')
        'foo "and"'
    """
    pass


def getSearchCatalog(context, name=''):
    """ Get named catalog in portal of context with fallback
    """
    pass


class IExtensible(Interface):
    """Marker interface applied to extensible content types
    """
    pass


class IExtensionField(Interface):
    """Extension field"""

    @staticmethod
    def getAccessor(instance):
        """Return the accessor method for getting data out of this field."""
        pass

    @staticmethod
    def getEditAccessor(instance):
        """Return the accessor method for getting raw data out of this field
        e.g.: for editing.
        """
        pass
    @staticmethod
    def getMutator(instance):
        """Return the mutator method used for changing the value of this field.
        """
        pass
    @staticmethod
    def getIndexAccessor(instance):
        """Return the index accessor, i.e. the getter for an indexable value.
        """
        pass


class ITranslatableExtensionField(IExtensionField):
    """Extension field for ITranslatable"""
    @staticmethod
    def getTranslationMutator(instance):
        """Return a mutator for translatable values"""
        pass
    @staticmethod
    def isLanguageIndependent(instance):
        """Get the language independed flag for i18n content."""
        pass


class ISchemaExtender(Interface):
    """Interface for adapters that extend the schema"""
    @staticmethod
    def __init__(context):
        """Constructor. Takes the instance whose schema we are frobbing."""
        pass
    @staticmethod
    def getFields():
        """Return a list of fields to be added to the schema."""
        pass


class IOrderableSchemaExtender(ISchemaExtender):
    """An orderable version of the schema extender"""
    @staticmethod
    def getOrder(original):
        """Return the optionally reordered fields.

        'original' is a dictionary where the keys are the names of
        schemata and the values are lists of field names, in order.

        The method should return a new such dictionary with re-ordered
        lists.

        It is recommended to use an OrderedDict (available as
        Products.Archetypes.utils.OrderedDict) to guarantee proper ordering
        of schemata.
        """
        pass


class IBrowserLayerAwareExtender(Interface):
    """An plone browserlayer aware schemaextender.

    Extenders with this interface are used only in context of the given
    browserlayer.
    """

    pass


class ISchemaModifier(Interface):
    """Interface for adapters that modify the existing schema.

    Before you're allowed to use this method, you must take the Oath
    of the Schema Modifier. Repeat after us:

      "I <name>, hereby do solemnly swear, to refrain, under any
       circumstances, from using this adapter for Evil. I will not
       delete fields, change field types or do other breakable and evil
       things. Promise."

    Okay, then we can all move on.
    """
    @staticmethod
    def __init__(context):
        """Constructor. Takes the instance whose schema we are frobbing."""
        pass
    @staticmethod
    def fiddle(schema):
        """Fiddle the schema.

        This is a copy of the class' schema, with any ISchemaExtender-provided
        fields added. The schema may be modified in-place: there is no
        need to return a value.

        In general, it will be a bad idea to delete or materially change
        fields, since other components may depend on these ones.

        If you change any fields, then you are responsible for making a copy of
        them first and place the copy in the schema.
        """
        pass

def namedtuple(typename, field_names, verbose=False, rename=False):
    #Ubaid start from here
    """Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessable by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

    """

    # Validate the field names.  At the user's option, either generate an error
    # message or automatically replace the field name with a valid name.
    
    # Fill-in the class template
    

    # For pickling to work, the __module__ variable needs to be set to the frame
    # where the named tuple is created.  Bypass this step in environments where
    # sys._getframe is not defined (Jython for example) or sys._getframe is not
    # defined for arguments greater than 0 (IronPython).
    pass

class InitialiseProgressBar: #(ObjectEvent):

    pass


class ProgressBar(object):

    def __init__(self, context, request, title, description, view=None):
        pass


class ProgressState(object):

    def __init__(self, request, progress):
        pass


class UpdateProgressEvent: #(ObjectEvent):
    pass

def getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell."""
    pass

class DateTime(object):
    """DateTime objects represent instants in time and provide
       interfaces for controlling its representation without
       affecting the absolute value of the object.

       DateTime objects may be created from a wide variety of string
       or numeric data, or may be computed from other DateTime objects.
       DateTimes support the ability to convert their representations
       to many major timezones, as well as the ablility to create a
       DateTime object in the context of a given timezone.

       DateTime objects provide partial numerical behavior:

          - Two date-time objects can be subtracted to obtain a time,
            in days between the two.

          - A date-time object and a positive or negative number may
            be added to obtain a new date-time object that is the given
            number of days later than the input date-time object.

          - A positive or negative number and a date-time object may
            be added to obtain a new date-time object that is the given
            number of days later than the input date-time object.

          - A positive or negative number may be subtracted from a
            date-time object to obtain a new date-time object that is
            the given number of days earlier than the input date-time
            object.

        DateTime objects may be converted to integer, long, or float
        numbers of days since January 1, 1901, using the standard int,
        long, and float functions (Compatibility Note: int, long and
        float return the number of days since 1901 in GMT rather than
        local machine timezone). DateTime objects also provide access
        to their value in a float format usable with the python time
        module, provided that the value of the object falls in the
        range of the epoch-based time module, and as a datetime.datetime
        object.

        A DateTime object should be considered immutable; all conversion
        and numeric operations return a new DateTime object rather than
        modify the current object."""

    

    def __init__(self, *args, **kw):
        """Return a new date-time object"""
        pass

    def __getstate__(self):
        # We store a float of _micros, instead of the _micros long, as we most
        # often don't have any sub-second resolution and can save those bytes
        pass

    def __setstate__(self, value):
        pass

    def _parse_args(self, *args, **kw):
        """Return a new date-time object.

        A DateTime object always maintains its value as an absolute
        UTC time, and is represented in the context of some timezone
        based on the arguments used to create the object. A DateTime
        object's methods return values based on the timezone context.

        Note that in all cases the local machine timezone is used for
        representation if no timezone is specified.

        DateTimes may be created with from zero to seven arguments.

          - If the function is called with no arguments or with None,
            then the current date/time is returned, represented in the
            timezone of the local machine.

          - If the function is invoked with a single string argument
            which is a recognized timezone name, an object representing
            the current time is returned, represented in the specified
            timezone.

          - If the function is invoked with a single string argument
            representing a valid date/time, an object representing
            that date/time will be returned.

            As a general rule, any date-time representation that is
            recognized and unambigous to a resident of North America
            is acceptable. The reason for this qualification is that
            in North America, a date like: 2/1/1994 is interpreted
            as February 1, 1994, while in some parts of the world,
            it is interpreted as January 2, 1994.

            A date/time string consists of two components, a date
            component and an optional time component, separated by one
            or more spaces. If the time component is omited, 12:00am is
            assumed. Any recognized timezone name specified as the final
            element of the date/time string will be used for computing
            the date/time value. If you create a DateTime with the
            string 'Mar 9, 1997 1:45pm US/Pacific', the value will
            essentially be the same as if you had captured time.time()
            at the specified date and time on a machine in that timezone:

            <PRE>
            e=DateTime('US/Eastern')
            # returns current date/time, represented in US/Eastern.

            x=DateTime('1997/3/9 1:45pm')
            # returns specified time, represented in local machine zone.

            y=DateTime('Mar 9, 1997 13:45:00')
            # y is equal to x
            </PRE>

            The date component consists of year, month, and day
            values. The year value must be a one-, two-, or
            four-digit integer. If a one- or two-digit year is
            used, the year is assumed to be in the twentieth
            century. The month may be an integer, from 1 to 12, a
            month name, or a month abreviation, where a period may
            optionally follow the abreviation. The day must be an
            integer from 1 to the number of days in the month. The
            year, month, and day values may be separated by
            periods, hyphens, forward, shashes, or spaces. Extra
            spaces are permitted around the delimiters. Year,
            month, and day values may be given in any order as long
            as it is possible to distinguish the components. If all
            three components are numbers that are less than 13,
            then a a month-day-year ordering is assumed.

            The time component consists of hour, minute, and second
            values separated by colons.  The hour value must be an
            integer between 0 and 23 inclusively. The minute value
            must be an integer between 0 and 59 inclusively. The
            second value may be an integer value between 0 and
            59.999 inclusively. The second value or both the minute
            and second values may be ommitted. The time may be
            followed by am or pm in upper or lower case, in which
            case a 12-hour clock is assumed.

            New in Zope 2.4:
            The DateTime constructor automatically detects and handles
            ISO8601 compliant dates (YYYY-MM-DDThh:ss:mmTZD).

            New in Zope 2.9.6:
            The existing ISO8601 parser was extended to support almost
            the whole ISO8601 specification. New formats includes:

            <PRE>
            y=DateTime('1993-045')
            # returns the 45th day from 1993, which is 14th February

            w=DateTime('1993-W06-7')
            # returns the 7th day from the 6th week from 1993, which
            # is also 14th February
            </PRE>

            See http://en.wikipedia.org/wiki/ISO_8601 for full specs.

            Note that the Zope DateTime parser assumes timezone naive ISO
            strings to be in UTC rather than local time as specified.

          - If the DateTime function is invoked with a single Numeric
            argument, the number is assumed to be a floating point value
            such as that returned by time.time().

            A DateTime object is returned that represents the GMT value
            of the time.time() float represented in the local machine's
            timezone.

          - If the DateTime function is invoked with a single argument
            that is a DateTime instane, a copy of the passed object will
            be created.

          - New in 2.11:
            The DateTime function may now be invoked with a single argument
            that is a datetime.datetime instance. DateTimes may be converted
            back to datetime.datetime objects with asdatetime().
            DateTime instances may be converted to a timezone naive
            datetime.datetime in UTC with utcdatetime().

          - If the function is invoked with two numeric arguments, then
            the first is taken to be an integer year and the second
            argument is taken to be an offset in days from the beginning
            of the year, in the context of the local machine timezone.

            The date-time value returned is the given offset number of
            days from the beginning of the given year, represented in
            the timezone of the local machine. The offset may be positive
            or negative.

            Two-digit years are assumed to be in the twentieth
            century.

          - If the function is invoked with two arguments, the first
            a float representing a number of seconds past the epoch
            in gmt (such as those returned by time.time()) and the
            second a string naming a recognized timezone, a DateTime
            with a value of that gmt time will be returned, represented
            in the given timezone.

            <PRE>
            import time
            t=time.time()

            now_east=DateTime(t,'US/Eastern')
            # Time t represented as US/Eastern

            now_west=DateTime(t,'US/Pacific')
            # Time t represented as US/Pacific

            # now_east == now_west
            # only their representations are different
            </PRE>

          - If the function is invoked with three or more numeric
            arguments, then the first is taken to be an integer
            year, the second is taken to be an integer month, and
            the third is taken to be an integer day. If the
            combination of values is not valid, then a
            DateError is raised. Two-digit years are assumed
            to be in the twentieth century. The fourth, fifth, and
            sixth arguments specify a time in hours, minutes, and
            seconds; hours and minutes should be positive integers
            and seconds is a positive floating point value, all of
            these default to zero if not given. An optional string may
            be given as the final argument to indicate timezone (the
            effect of this is as if you had taken the value of time.time()
            at that time on a machine in the specified timezone).

            New in Zope 2.7:
            A new keyword parameter "datefmt" can be passed to the
            constructor. If set to "international", the constructor
            is forced to treat ambigious dates as "days before month
            before year". This useful if you need to parse non-US
            dates in a reliable way

        In any case that a floating point number of seconds is given
        or derived, it's rounded to the nearest millisecond.

        If a string argument passed to the DateTime constructor cannot be
        parsed, it will raise DateTime.SyntaxError. Invalid date components
        will raise a DateError, while invalid time or timezone components
        will raise a DateTimeError.

        The module function Timezones() will return a list of the (common)
        timezones recognized by the DateTime module. Recognition of
        timezone names is case-insensitive.
        """

        pass

    def localZone(self, ltm=None):
        '''Returns the time zone on the given date.  The time zone
        can change according to daylight savings.'''
        pass

    def _calcTimezoneName(self, x, ms):
        # Derive the name of the local time zone at the given
        # timezone-dependent second.
        pass

    def _parse(self, st, datefmt= None): #getDefaultDateFormat()):
        # Parse date-time components from a string
        pass

    # Internal methods
    def _validDate(self, y, m, d):
        pass

    def _validTime(self, h, m, s):
        pass

    def __getattr__(self, name):
        pass

    # Conversion and comparison methods

    def timeTime(self):
        """Return the date/time as a floating-point number in UTC,
        in the format used by the python time module.

        Note that it is possible to create date/time values with
        DateTime that have no meaningful value to the time module.
        """
        pass

    def toZone(self, z):
        """Return a DateTime with the value as the current
        object, represented in the indicated timezone.
        """
        pass

    def isFuture(self):
        """Return true if this object represents a date/time
        later than the time of the call.
        """
        pass

    def isPast(self):
        """Return true if this object represents a date/time
        earlier than the time of the call.
        """
        pass

    def isCurrentYear(self):
        """Return true if this object represents a date/time
        that falls within the current year, in the context
        of this object\'s timezone representation.
        """
        pass

    def isCurrentMonth(self):
        """Return true if this object represents a date/time
        that falls within the current month, in the context
        of this object\'s timezone representation.
        """
        pass

    def isCurrentDay(self):
        """Return true if this object represents a date/time
        that falls within the current day, in the context
        of this object\'s timezone representation.
        """
        pass

    def isCurrentHour(self):
        """Return true if this object represents a date/time
        that falls within the current hour, in the context
        of this object\'s timezone representation.
        """
        pass

    def isCurrentMinute(self):
        """Return true if this object represents a date/time
        that falls within the current minute, in the context
        of this object\'s timezone representation.
        """
        pass

    def earliestTime(self):
        """Return a new DateTime object that represents the earliest
        possible time (in whole seconds) that still falls within
        the current object\'s day, in the object\'s timezone context.
        """
        pass

    def latestTime(self):
        """Return a new DateTime object that represents the latest
        possible time (in whole seconds) that still falls within
        the current object\'s day, in the object\'s timezone context.
        """
        pass

    def greaterThan(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time greater
        than the specified DateTime or time module style time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass

    def greaterThanEqualTo(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time greater
        than or equal to the specified DateTime or time module style
        time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass

    def equalTo(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time equal to
        the specified DateTime or time module style time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass

    def notEqualTo(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time not equal
        to the specified DateTime or time module style time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass

    def __eq__(self, t):
        """Compare this DateTime object to another DateTime object.
        Return True if their internal state is the same. Two objects
        representing the same time in different timezones are regared as
        unequal. Use the equalTo method if you are only interested in them
        refering to the same moment in time.
        """
        pass

    def __ne__(self, t):
        pass

    def lessThan(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time less than
        the specified DateTime or time module style time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass


    def lessThanEqualTo(self, t):
        """Compare this DateTime object to another DateTime object
        OR a floating point number such as that which is returned
        by the python time module.

        Returns true if the object represents a date/time less than
        or equal to the specified DateTime or time module style time.

        Revised to give more correct results through comparison of
        long integer microseconds.
        """
        pass

    def isLeapYear(self):
        """Return true if the current year (in the context of the
        object\'s timezone) is a leap year.
        """
        pass

    def dayOfYear(self):
        """Return the day of the year, in context of the timezone
        representation of the object.
        """
        pass

    # Component access
    def parts(self):
        """Return a tuple containing the calendar year, month,
        day, hour, minute second and timezone of the object.
        """
        pass

    def timezone(self):
        """Return the timezone in which the object is represented."""
        pass

    def tzoffset(self):
        """Return the timezone offset for the objects timezone."""
        pass

    def year(self):
        """Return the calendar year of the object."""
        pass

    def month(self):
        """Return the month of the object as an integer."""
        pass


    def _fmon(self):
        pass

    def Month(self):
        """Return the full month name."""
        pass

    def _amon(self):
        pass

    def aMonth(self):
        """Return the abreviated month name."""
        pass

    def Mon(self):
        """Compatibility: see aMonth."""
        pass

    
    def _pmon(self):
        pass

    def pMonth(self):
        """Return the abreviated (with period) month name."""
        pass

    def Mon_(self):
        """Compatibility: see pMonth."""
        pass

    def day(self):
        """Return the integer day."""
        pass

    
    def _fday(self):
        pass

    def Day(self):
        """Return the full name of the day of the week."""
        pass

    def DayOfWeek(self):
        """Compatibility: see Day."""
        pass

    
    def _aday(self):
        pass

    def aDay(self):
        """Return the abreviated name of the day of the week."""
        pass

    
    def _pday(self):
        pass

    def pDay(self):
        """Return the abreviated (with period) name of the day of the week."""
        pass

    def Day_(self):
        """Compatibility: see pDay."""
        pass

    def dow(self):
        """Return the integer day of the week, where sunday is 0."""
        pass

    def dow_1(self):
        """Return the integer day of the week, where sunday is 1."""
        pass

    
    def _pmhour(self):
        pass

    def h_12(self):
        """Return the 12-hour clock representation of the hour."""
        pass

    def h_24(self):
        """Return the 24-hour clock representation of the hour."""
        pass

    
    def _pm(self):
        pass

    def ampm(self):
        """Return the appropriate time modifier (am or pm)."""
        pass

    def hour(self):
        """Return the 24-hour clock representation of the hour."""
        pass

    def minute(self):
        """Return the minute."""
        pass

    def second(self):
        """Return the second."""
        pass

    def millis(self):
        """Return the millisecond since the epoch in GMT."""
        pass

    def micros(self):
        """Return the microsecond since the epoch in GMT."""
        pass

    def timezoneNaive(self):
        """The python datetime module introduces the idea of distinguishing
        between timezone aware and timezone naive datetime values. For lossless
        conversion to and from datetime.datetime record if we record this
        information using True / False. DateTime makes no distinction, when we
        don't have any information we return None here.
        """
        pass

    def strftime(self, format):
        """Format the date/time using the *current timezone representation*."""
        pass

    # General formats from previous DateTime
    def Date(self):
        """Return the date string for the object."""
        pass

    def Time(self):
        """Return the time string for an object to the nearest second."""
        pass

    def TimeMinutes(self):
        """Return the time string for an object not showing seconds."""
        pass

    def AMPM(self):
        """Return the time string for an object to the nearest second."""
        pass

    def AMPMMinutes(self):
        """Return the time string for an object not showing seconds."""
        pass

    def PreciseTime(self):
        """Return the time string for the object."""
        pass

    def PreciseAMPM(self):
        """Return the time string for the object."""
        pass

    def yy(self):
        """Return calendar year as a 2 digit string."""
        pass

    def mm(self):
        """Return month as a 2 digit string."""
        pass

    def dd(self):
        """Return day as a 2 digit string."""
        pass

    def rfc822(self):
        """Return the date in RFC 822 format."""
        pass

    # New formats
    def fCommon(self):
        """Return a string representing the object\'s value
        in the format: March 1, 1997 1:45 pm.
        """
        pass

    def fCommonZ(self):
        """Return a string representing the object\'s value
        in the format: March 1, 1997 1:45 pm US/Eastern.
        """
        pass

    def aCommon(self):
        """Return a string representing the object\'s value
        in the format: Mar 1, 1997 1:45 pm.
        """
        pass

    def aCommonZ(self):
        """Return a string representing the object\'s value
        in the format: Mar 1, 1997 1:45 pm US/Eastern.
        """
        pass

    def pCommon(self):
        """Return a string representing the object\'s value
        in the format: Mar. 1, 1997 1:45 pm.
        """
        pass

    def pCommonZ(self):
        """Return a string representing the object\'s value
        in the format: Mar. 1, 1997 1:45 pm US/Eastern.
        """
        pass

    def ISO(self):
        """Return the object in ISO standard format.

        Note: this is *not* ISO 8601-format! See the ISO8601 and
        HTML4 methods below for ISO 8601-compliant output.

        Dates are output as: YYYY-MM-DD HH:MM:SS
        """
        pass

    def ISO8601(self):
        """Return the object in ISO 8601-compatible format containing the
        date, time with seconds-precision and the time zone identifier.

        See: http://www.w3.org/TR/NOTE-datetime

        Dates are output as: YYYY-MM-DDTHH:MM:SSTZD
            T is a literal character.
            TZD is Time Zone Designator, format +HH:MM or -HH:MM

        If the instance is timezone naive (it was not specified with a timezone
        when it was constructed) then the timezone is ommitted.

        The HTML4 method below offers the same formatting, but converts
        to UTC before returning the value and sets the TZD "Z".
        """
        pass

    def HTML4(self):
        """Return the object in the format used in the HTML4.0 specification,
        one of the standard forms in ISO8601.

        See: http://www.w3.org/TR/NOTE-datetime

        Dates are output as: YYYY-MM-DDTHH:MM:SSZ
           T, Z are literal characters.
           The time is in UTC.
        """
        pass

    def asdatetime(self):
        """Return a standard libary datetime.datetime
        """
        pass

    def utcdatetime(self):
        """Convert the time to UTC then return a timezone naive datetime object
        """
        pass

    def __add__(self, other):
        """A DateTime may be added to a number and a number may be
        added to a DateTime;  two DateTimes cannot be added.
        """
        pass

    def __sub__(self, other):
        """Either a DateTime or a number may be subtracted from a
        DateTime, however, a DateTime may not be subtracted from
        a number.
        """
        pass

    def __repr__(self):
        """Convert a DateTime to a string that looks like a Python
        expression.
        """
        pass

    def __str__(self):
        """Convert a DateTime to a string."""
        pass

    def __hash__(self):
        """Compute a hash value for a DateTime."""
        pass

    def __int__(self):
        """Convert to an integer number of seconds since the epoch (gmt)."""
        pass

    def __long__(self):
        """Convert to a long-int number of seconds since the epoch (gmt)."""
        pass

    def __float__(self):
        """Convert to floating-point number of seconds since the epoch (gmt).
        """
        pass

    
    def _t(self):
        pass

    def _parse_iso8601(self, s):
        # preserve the previously implied contract
        # who know where this could be used...
        pass

    def _parse_iso8601_preserving_tznaive(self, s):
        pass

    def __parse_iso8601(self, s):
        """Parse an ISO 8601 compliant date.

        See: http://en.wikipedia.org/wiki/ISO_8601
        """
        pass

    def JulianDay(self):
        """Return the Julian day.

        See: http://www.tondering.dk/claus/cal/node3.html#sec-calcjd
        """
        pass

    def week(self):
        """Return the week number according to ISO.

        See: http://www.tondering.dk/claus/cal/node6.html
        """
        pass

    def encode(self, out):
        """Encode value for XML-RPC."""
        pass

def safelocaltime(t):
    '''localtime with a safety zone.'''
    pass


class Decimal(object):
    """Floating point class for decimal arithmetic."""

    def __new__(cls, value="0", context=None):
        """Create a decimal point instance.

        >>> Decimal('3.14')              # string input
        Decimal('3.14')
        >>> Decimal((0, (3, 1, 4), -2))  # tuple (sign, digit_tuple, exponent)
        Decimal('3.14')
        >>> Decimal(314)                 # int or long
        Decimal('314')
        >>> Decimal(Decimal(314))        # another decimal instance
        Decimal('314')
        >>> Decimal('  3.14  \\n')        # leading and trailing whitespace okay
        Decimal('3.14')
        """

        # Note that the coefficient, self._int, is actually stored as
        # a string rather than as a tuple of digits.  This speeds up
        # the "digits to integer" and "integer to digits" conversions
        # that are used in almost every arithmetic operation on
        # Decimals.  This is an internal detail: the as_tuple function
        # and the Decimal constructor still deal with tuples of
        # digits.

        pass

    # @classmethod, but @decorator is not valid Python 2.3 syntax, so
    # don't use it (see notes on Py2.3 compatibility at top of file)
    @classmethod
    def from_float(cls, f):
        """Converts a float to a decimal number, exactly.

        Note that Decimal.from_float(0.1) is not the same as Decimal('0.1').
        Since 0.1 is not exactly representable in binary floating point, the
        value is stored as the nearest representable value which is
        0x1.999999999999ap-4.  The exact equivalent of the value in decimal
        is 0.1000000000000000055511151231257827021181583404541015625.

        >>> Decimal.from_float(0.1)
        Decimal('0.1000000000000000055511151231257827021181583404541015625')
        >>> Decimal.from_float(float('nan'))
        Decimal('NaN')
        >>> Decimal.from_float(float('inf'))
        Decimal('Infinity')
        >>> Decimal.from_float(-float('inf'))
        Decimal('-Infinity')
        >>> Decimal.from_float(-0.0)
        Decimal('-0')

        """
        pass

    def _isnan(self):
        """Returns whether the number is not actually one.

        0 if a number
        1 if NaN
        2 if sNaN
        """
        pass

    def _isinfinity(self):
        """Returns whether the number is infinite

        0 if finite or not a number
        1 if +INF
        -1 if -INF
        """
        pass

    def _check_nans(self, other=None, context=None):
        """Returns whether the number is not actually one.

        if self, other are sNaN, signal
        if self, other are NaN return nan
        return 0

        Done before operations.
        """

        pass

    def _compare_check_nans(self, other, context):
        """Version of _check_nans used for the signaling comparisons
        compare_signal, __le__, __lt__, __ge__, __gt__.

        Signal InvalidOperation if either self or other is a (quiet
        or signaling) NaN.  Signaling NaNs take precedence over quiet
        NaNs.

        Return 0 if neither operand is a NaN.

        """
        pass

    def __nonzero__(self):
        """Return True if self is nonzero; otherwise return False.

        NaNs and infinities are considered nonzero.
        """
        pass

    def _cmp(self, other):
        """Compare the two non-NaN decimal instances self and other.

        Returns -1 if self < other, 0 if self == other and 1
        if self > other.  This routine is for internal use only."""

        pass

    def __eq__(self, other, context=None):
        pass

    def __ne__(self, other, context=None):
        pass

    def __lt__(self, other, context=None):
        pass

    def __le__(self, other, context=None):
        pass

    def __gt__(self, other, context=None):
        pass

    def __ge__(self, other, context=None):
        pass

    def compare(self, other, context=None):
        """Compares one to another.

        -1 => a < b
        0  => a = b
        1  => a > b
        NaN => one is NaN
        Like __cmp__, but returns Decimal instances.
        """
        pass

    def __hash__(self):
        """x.__hash__() <==> hash(x)"""
        # Decimal integers must hash the same as the ints
        #
        # The hash of a nonspecial noninteger Decimal must depend only
        # on the value of that Decimal, and not on its representation.
        # For example: hash(Decimal('100E-1')) == hash(Decimal('10')).

        # Equality comparisons involving signaling nans can raise an
        # exception; since equality checks are implicitly and
        # unpredictably used when checking set and dict membership, we
        # prevent signaling nans from being used as set elements or
        # dict keys by making __hash__ raise an exception.
        pass

    def as_tuple(self):
        """Represents the number as a triple tuple.

        To show the internals exactly as they are.
        """
        pass

    def __repr__(self):
        """Represents the number as an instance of Decimal."""
        # Invariant:  eval(repr(d)) == d
        pass

    def __str__(self, eng=False, context=None):
        """Return string representation of the number in scientific notation.

        Captures all of the information in the underlying representation.
        """

        pass

    def to_eng_string(self, context=None):
        """Convert to engineering-type string.

        Engineering notation has an exponent which is a multiple of 3, so there
        are up to 3 digits left of the decimal place.

        Same rules for when in exponential and when as a value as in __str__.
        """
        pass

    def __neg__(self, context=None):
        """Returns a copy with the sign switched.

        Rounds, if it has reason.
        """
        pass

    def __pos__(self, context=None):
        """Returns a copy, unless it is a sNaN.

        Rounds the number (if more then precision digits)
        """
        pass

    def __abs__(self, round=True, context=None):
        """Returns the absolute value of self.

        If the keyword argument 'round' is false, do not round.  The
        expression self.__abs__(round=False) is equivalent to
        self.copy_abs().
        """
        pass

    def __add__(self, other, context=None):
        """Returns self + other.

        -INF + INF (or the reverse) cause InvalidOperation errors.
        """
        pass

    def __sub__(self, other, context=None):
        """Return self - other"""
        pass

    def __rsub__(self, other, context=None):
        """Return other - self"""
        pass

    def __mul__(self, other, context=None):
        """Return self * other.

        (+-) INF * 0 (or its reverse) raise InvalidOperation.
        """
        pass

    def __truediv__(self, other, context=None):
        """Return self / other."""
        pass

    def _divide(self, other, context):
        """Return (self // other, self % other), to context.prec precision.

        Assumes that neither self nor other is a NaN, that self is not
        infinite and that other is nonzero.
        """
        pass

    def __rtruediv__(self, other, context=None):
        """Swaps self/other and returns __truediv__."""
        pass

    def __divmod__(self, other, context=None):
        """
        Return (self // other, self % other)
        """
        pass

    def __rdivmod__(self, other, context=None):
        """Swaps self/other and returns __divmod__."""
        pass

    def __mod__(self, other, context=None):
        """
        self % other
        """
        pass

    def __rmod__(self, other, context=None):
        """Swaps self/other and returns __mod__."""
        pass

    def remainder_near(self, other, context=None):
        """
        Remainder nearest to 0-  abs(remainder-near) <= other/2
        """
        pass

    def __floordiv__(self, other, context=None):
        """self // other"""
        pass

    def __rfloordiv__(self, other, context=None):
        """Swaps self/other and returns __floordiv__."""
        pass

    def __float__(self):
        """Float representation."""
        pass

    def __int__(self):
        """Converts self to an int, truncating if necessary."""
        pass

    def real(self):
        pass

    def imag(self):
        pass

    def conjugate(self):
        pass

    def __complex__(self):
        pass

    def __long__(self):
        """Converts to a long.

        Equivalent to long(int(self))
        """
        pass

    def _fix_nan(self, context):
        """Decapitate the payload of a NaN to fit the context"""
        pass

    def _fix(self, context):
        """Round if it is necessary to keep self within prec precision.

        Rounds and fixes the exponent.  Does not raise on a sNaN.

        Arguments:
        self - Decimal instance
        context - context used.
        """

        pass

    def _round_down(self, prec):
        """Also known as round-towards-0, truncate."""
        pass

    def _round_up(self, prec):
        """Rounds away from 0."""
        pass

    def _round_half_up(self, prec):
        """Rounds 5 up (away from 0)"""
        pass

    def _round_half_down(self, prec):
        """Round 5 down"""
        pass

    def _round_half_even(self, prec):
        """Round 5 to even, rest to nearest."""
        pass

    def _round_ceiling(self, prec):
        """Rounds up (not away from 0 if negative.)"""
        pass

    def _round_floor(self, prec):
        """Rounds down (not towards 0 if negative)"""
        pass

    def _round_05up(self, prec):
        """Round down unless digit prec-1 is 0 or 5."""
        pass

    def fma(self, other, third, context=None):
        """Fused multiply-add.

        Returns self*other+third with no rounding of the intermediate
        product self*other.

        self and other are multiplied together, with no rounding of
        the result.  The third operand is then added to the result,
        and a single final rounding is performed.
        """

        pass

    def _power_modulo(self, other, modulo, context=None):
        """Three argument version of __pow__"""

        # if can't convert other and modulo to Decimal, raise
        # TypeError; there's no point returning NotImplemented (no
        # equivalent of __rpow__ for three argument pow)
        pass

    def _power_exact(self, other, p):
        """Attempt to compute self**other exactly.

        Given Decimals self and other and an integer p, attempt to
        compute an exact result for the power self**other, with p
        digits of precision.  Return None if self**other is not
        exactly representable in p digits.

        Assumes that elimination of special cases has already been
        performed: self and other must both be nonspecial; self must
        be positive and not numerically equal to 1; other must be
        nonzero.  For efficiency, other._exp should not be too large,
        so that 10**abs(other._exp) is a feasible calculation."""

        # In the comments below, we write x for the value of self and y for the
        # value of other.  Write x = xc*10**xe and abs(y) = yc*10**ye, with xc
        # and yc positive integers not divisible by 10.

        # The main purpose of this method is to identify the *failure*
        # of x**y to be exactly representable with as little effort as
        # possible.  So we look for cheap and easy tests that
        # eliminate the possibility of x**y being exact.  Only if all
        # these tests are passed do we go on to actually compute x**y.

        # Here's the main idea.  Express y as a rational number m/n, with m and
        # n relatively prime and n>0.  Then for x**y to be exactly
        # representable (at *any* precision), xc must be the nth power of a
        # positive integer and xe must be divisible by n.  If y is negative
        # then additionally xc must be a power of either 2 or 5, hence a power
        # of 2**n or 5**n.
        #
        # There's a limit to how small |y| can be: if y=m/n as above
        # then:
        #
        #  (1) if xc != 1 then for the result to be representable we
        #      need xc**(1/n) >= 2, and hence also xc**|y| >= 2.  So
        #      if |y| <= 1/nbits(xc) then xc < 2**nbits(xc) <=
        #      2**(1/|y|), hence xc**|y| < 2 and the result is not
        #      representable.
        #
        #  (2) if xe != 0, |xe|*(1/n) >= 1, so |xe|*|y| >= 1.  Hence if
        #      |y| < 1/|xe| then the result is not representable.
        #
        # Note that since x is not equal to 1, at least one of (1) and
        # (2) must apply.  Now |y| < 1/nbits(xc) iff |yc|*nbits(xc) <
        # 10**-ye iff len(str(|yc|*nbits(xc)) <= -ye.
        #
        # There's also a limit to how large y can be, at least if it's
        # positive: the normalized result will have coefficient xc**y,
        # so if it's representable then xc**y < 10**p, and y <
        # p/log10(xc).  Hence if y*log10(xc) >= p then the result is
        # not exactly representable.

        # if len(str(abs(yc*xe)) <= -ye then abs(yc*xe) < 10**-ye,
        # so |y| < 1/xe and the result is not representable.
        # Similarly, len(str(abs(yc)*xc_bits)) <= -ye implies |y|
        # < 1/nbits(xc).

        pass

    def __pow__(self, other, modulo=None, context=None):
        """Return self ** other [ % modulo].

        With two arguments, compute self**other.

        With three arguments, compute (self**other) % modulo.  For the
        three argument form, the following restrictions on the
        arguments hold:

         - all three arguments must be integral
         - other must be nonnegative
         - either self or other (or both) must be nonzero
         - modulo must be nonzero and must have at most p digits,
           where p is the context precision.

        If any of these restrictions is violated the InvalidOperation
        flag is raised.

        The result of pow(self, other, modulo) is identical to the
        result that would be obtained by computing (self**other) %
        modulo with unbounded precision, but is computed more
        efficiently.  It is always exact.
        """

        pass

    def __rpow__(self, other, context=None):
        """Swaps self/other and returns __pow__."""
        pass

    def normalize(self, context=None):
        """Normalize- strip trailing 0s, change anything equal to 0 to 0e0"""

        pass

    def quantize(self, exp, rounding=None, context=None, watchexp=True):
        """Quantize self so its exponent is the same as that of exp.

        Similar to self._rescale(exp._exp) but with error checking.
        """
        pass

    def same_quantum(self, other):
        """Return True if self and other have the same exponent; otherwise
        return False.

        If either operand is a special value, the following rules are used:
           * return True if both operands are infinities
           * return True if both operands are NaNs
           * otherwise, return False.
        """
        pass

    def _rescale(self, exp, rounding):
        """Rescale self so that the exponent is exp, either by padding with zeros
        or by truncating digits, using the given rounding mode.

        Specials are returned without change.  This operation is
        quiet: it raises no flags, and uses no information from the
        context.

        exp = exp to scale to (an integer)
        rounding = rounding mode
        """
        pass

    def _round(self, places, rounding):
        """Round a nonzero, nonspecial Decimal to a fixed number of
        significant figures, using the given rounding mode.

        Infinities, NaNs and zeros are returned unaltered.

        This operation is quiet: it raises no flags, and uses no
        information from the context.

        """
        pass

    def to_integral_exact(self, rounding=None, context=None):
        """Rounds to a nearby integer.

        If no rounding mode is specified, take the rounding mode from
        the context.  This method raises the Rounded and Inexact flags
        when appropriate.

        See also: to_integral_value, which does exactly the same as
        this method except that it doesn't raise Inexact or Rounded.
        """
        pass

    def to_integral_value(self, rounding=None, context=None):
        """Rounds to the nearest integer, without raising inexact, rounded."""
        pass

    def sqrt(self, context=None):
        """Return the square root of self."""
        pass

    def max(self, other, context=None):
        """Returns the larger value.

        Like max(self, other) except if one is not a number, returns
        NaN (and signals if one is sNaN).  Also rounds.
        """
        pass

    def min(self, other, context=None):
        """Returns the smaller value.

        Like min(self, other) except if one is not a number, returns
        NaN (and signals if one is sNaN).  Also rounds.
        """
        pass

    def _isinteger(self):
        """Returns whether self is an integer"""
        pass

    def _iseven(self):
        """Returns True if self is even.  Assumes self is an integer."""
        pass

    def adjusted(self):
        """Return the adjusted exponent of self"""
        pass

    def canonical(self, context=None):
        """Returns the same Decimal object.

        As we do not have different encodings for the same number, the
        received object already is in its canonical form.
        """
        pass

    def compare_signal(self, other, context=None):
        """Compares self to the other operand numerically.

        It's pretty much like compare(), but all NaNs signal, with signaling
        NaNs taking precedence over quiet NaNs.
        """
        pass

    def compare_total(self, other):
        """Compares self to other using the abstract representations.

        This is not like the standard compare, which use their numerical
        value. Note that a total ordering is defined for all possible abstract
        representations.
        """
        pass


    def compare_total_mag(self, other):
        """Compares self to other using abstract repr., ignoring sign.

        Like compare_total, but with operand's sign ignored and assumed to be 0.
        """
        pass

    def copy_abs(self):
        """Returns a copy with the sign set to 0. """
        pass

    def copy_negate(self):
        """Returns a copy with the sign inverted."""
        pass

    def copy_sign(self, other):
        """Returns self with the sign of other."""
        pass

    def exp(self, context=None):
        """Returns e ** self."""

        pass

    def is_canonical(self):
        """Return True if self is canonical; otherwise return False.

        Currently, the encoding of a Decimal instance is always
        canonical, so this method returns True for any Decimal.
        """
        pass

    def is_finite(self):
        """Return True if self is finite; otherwise return False.

        A Decimal instance is considered finite if it is neither
        infinite nor a NaN.
        """
        pass

    def is_infinite(self):
        """Return True if self is infinite; otherwise return False."""
        pass

    def is_nan(self):
        """Return True if self is a qNaN or sNaN; otherwise return False."""
        pass

    def is_normal(self, context=None):
        """Return True if self is a normal number; otherwise return False."""
        pass

    def is_qnan(self):
        """Return True if self is a quiet NaN; otherwise return False."""
        pass

    def is_signed(self):
        """Return True if self is negative; otherwise return False."""
        pass

    def is_snan(self):
        """Return True if self is a signaling NaN; otherwise return False."""
        pass

    def is_subnormal(self, context=None):
        """Return True if self is subnormal; otherwise return False."""
        pass

    def is_zero(self):
        """Return True if self is a zero; otherwise return False."""
        pass

    def _ln_exp_bound(self):
        """Compute a lower bound for the adjusted exponent of self.ln().
        In other words, compute r such that self.ln() >= 10**r.  Assumes
        that self is finite and positive and that self != 1.
        """

        pass


    def ln(self, context=None):
        """Returns the natural (base e) logarithm of self."""
        pass

    def _log10_exp_bound(self):
        """Compute a lower bound for the adjusted exponent of self.log10().
        In other words, find r such that self.log10() >= 10**r.
        Assumes that self is finite and positive and that self != 1.
        """

        pass

    def log10(self, context=None):
        """Returns the base 10 logarithm of self."""

        pass

    def logb(self, context=None):
        """ Returns the exponent of the magnitude of self's MSD.

        The result is the integer which is the exponent of the magnitude
        of the most significant digit of self (as though it were truncated
        to a single digit while maintaining the value of that digit and
        without limiting the resulting exponent).
        """
        pass

    def _islogical(self):
        """Return True if self is a logical operand.

        For being logical, it must be a finite number with a sign of 0,
        an exponent of 0, and a coefficient whose digits must all be
        either 0 or 1.
        """
        pass

    def _fill_logical(self, context, opa, opb):
        pass

    def logical_and(self, other, context=None):
        """Applies an 'and' operation between self and other's digits."""
        pass

    def logical_invert(self, context=None):
        """Invert all its digits."""
        pass

    def logical_or(self, other, context=None):
        """Applies an 'or' operation between self and other's digits."""
        pass

    def logical_xor(self, other, context=None):
        """Applies an 'xor' operation between self and other's digits."""
        pass

    def max_mag(self, other, context=None):
        """Compares the values numerically with their sign ignored."""
        pass

    def min_mag(self, other, context=None):
        """Compares the values numerically with their sign ignored."""
        pass

    def next_minus(self, context=None):
        """Returns the largest representable number smaller than itself."""
        pass

    def next_plus(self, context=None):
        """Returns the smallest representable number larger than itself."""
        pass

    def next_toward(self, other, context=None):
        """Returns the number closest to self, in the direction towards other.

        The result is the closest representable number to self
        (excluding self) that is in the direction towards other,
        unless both have the same value.  If the two operands are
        numerically equal, then the result is a copy of self with the
        sign set to be the same as the sign of other.
        """
        pass

    def number_class(self, context=None):
        """Returns an indication of the class of self.

        The class is one of the following strings:
          sNaN
          NaN
          -Infinity
          -Normal
          -Subnormal
          -Zero
          +Zero
          +Subnormal
          +Normal
          +Infinity
        """
        pass

    def radix(self):
        """Just returns 10, as this is Decimal, :)"""
        pass

    def rotate(self, other, context=None):
        """Returns a rotated copy of self, value-of-other times."""
        pass

    def scaleb(self, other, context=None):
        """Returns self operand after adding the second value to its exp."""
        pass

    def shift(self, other, context=None):
        """Returns a shifted copy of self, value-of-other times."""
        pass

    # Support for pickling, copy, and deepcopy
    def __reduce__(self):
        pass

    def __copy__(self):
        pass

    def __deepcopy__(self, memo):
        pass

    # PEP 3101 support.  the _localeconv keyword argument should be
    # considered private: it's provided for ease of testing only.
    def __format__(self, specifier, context=None, _localeconv=None):
        """Format a Decimal instance according to the given specifier.

        The specifier should be a standard format specifier, with the
        form described in PEP 3101.  Formatting types 'e', 'E', 'f',
        'F', 'g', 'G', 'n' and '%' are supported.  If the formatting
        type is omitted it defaults to 'g' or 'G', depending on the
        value of context.capitals.
        """

        # Note: PEP 3101 says that if the type is not present then
        # there should be at least one digit after the decimal point.
        # We take the liberty of ignoring this requirement for
        # Decimal---it's presumably there to make sure that
        # format(float, '') behaves similarly to str(float).
        pass

def DocFileSuite(*paths, **kw):
    """A unittest suite for one or more doctest files.

    The path to each doctest file is given as a string; the
    interpretation of that string depends on the keyword argument
    "module_relative".

    A number of options may be provided as keyword arguments:

    module_relative
      If "module_relative" is True, then the given file paths are
      interpreted as os-independent module-relative paths.  By
      default, these paths are relative to the calling module's
      directory; but if the "package" argument is specified, then
      they are relative to that package.  To ensure os-independence,
      "filename" should use "/" characters to separate path
      segments, and may not be an absolute path (i.e., it may not
      begin with "/").

      If "module_relative" is False, then the given file paths are
      interpreted as os-specific paths.  These paths may be absolute
      or relative (to the current working directory).

    package
      A Python package or the name of a Python package whose directory
      should be used as the base directory for module relative paths.
      If "package" is not specified, then the calling module's
      directory is used as the base directory for module relative
      filenames.  It is an error to specify "package" if
      "module_relative" is False.

    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.

    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.

    globs
      A dictionary containing initial global variables for the tests.

    optionflags
      A set of doctest option flags expressed as an integer.

    parser
      A DocTestParser (or subclass) that should be used to extract
      tests from the files.

    encoding
      An encoding that will be used to convert the files to unicode.
    """
    pass

def DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None,
                 **options):
    """
    Convert doctest tests for a module to a unittest test suite.

    This converts each documentation string in a module that
    contains doctest tests to a unittest test case.  If any of the
    tests in a doc string fail, then the test case fails.  An exception
    is raised showing the name of the file containing the test and a
    (sometimes approximate) line number.

    The `module` argument provides the module to be tested.  The argument
    can be either a module or a module name.

    If no argument is given, the calling module is used.

    A number of options may be provided as keyword arguments:

    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.

    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.

    globs
      A dictionary containing initial global variables for the tests.

    optionflags
       A set of doctest option flags expressed as an integer.
    """

    pass

def glob(pathname):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    """
    pass

def plot(data, gnuplotpath=None, plotscriptfile=None, plotscript=None, usefifo=True):
    """
    Feeds data and plotting instructions to GNUplot, returns GNUplot output (hopefully, a graph).
    """

    pass

class MagnitudeError(Exception):
    pass


class IOrderedContainer(Interface):

    """ Ordered Container interface.

    This interface provides a common mechanism for maintaining ordered
    collections.
    """
    @staticmethod
    def moveObjectsByDelta(ids, delta, subset_ids=None):
        """ Move specified sub-objects by delta.

        If delta is higher than the possible maximum, objects will be moved to
        the bottom. If delta is lower than the possible minimum, objects will
        be moved to the top.

        If subset_ids is not None, delta will be interpreted relative to the
        subset specified by a sequence of ids. The position of objects that
        are not part of this subset will not be changed.

        The order of the objects specified by ids will always be preserved. So
        if you don't want to change their original order, make sure the order
        of ids corresponds to their original order.

        If an object with id doesn't exist an error will be raised.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def moveObjectsUp(ids, delta=1, subset_ids=None):
        """ Move specified sub-objects up by delta in container.

        If no delta is specified, delta is 1. See moveObjectsByDelta for more
        details.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def moveObjectsDown(ids, delta=1, subset_ids=None):
        """ Move specified sub-objects down by delta in container.

        If no delta is specified, delta is 1. See moveObjectsByDelta for more
        details.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def moveObjectsToTop(ids, subset_ids=None):
        """ Move specified sub-objects to top of container.

        See moveObjectsByDelta for more details.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def moveObjectsToBottom(ids, subset_ids=None):
        """ Move specified sub-objects to bottom of container.

        See moveObjectsByDelta for more details.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def orderObjects(key, reverse=None):
        """ Order sub-objects by key and direction.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass
    @staticmethod
    def getObjectPosition(id):
        """ Get the position of an object by its id.

        Permission -- Access contents information

        Returns -- Position
        """
        pass
    @staticmethod
    def moveObjectToPosition(id, position):
        """ Move specified object to absolute position.

        Permission -- Manage properties

        Returns -- Number of moved sub-objects
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.CopySupport.CopySource
class ICopySource(Interface):

    """Interface for objects which allow themselves to be copied."""
    @staticmethod
    def _canCopy(op=0):
        """Called to make sure this object is copyable.

        The op var is 0 for a copy, 1 for a move.
        """
        pass
    @staticmethod
    def _notifyOfCopyTo(container, op=0):
        """Overide this to be pickly about where you go!

        If you dont want to go there, raise an exception. The op variable is 0
        for a copy, 1 for a move.
        """
        pass
    @staticmethod
    def _getCopy(container):
        """
        """
        pass
    @staticmethod
    def _postCopy(container, op=0):
        """Called after the copy is finished to accomodate special cases.
        The op var is 0 for a copy, 1 for a move.
        """
        pass
    @staticmethod
    def _setId(id):
        """Called to set the new id of a copied object.
        """
        pass
    @staticmethod
    def cb_isCopyable():
        """Is object copyable? Returns 0 or 1
        """
        pass
    @staticmethod
    def cb_isMoveable():
        """Is object moveable? Returns 0 or 1
        """
        pass
    @staticmethod
    def cb_userHasCopyOrMovePermission():
        """
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.FTPInterface.FTPInterface
class IFTPAccess(Interface):

    """Provide support for FTP access"""
    @staticmethod
    def manage_FTPstat(REQUEST):
        """Returns a stat-like tuple. (marshalled to a string) Used by
        FTP for directory listings, and MDTM and SIZE"""
        pass
    @staticmethod
    def manage_FTPlist(REQUEST):
        """Returns a directory listing consisting of a tuple of
        (id,stat) tuples, marshaled to a string. Note, the listing it
        should include '..' if there is a Folder above the current
        one.

        In the case of non-foldoid objects it should return a single
        tuple (id,stat) representing itself."""
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.Traversable.Traversable
class ITraversable(Interface):
    @staticmethod
    def absolute_url(relative=0):
        """Return the absolute URL of the object.

        This a canonical URL based on the object's physical
        containment path.  It is affected by the virtual host
        configuration, if any, and can be used by external
        agents, such as a browser, to address the object.

        If the relative argument is provided, with a true value, then
        the value of virtual_url_path() is returned.

        Some Products incorrectly use '/'+absolute_url(1) as an
        absolute-path reference.  This breaks in certain virtual
        hosting situations, and should be changed to use
        absolute_url_path() instead.
        """
    @staticmethod
    def absolute_url_path():
        """Return the path portion of the absolute URL of the object.

        This includes the leading slash, and can be used as an
        'absolute-path reference' as defined in RFC 2396.
        """
        pass
    @staticmethod
    def virtual_url_path():
        """Return a URL for the object, relative to the site root.

        If a virtual host is configured, the URL is a path relative to
        the virtual host's root object.  Otherwise, it is the physical
        path.  In either case, the URL does not begin with a slash.
        """
        pass
    @staticmethod
    def getPhysicalPath():
        """Get the physical path of the object.

        Returns a path (an immutable sequence of strings) that can be used to
        access this object again later, for example in a copy/paste operation.
        getPhysicalRoot() and getPhysicalPath() are designed to operate
        together.
        """
        pass
    @staticmethod
    def unrestrictedTraverse(path, default=None, restricted=0):
        """Lookup an object by path.

        path -- The path to the object. May be a sequence of strings or a slash
        separated string. If the path begins with an empty path element
        (i.e., an empty string or a slash) then the lookup is performed
        from the application root. Otherwise, the lookup is relative to
        self. Two dots (..) as a path element indicates an upward traversal
        to the acquisition parent.

        default -- If provided, this is the value returned if the path cannot
        be traversed for any reason (i.e., no object exists at that path or
        the object is inaccessible).

        restricted -- If false (default) then no security checking is performed.
        If true, then all of the objects along the path are validated with
        the security machinery. Usually invoked using restrictedTraverse().
        """
        pass
    @staticmethod
    def restrictedTraverse(path, default=None):
        """Trusted code traversal code, always enforces security.
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on many classes
class IZopeObject(Interface):

    pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.SimpleItem.Item and App.Management.Tabs
class IManageable(Interface):

    """Something that is manageable in the ZMI"""

    @staticmethod
    def manage(URL1):
        """Show management screen"""
        pass
    @staticmethod
    def manage_afterAdd(item, container):
        """Gets called after being added to a container"""
        pass
    @staticmethod
    def manage_beforeDelete(item, container):
        """Gets called before being deleted"""
        pass
    @staticmethod
    def manage_afterClone(item):
        """Gets called after being cloned"""
        pass
    @staticmethod
    def filtered_manage_options(REQUEST=None):
        """
        """
        pass
    @staticmethod
    def manage_workspace(REQUEST):
        """Dispatch to first interface in manage_options
        """
        pass
    @staticmethod
    def tabs_path_default(REQUEST):
        """
        """
        pass
    @staticmethod
    def tabs_path_info(script, path):
        """
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.SimpleItem.Item
class IItem : #(IZopeObject, IManageable, IFTPAccess, IDAVResource,
    #ICopySource, ITraversable, IOwned, IUndoSupport):

    @staticmethod
    def getId():
        """Return the id of the object as a string.

        This method should be used in preference to accessing an id
        attribute of an object directly. The getId method is public.
        """
        pass
    @staticmethod
    def title_or_id():
        """Return the title if it is not blank and the id otherwise.
        """
        pass
    @staticmethod
    def title_and_id():
        """Return the title if it is not blank and the id otherwise.

        If the title is not blank, then the id is included in parens.
        """
        pass
    @staticmethod
    def manage_editedDialog(REQUEST, **args):
        """Show an 'edited' dialog.
        """
        pass
    @staticmethod
    def raise_standardErrorMessage(client=None, REQUEST={},
                                   error_type=None, error_value=None, tb=None,
                                   error_tb=None, error_message='',
                                   tagSearch=None, error_log_url=''):
        """Raise standard error message.
        """
        pass


# XXX: based on OFS.SimpleItem.Item_w__name__
class IItemWithName(IItem):

    """Item with name.
    """
    pass


# XXX: based on OFS.SimpleItem.SimpleItem
class ISimpleItem: # (IItem, IPersistent, IAcquirer, IRoleManager):

    """Not-so-simple item.
    """
    pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.CopySupport.CopyContainer
class ICopyContainer(Interface):

    """Interface for containerish objects which allow cut/copy/paste"""

    # The following three methods should be overridden to store sub-objects
    # as non-attributes.
    @staticmethod
    def _setOb(id, object):
        """
        """
        pass
    @staticmethod
    def _delOb(id):
        """
        """
        pass
    @staticmethod
    def _getOb(id, default=None):
        """
        """
        pass
    @staticmethod
    def manage_CopyContainerFirstItem(REQUEST):
        """
        """
        pass
    @staticmethod
    def manage_CopyContainerAllItems(REQUEST):
        """
        """
        pass
    @staticmethod
    def manage_cutObjects(ids=None, REQUEST=None):
        """Put a reference to the objects named in ids in the clip board"""
        pass
    @staticmethod
    def manage_copyObjects(ids=None, REQUEST=None, RESPONSE=None):
        """Put a reference to the objects named in ids in the clip board"""
        pass
    @staticmethod
    def _get_id(id):
        """Allow containers to override the generation of object copy id by
        attempting to call its _get_id method, if it exists.
        """
        pass
    @staticmethod
    def manage_pasteObjects(cb_copy_data=None, REQUEST=None):
        """Paste previously copied objects into the current object.

        If calling manage_pasteObjects from python code, pass the result of a
        previous call to manage_cutObjects or manage_copyObjects as the first
        argument.
        """
        pass

    @staticmethod
    def manage_renameObjects(ids=[], new_ids=[], REQUEST=None):
        """Rename several sub-objects"""
        pass
    @staticmethod
    def manage_renameObject(id, new_id, REQUEST=None):
        """Rename a particular sub-object"""
        pass
    @staticmethod
    def manage_clone(ob, id, REQUEST=None):
        """Clone an object, creating a new object with the given id.
        """
        pass
    @staticmethod
    def cb_dataValid():
        """Return true if clipboard data seems valid.
        """
        pass
    @staticmethod
    def cb_dataItems():
        """List of objects in the clip board.
        """
        pass
    @staticmethod
    def _verifyObjectPaste(object, validate_src=1):
        """Verify whether the current user is allowed to paste the passed
        object into self. This is determined by checking to see if the
        user could create a new object of the same meta_type of the
        object passed in and checking that the user actually is
        allowed to access the passed in object in its existing
        context.

        Passing a false value for the validate_src argument will skip
        checking the passed in object in its existing context. This is
        mainly useful for situations where the passed in object has no
        existing context, such as checking an object during an import
        (the object will not yet have been connected to the
        acquisition hierarchy).
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.ObjectManager.ObjectManager
class IObjectManager: #(IZopeObject, ICopyContainer, INavigation, IManageable,
#                      IAcquirer, IPersistent, IDAVCollection, ITraversable,
#                      IPossibleSite, IContainer):
    """Generic object manager

    This interface provides core behavior for collections of heterogeneous
    objects."""

    @staticmethod
    def all_meta_types(interfaces=None):
        """
        """
        pass
    @staticmethod
    def _subobject_permissions():
        """
        """
        pass
    @staticmethod
    def filtered_meta_types(user=None):
        """Return a list of the types for which the user has adequate
        permission to add that type of object.
        """
        pass
    @staticmethod
    def _setOb(id, object):
        """
        """
        pass
    @staticmethod
    def _delOb(id):
        """
        """
        pass
    @staticmethod
    def _getOb(id, default=None):
        """
        """
        pass
    @staticmethod
    def _setObject(id, object, roles=None, user=None, set_owner=1):
        """
        """
        pass
    @staticmethod
    def _delObject(id, dp=1):
        """
        """
        pass
    @staticmethod
    def hasObject(id):
        """Indicate whether the folder has an item by ID.
        """
        pass
    @staticmethod
    def objectIds(spec=None):
        """List the IDs of the subobjects of the current object.

        If 'spec' is specified, returns only objects whose meta_types match
        'spec'.
        """
        pass
    @staticmethod
    def objectValues(spec=None):
        """List the subobjects of the current object.

        If 'spec' is specified, returns only objects whose meta_types match
        'spec'.
        """
        pass
    @staticmethod
    def objectItems(spec=None):
        """List (ID, subobject) tuples for subobjects of the current object.

        If 'spec' is specified, returns only objects whose meta_types match
        'spec'.
        """
        pass
    @staticmethod
    def objectMap():
        """Return a tuple of mappings containing subobject meta-data.
        """
        pass
    @staticmethod
    def superValues(t):
        """Return all of the objects of a given type located in this object
        and containing objects.
        """
        pass
    @staticmethod
    def manage_delObjects(ids=[], REQUEST=None):
        """Delete a subordinate object

        The objects specified in 'ids' get deleted.
        """
        pass
    @staticmethod
    def tpValues():
        """Return a list of subobjects, used by tree tag.
        """
        pass
    @staticmethod
    def manage_exportObject(id='', download=None, toxml=None,
                            RESPONSE=None,REQUEST=None):
        """Exports an object to a file and returns that file."""
        pass
    @staticmethod
    def manage_importObject(file, REQUEST=None, set_owner=1):
        """Import an object from a file"""
        pass
    @staticmethod
    def _importObjectFromFile(filepath, verify=1, set_owner=1):
        """
        """
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.FindSupport.FindSupport
class IFindSupport(Interface):

    """Find support for Zope Folders"""

    @staticmethod
    def ZopeFind(obj, obj_ids=None, obj_metatypes=None,
                 obj_searchterm=None, obj_expr=None,
                 obj_mtime=None, obj_mspec=None,
                 obj_permission=None, obj_roles=None,
                 search_sub=0,
                 REQUEST=None, result=None, pre=''):
        """Zope Find interface"""
        pass

    
    @staticmethod
    def ZopeFindAndApply(obj, obj_ids=None, obj_metatypes=None,
                         obj_searchterm=None, obj_expr=None,
                         obj_mtime=None, obj_mspec=None,
                         obj_permission=None, obj_roles=None,
                         search_sub=0,
                         REQUEST=None, result=None, pre='',
                         apply_func=None, apply_path=''):
        """Zope Find interface and apply"""
        pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.PropertyManager.PropertyManager
class IPropertyManager(Interface):

    """
    The PropertyManager mixin class provides an object with
    transparent property management. An object which wants to
    have properties should inherit from PropertyManager.

    An object may specify that it has one or more predefined
    properties, by specifying an _properties structure in its
    class::

      _properties=({'id':'title', 'type': 'string', 'mode': 'w'},
                   {'id':'color', 'type': 'string', 'mode': 'w'},
                   )

    The _properties structure is a sequence of dictionaries, where
    each dictionary represents a predefined property. Note that if a
    predefined property is defined in the _properties structure, you
    must provide an attribute with that name in your class or instance
    that contains the default value of the predefined property.

    Each entry in the _properties structure must have at least an 'id'
    and a 'type' key. The 'id' key contains the name of the property,
    and the 'type' key contains a string representing the object's type.
    The 'type' string must be one of the values: 'float', 'int', 'long',
    'string', 'lines', 'text', 'date', 'tokens', 'selection', or
    'multiple section'.

    For 'selection' and 'multiple selection' properties, there is an
    addition item in the property dictionay, 'select_variable' which
    provides the name of a property or method which returns a list of
    strings from which the selection(s) can be chosen.

    Each entry in the _properties structure may *optionally* provide a
    'mode' key, which specifies the mutability of the property. The 'mode'
    string, if present, must contain 0 or more characters from the set
    'w','d'.

    A 'w' present in the mode string indicates that the value of the
    property may be changed by the user. A 'd' indicates that the user
    can delete the property. An empty mode string indicates that the
    property and its value may be shown in property listings, but that
    it is read-only and may not be deleted.

    Entries in the _properties structure which do not have a 'mode' key
    are assumed to have the mode 'wd' (writeable and deleteable).

    To fully support property management, including the system-provided
    tabs and user interfaces for working with properties, an object which
    inherits from PropertyManager should include the following entry in
    its manage_options structure::

      {'label':'Properties', 'action':'manage_propertiesForm',}

    to ensure that a 'Properties' tab is displayed in its management
    interface. Objects that inherit from PropertyManager should also
    include the following entry in its __ac_permissions__ structure::

      ('Manage properties', ('manage_addProperty',
                             'manage_editProperties',
                             'manage_delProperties',
                             'manage_changeProperties',)),
    """
    @staticmethod
    def valid_property_id(id):
        """
        """
        pass
    @staticmethod
    def hasProperty(id):
        """Return true if object has a property 'id'.
        """
        pass
    @staticmethod
    def getProperty(id, d=None):
        """Get the property 'id'.

        Returns the optional second argument or None if no such property is
        found.
        """
        pass
    @staticmethod
    def getPropertyType(id):
        """Get the type of property 'id'.

        Returns None if no such property exists.
        """
        pass
    @staticmethod
    def _wrapperCheck(object):
        """Raise an error if an object is wrapped.
        """
        pass
    @staticmethod
    def _setPropValue(id, value):
        """
        """
        pass
    @staticmethod
    def _delPropValue(id):
        """
        """
        pass
    @staticmethod
    def _setProperty(id, value, type='string'):
        """Set property.

        For selection and multiple selection properties the value argument
        indicates the select variable of the property.
        """
        pass
    @staticmethod
    def _updateProperty(id, value):
        """Update the value of an existing property.

        If value is a string, an attempt will be made to convert the value to
        the type of the existing property.
        """
        pass
    @staticmethod
    def _delProperty(id):
        """
        """
        pass
    @staticmethod
    def propertyIds():
        """Return a list of property ids.
        """
        pass
    @staticmethod
    def propertyValues():
        """Return a list of actual property objects.
        """
        pass
    @staticmethod
    def propertyItems():
        """Return a list of (id,property) tuples.
        """
        pass
    @staticmethod
    def _propertyMap():
        """Return a tuple of mappings, giving meta-data for properties.
        """
        pass
    @staticmethod
    def propertyMap():
        """Return a tuple of mappings, giving meta-data for properties.

        Return copies of the real definitions for security.
        """
        pass
    @staticmethod
    def propertyLabel(id):
        """Return a label for the given property id
        """
        pass
    @staticmethod
    def propdict():
        """
        """
        pass

    # Web interface
    @staticmethod
    def manage_addProperty(id, value, type, REQUEST=None):
        """Add a new property via the web.

        Sets a new property with the given id, type, and value.
        """
        pass
    @staticmethod
    def manage_editProperties(REQUEST):
        """Edit object properties via the web.

        The purpose of this method is to change all property values,
        even those not listed in REQUEST; otherwise checkboxes that
        get turned off will be ignored.  Use manage_changeProperties()
        instead for most situations.
        """
        pass
    @staticmethod
    def manage_changeProperties(REQUEST=None, **kw):
        """Change existing object properties.

        Change object properties by passing either a REQUEST object or
        name=value parameters
        """
        pass
    @staticmethod
    def manage_changePropertyTypes(old_ids, props, REQUEST=None):
        """Replace one set of properties with another

        Delete all properties that have ids in old_ids, then add a
        property for each item in props.  Each item has a new_id,
        new_value, and new_type.  The type of new_value should match
        new_type.
        """
        pass
    @staticmethod
    def manage_delProperties(ids=None, REQUEST=None):
        """Delete one or more properties specified by 'ids'."""
        pass


# XXX: based on OFS.Folder.Folder
class IFolder: #(IObjectManager, IPropertyManager, IRoleManager,
#               IDAVCollection, IItem, IFindSupport):

    """Folders are basic container objects that provide a standard
    interface for object management. Folder objects also implement a
    management interface and can have arbitrary properties.
    """
    pass


# XXX: based on OFS.OrderedFolder.OrderedFolder
class IOrderedFolder(IOrderedContainer, IFolder):

    """Ordered folder.
    """
    pass


# XXX: might contain non-API methods and outdated comments;
#      not synced with ZopeBook API Reference;
#      based on OFS.Application.Application
class IApplication: #(IFolder, IRoot):

    """Top-level system object"""

    @staticmethod
    def PrincipiaRedirect(destination, URL1):
        """Utility function to allow user-controlled redirects"""
        pass

    @staticmethod
    def __bobo_traverse__(REQUEST, name=None):
        """Bobo traverse.
        """
        pass
    @staticmethod
    def PrincipiaTime(*args):
        """Utility function to return current date/time"""
        pass

    @staticmethod
    def ZopeAttributionButton():
        """Returns an HTML fragment that displays the 'powered by zope'
        button along with a link to the Zope site."""
        pass

    @staticmethod
    def absolute_url(relative=0):
        """The absolute URL of the root object is BASE1 or "/".
        """
        pass
    
    @staticmethod
    def absolute_url_path():
        """The absolute URL path of the root object is BASEPATH1 or "/".
        """
        pass

    @staticmethod
    def virtual_url_path():
        """The virtual URL path of the root object is empty.
        """
        pass

    @staticmethod
    def getPhysicalRoot():
        """
        """
        pass


class IObjectWillBeMovedEvent: #(IObjectEvent):
    """An object will be moved."""
    pass

class IObjectWillBeAddedEvent(IObjectWillBeMovedEvent):
    """An object will be added to a container."""
    pass

class IObjectWillBeRemovedEvent(IObjectWillBeMovedEvent):
    """An object will be removed from a container"""
    pass

class IObjectClonedEvent: #(IObjectEvent):
    """An object has been cloned (a la Zope 2).

    This is for Zope 2 compatibility, subscribers should really use
    IObjectCopiedEvent or IObjectAddedEvent, depending on their use
    cases.

    event.object is the copied object, already added to its container.
    Note that this event is dispatched to all sublocations.
    """
    pass

class SimpleItem: #(Item,
#                  Persistent,
#                  Implicit,
#                  RoleManager,
#                  ):

    # Blue-plate special, Zope Masala
    """Mix-in class combining the most common set of basic mix-ins
    """

    pass

def load_workbook(filename, use_iterators=False):
    """Open the given filename and return the workbook

    :param filename: the path to open or a file-like object
    :type filename: string or a file-like object open in binary mode c.f., :class:`zipfile.ZipFile`

    :param use_iterators: use lazy load for cells
    :type use_iterators: bool

    :rtype: :class:`openpyxl.workbook.Workbook`

    .. note::

        When using lazy load, all worksheets will be :class:`openpyxl.reader.iter_worksheet.IterableWorksheet`
        and the returned workbook will be read-only.

    """

    pass

def join(a, *p):
    """Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator."""
    pass

def _declare_state(vartype, **kw):
    pass

def __getstate__():
    pass

def __setstate__(state):
    pass

def _sget_dict(val):
    pass

def _sset_dict(key, ob, state):
    pass

def _sget_object(val):
    pass

def _sset_object(key, ob, state):
    pass


def get_supported_platform():
    """Return this platform's maximum compatible version.

    distutils.util.get_platform() normally reports the minimum version
    of Mac OS X that would be required to *use* extensions produced by
    distutils.  But what we want when checking compatibility is to know the
    version of Mac OS X that we are *running*.  To allow usage of packages that
    explicitly require a newer version of Mac OS X, we must also know the
    current version of the OS.

    If this condition occurs for any other platform with a version in its
    platform strings, this function should be extended accordingly.
    """
    pass

class ResolutionError(Exception):
    """Abstract base for dependency resolution errors"""
    def __repr__(self):
        pass

class VersionConflict(ResolutionError):
    """An already-installed version conflicts with the requested version"""
    pass

class DistributionNotFound(ResolutionError):
    """A requested distribution was not found"""
    pass

class UnknownExtra(ResolutionError):
    """Distribution doesn't have an "extra feature" of the given name"""
    pass



def register_loader_type(loader_type, provider_factory):
    """Register `provider_factory` to make providers for `loader_type`

    `loader_type` is the type or class of a PEP 302 ``module.__loader__``,
    and `provider_factory` is a function that, passed a *module* object,
    returns an ``IResourceProvider`` for that module.
    """
    pass

def get_provider(moduleOrReq):
    """Return an IResourceProvider for the named module or requirement"""
    pass

def _macosx_vers(_cache=[]):
    pass

def _macosx_arch(machine):
    pass

def get_build_platform():
    """Return this platform's string for platform-specific distributions

    XXX Currently this is the same as ``distutils.util.get_platform()``, but it
    needs some hacks for Linux and Mac OS X.
    """
    pass


def compatible_platforms(provided, required):
    """Can code for the `provided` platform run on the `required` platform?

    Returns true if either platform is ``None``, or the platforms are equal.

    XXX Needs compatibility checks for Linux and other unixy OSes.
    """
    pass


def run_script(dist_spec, script_name):
    """Locate distribution `dist_spec` and run its `script_name` script"""
    pass

# backward compatibility


def get_distribution(dist):
    """Return a current distribution object for a Requirement or string"""
    pass

def load_entry_point(dist, group, name):
    """Return `name` entry point of `group` for `dist` or raise ImportError"""
    pass

def get_entry_map(dist, group=None):
    """Return the entry point map for `group`, or the full entry map"""
    pass

def get_entry_info(dist, group, name):
    """Return the EntryPoint object for `group`+`name`, or ``None``"""
    pass


class IMetadataProvider:
    @staticmethod
    def has_metadata(name):
        """Does the package's distribution contain the named metadata?"""
        pass

    @staticmethod
    def get_metadata(name):
        """The named metadata resource as a string"""
        pass

    @staticmethod
    def get_metadata_lines(name):
        """Yield named metadata resource as list of non-blank non-comment lines
        Leading and trailing whitespace is stripped from each line, and lines
        with ``#`` as the first non-blank character are omitted."""
        pass

    @staticmethod
    def metadata_isdir(name):
        """Is the named metadata a directory?  (like ``os.path.isdir()``)"""
        pass

    @staticmethod
    def metadata_listdir(name):
        """List of metadata names in the directory (like ``os.listdir()``)"""
        pass

    @staticmethod
    def run_script(script_name, namespace):
        """Execute the named script in the supplied namespace dictionary"""
        pass


class IResourceProvider(IMetadataProvider):
    """An object that provides access to package resources"""
    @staticmethod
    def get_resource_filename(manager, resource_name):
        """Return a true filesystem path for `resource_name`

        `manager` must be an ``IResourceManager``"""
        pass

    @staticmethod
    def get_resource_stream(manager, resource_name):
        """Return a readable file-like object for `resource_name`

        `manager` must be an ``IResourceManager``"""
        pass

    @staticmethod
    def get_resource_string(manager, resource_name):
        """Return a string containing the contents of `resource_name`

        `manager` must be an ``IResourceManager``"""
        pass

    @staticmethod
    def has_resource(resource_name):
        """Does the package contain the named resource?"""
        pass

    @staticmethod
    def resource_isdir(resource_name):
        """Is the named resource a directory?  (like ``os.path.isdir()``)"""
        pass

    @staticmethod
    def resource_listdir(resource_name):
        """List of resource names in the directory (like ``os.listdir()``)"""
        pass

class WorkingSet(object):
    """A collection of active distributions on sys.path (or a similar list)"""

    def __init__(self, entries=None):
        """Create working set from list of path entries (default=sys.path)"""
        pass
    @classmethod
    def _build_master(cls):
        """
        Prepare the master working set.
        """
        pass
    
    @classmethod
    def _build_from_requirements(cls, req_spec):
        """
        Build a working set from a requirement spec. Rewrites sys.path.
        """
        pass

    def add_entry(self, entry):
        """Add a path item to ``.entries``, finding any distributions on it

        ``find_distributions(entry, True)`` is used to find distributions
        corresponding to the path entry, and they are added.  `entry` is
        always appended to ``.entries``, even if it is already present.
        (This is because ``sys.path`` can contain the same value more than
        once, and the ``.entries`` of the ``sys.path`` WorkingSet should always
        equal ``sys.path``.)
        """
        pass

    def __contains__(self, dist):
        """True if `dist` is the active distribution for its project"""
        pass

    def find(self, req):
        """Find a distribution matching requirement `req`

        If there is an active distribution for the requested project, this
        returns it as long as it meets the version requirement specified by
        `req`.  But, if there is an active distribution for the project and it
        does *not* meet the `req` requirement, ``VersionConflict`` is raised.
        If there is no active distribution for the requested project, ``None``
        is returned.
        """
        pass

    def iter_entry_points(self, group, name=None):
        """Yield entry point objects from `group` matching `name`

        If `name` is None, yields all entry points in `group` from all
        distributions in the working set, otherwise only ones matching
        both `group` and `name` are yielded (in distribution order).
        """
        pass

    def run_script(self, requires, script_name):
        """Locate distribution for `requires` and run `script_name` script"""
        pass

    def __iter__(self):
        """Yield distributions for non-duplicate projects in the working set

        The yield order is the order in which the items' path entries were
        added to the working set.
        """
        pass

    def add(self, dist, entry=None, insert=True, replace=False):
        """Add `dist` to working set, associated with `entry`

        If `entry` is unspecified, it defaults to the ``.location`` of `dist`.
        On exit from this routine, `entry` is added to the end of the working
        set's ``.entries`` (if it wasn't already present).

        `dist` is only added to the working set if it's for a project that
        doesn't already have a distribution in the set, unless `replace=True`.
        If it's added, any callbacks registered with the ``subscribe()`` method
        will be called.
        """
        pass

    def resolve(self, requirements, env=None, installer=None,
            replace_conflicting=False):
        """List all distributions needed to (recursively) meet `requirements`

        `requirements` must be a sequence of ``Requirement`` objects.  `env`,
        if supplied, should be an ``Environment`` instance.  If
        not supplied, it defaults to all distributions available within any
        entry or distribution in the working set.  `installer`, if supplied,
        will be invoked with each requirement that cannot be met by an
        already-installed distribution; it should return a ``Distribution`` or
        ``None``.

        Unless `replace_conflicting=True`, raises a VersionConflict exception if
        any requirements are found on the path that have the correct name but
        the wrong version.  Otherwise, if an `installer` is supplied it will be
        invoked to obtain the correct version of the requirement and activate
        it.
        """
        pass

    def find_plugins(self, plugin_env, full_env=None, installer=None,
            fallback=True):
        """Find all activatable distributions in `plugin_env`

        Example usage::

            distributions, errors = working_set.find_plugins(
                Environment(plugin_dirlist)
            )
            # add plugins+libs to sys.path
            map(working_set.add, distributions)
            # display errors
            print('Could not load', errors)

        The `plugin_env` should be an ``Environment`` instance that contains
        only distributions that are in the project's "plugin directory" or
        directories. The `full_env`, if supplied, should be an ``Environment``
        contains all currently-available distributions.  If `full_env` is not
        supplied, one is created automatically from the ``WorkingSet`` this
        method is called on, which will typically mean that every directory on
        ``sys.path`` will be scanned for distributions.

        `installer` is a standard installer callback as used by the
        ``resolve()`` method. The `fallback` flag indicates whether we should
        attempt to resolve older versions of a plugin if the newest version
        cannot be resolved.

        This method returns a 2-tuple: (`distributions`, `error_info`), where
        `distributions` is a list of the distributions found in `plugin_env`
        that were loadable, along with any other distributions that are needed
        to resolve their dependencies.  `error_info` is a dictionary mapping
        unloadable plugin distributions to an exception instance describing the
        error that occurred. Usually this will be a ``DistributionNotFound`` or
        ``VersionConflict`` instance.
        """
        pass

    def require(self, *requirements):
        """Ensure that distributions matching `requirements` are activated

        `requirements` must be a string or a (possibly-nested) sequence
        thereof, specifying the distributions and versions required.  The
        return value is a sequence of the distributions that needed to be
        activated to fulfill the requirements; all relevant distributions are
        included, even if they were already activated in this working set.
        """
        pass

    def subscribe(self, callback):
        """Invoke `callback` for all distributions (including existing ones)"""
        pass

    def _added_new(self, dist):
        pass

    def __getstate__(self):
        pass

    def __setstate__(self, e_k_b_c):
        pass


class Environment(object):
    """Searchable snapshot of distributions on a search path"""
    PY_MAJOR = None
    
    def __init__(self, search_path=None, platform=get_supported_platform(),
            python=PY_MAJOR):
        """Snapshot distributions available on a search path

        Any distributions found on `search_path` are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.

        `platform` is an optional string specifying the name of the platform
        that platform-specific distributions must be compatible with.  If
        unspecified, it defaults to the current platform.  `python` is an
        optional string naming the desired version of Python (e.g. ``'3.3'``);
        it defaults to the current version.

        You may explicitly set `platform` (and/or `python`) to ``None`` if you
        wish to map *all* distributions, not just those compatible with the
        running platform or Python version.
        """
        pass

    def can_add(self, dist):
        """Is distribution `dist` acceptable for this environment?

        The distribution must match the platform and python version
        requirements specified when this environment was created, or False
        is returned.
        """
        pass

    def remove(self, dist):
        """Remove `dist` from the environment"""
        pass

    def scan(self, search_path=None):
        """Scan `search_path` for distributions usable in this environment

        Any distributions found are added to the environment.
        `search_path` should be a sequence of ``sys.path`` items.  If not
        supplied, ``sys.path`` is used.  Only distributions conforming to
        the platform/python version defined at initialization are added.
        """
        pass

    def __getitem__(self, project_name):
        """Return a newest-to-oldest list of distributions for `project_name`

        Uses case-insensitive `project_name` comparison, assuming all the
        project's distributions use their project's name converted to all
        lowercase as their key.

        """
        pass

    def add(self, dist):
        """Add `dist` if we ``can_add()`` it and it has not already been added
        """
        pass

    def best_match(self, req, working_set, installer=None):
        """Find distribution best matching `req` and usable on `working_set`

        This calls the ``find(req)`` method of the `working_set` to see if a
        suitable distribution is already active.  (This may raise
        ``VersionConflict`` if an unsuitable version of the project is already
        active in the specified `working_set`.)  If a suitable distribution
        isn't active, this method returns the newest distribution in the
        environment that meets the ``Requirement`` in `req`.  If no suitable
        distribution is found, and `installer` is supplied, then the result of
        calling the environment's ``obtain(req, installer)`` method will be
        returned.
        """
        pass

    def obtain(self, requirement, installer=None):
        """Obtain a distribution matching `requirement` (e.g. via download)

        Obtain a distro that matches requirement (e.g. via download).  In the
        base ``Environment`` class, this routine just returns
        ``installer(requirement)``, unless `installer` is None, in which case
        None is returned instead.  This method is a hook that allows subclasses
        to attempt other ways of obtaining a distribution before falling back
        to the `installer` argument."""
        pass

    def __iter__(self):
        """Yield the unique project names of the available distributions"""
        pass

    def __iadd__(self, other):
        """In-place addition of a distribution or environment"""
        pass

    def __add__(self, other):
        """Add an environment or distribution to an environment"""
        pass


# XXX backward compatibility
AvailableDistributions = Environment


class ExtractionError(RuntimeError):
    """An error occurred extracting a resource

    The following attributes are available from instances of this exception:

    manager
        The resource manager that raised this exception

    cache_path
        The base directory for resource extraction

    original_error
        The exception instance that caused extraction to fail
    """


class ResourceManager:
    """Manage resource extraction and packages"""
    extraction_path = None

    def __init__(self):
        pass

    def resource_exists(self, package_or_requirement, resource_name):
        """Does the named resource exist?"""
        pass

    def resource_isdir(self, package_or_requirement, resource_name):
        """Is the named resource an existing directory?"""
        pass

    def resource_filename(self, package_or_requirement, resource_name):
        """Return a true filesystem path for specified resource"""
        pass

    def resource_stream(self, package_or_requirement, resource_name):
        """Return a readable file-like object for specified resource"""
        pass

    def resource_string(self, package_or_requirement, resource_name):
        """Return specified resource as a string"""
        pass

    def resource_listdir(self, package_or_requirement, resource_name):
        """List the contents of the named resource directory"""
        pass

    def extraction_error(self):
        """Give an error message for problems extracting file(s)"""
        pass

    def get_cache_path(self, archive_name, names=()):
        """Return absolute location in cache for `archive_name` and `names`

        The parent directory of the resulting path will be created if it does
        not already exist.  `archive_name` should be the base filename of the
        enclosing egg (which may not be the name of the enclosing zipfile!),
        including its ".egg" extension.  `names`, if provided, should be a
        sequence of path name parts "under" the egg's extraction location.

        This method should only be called by resource providers that need to
        obtain an extraction location, and only for names they intend to
        extract, as it tracks the generated names for possible cleanup later.
        """
        pass
    @staticmethod
    def _warn_unsafe_extraction_path(path):
        """
        If the default extraction path is overridden and set to an insecure
        location, such as /tmp, it opens up an opportunity for an attacker to
        replace an extracted file with an unauthorized payload. Warn the user
        if a known insecure location is used.

        See Distribute #375 for more details.
        """
        pass

    def postprocess(self, tempname, filename):
        """Perform any platform-specific postprocessing of `tempname`

        This is where Mac header rewrites should be done; other platforms don't
        have anything special they should do.

        Resource providers should call this method ONLY after successfully
        extracting a compressed resource.  They must NOT call it on resources
        that are already in the filesystem.

        `tempname` is the current (temporary) name of the file, and `filename`
        is the name it will be renamed to by the caller after this routine
        returns.
        """
        pass

    def set_extraction_path(self, path):
        """Set the base path where resources will be extracted to, if needed.

        If you do not call this routine before any extractions take place, the
        path defaults to the return value of ``get_default_cache()``.  (Which
        is based on the ``PYTHON_EGG_CACHE`` environment variable, with various
        platform-specific fallbacks.  See that routine's documentation for more
        details.)

        Resources are extracted to subdirectories of this path based upon
        information given by the ``IResourceProvider``.  You may set this to a
        temporary directory, but then you must call ``cleanup_resources()`` to
        delete the extracted files when done.  There is no guarantee that
        ``cleanup_resources()`` will be able to remove all extracted files.

        (Note: you may not change the extraction path for a given resource
        manager once resources have been extracted, unless you first call
        ``cleanup_resources()``.)
        """
        pass

    def cleanup_resources(self, force=False):
        """
        Delete all extracted resource files and directories, returning a list
        of the file and directory names that could not be successfully removed.
        This function does not have any concurrency protection, so it should
        generally only be called when the extraction path is a temporary
        directory exclusive to a single process.  This method is not
        automatically called; you must call it explicitly or register it as an
        ``atexit`` function if you wish to ensure cleanup of a temporary
        directory used for extractions.
        """
        pass

def get_default_cache():
    """Determine the default cache location

    This returns the ``PYTHON_EGG_CACHE`` environment variable, if set.
    Otherwise, on Windows, it returns a "Python-Eggs" subdirectory of the
    "Application Data" directory.  On all other systems, it's "~/.python-eggs".
    """
    pass

def safe_name(name):
    """Convert an arbitrary string to a standard distribution name

    Any runs of non-alphanumeric/. characters are replaced with a single '-'.
    """
    pass

def safe_version(version):
    """Convert an arbitrary string to a standard version string

    Spaces become dots, and all other non-alphanumeric characters become
    dashes, with runs of multiple dashes condensed to a single dash.
    """
    pass

def safe_extra(extra):
    """Convert an arbitrary string to a standard 'extra' name

    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.
    """
    pass

def to_filename(name):
    """Convert a project or version name to its filename-escaped form

    Any '-' characters are currently replaced with '_'.
    """
    pass

class MarkerEvaluation(object):

    @classmethod
    def is_invalid_marker(cls, text):
        """
        Validate text as a PEP 426 environment marker; return an exception
        if invalid or False otherwise.
        """
        pass
    @staticmethod
    def normalize_exception(exc):
        """
        Given a SyntaxError from a marker evaluation, normalize the error
        message:
         - Remove indications of filename and line number.
         - Replace platform-specific error messages with standard error
           messages.
        """
        pass
    
    @classmethod
    def and_test(cls, nodelist):
        # MUST NOT short-circuit evaluation, or invalid syntax can be skipped!
        pass
    
    @classmethod
    def test(cls, nodelist):
        # MUST NOT short-circuit evaluation, or invalid syntax can be skipped!
        pass
    
    @classmethod
    def atom(cls, nodelist):
        pass
    
    @classmethod
    def comparison(cls, nodelist):
        pass
    
    @classmethod
    def get_op(cls, op):
        pass
   
    @classmethod
    def evaluate_marker(cls, text, extra=None):
        """
        Evaluate a PEP 426 environment marker on CPython 2.4+.
        Return a boolean indicating the marker result in this environment.
        Raise SyntaxError if marker is invalid.

        This implementation uses the 'parser' module, which is not implemented
        on
        Jython and has been superseded by the 'ast' module in Python 2.6 and
        later.
        """
        pass
    
    @classmethod
    def _markerlib_evaluate(cls, text):
        """
        Evaluate a PEP 426 environment marker using markerlib.
        Return a boolean indicating the marker result in this environment.
        Raise SyntaxError if marker is invalid.
        """
        pass

    if 'parser' not in globals():
        # Fall back to less-complete _markerlib implementation if 'parser' module
        # is not available.
        pass
    
    @classmethod
    def interpret(cls, nodelist):
        pass
    
    @classmethod
    def evaluate(cls, nodelist):
        pass
    @staticmethod
    def _safe_string(cand):
        pass

invalid_marker = MarkerEvaluation.is_invalid_marker
evaluate_marker = MarkerEvaluation.evaluate_marker

class NullProvider:
    """Try to implement resources and metadata for arbitrary PEP 302 loaders"""

    egg_name = None
    egg_info = None
    loader = None

    def __init__(self, module):
        pass

    def get_resource_filename(self, manager, resource_name):
        pass

    def get_resource_stream(self, manager, resource_name):
        pass

    def get_resource_string(self, manager, resource_name):
        pass

    def has_resource(self, resource_name):
        pass

    def has_metadata(self, name):
        pass

    def get_metadata(self, name):
        pass

    def get_metadata_lines(self, name):
        pass

    def resource_isdir(self, resource_name):
        pass

    def metadata_isdir(self, name):
        pass

    def resource_listdir(self, resource_name):
        pass

    def metadata_listdir(self, name):
        pass

    def run_script(self, script_name, namespace):
        pass

    def _has(self, path):
        pass

    def _isdir(self, path):
        pass

    def _listdir(self, path):
        pass

    def _fn(self, base, resource_name):
        pass

    def _get(self, path):
        pass

register_loader_type(object, NullProvider)


class EggProvider(NullProvider):
    """Provider based on a virtual filesystem"""

    def __init__(self, module):
        pass

    def _setup_prefix(self):
        # we assume here that our metadata may be nested inside a "basket"
        # of multiple eggs; that's why we use module_path instead of .archive
        pass

class DefaultProvider(EggProvider):
    """Provides access to package resources in the filesystem"""

    def _has(self, path):
        pass

    def _isdir(self, path):
        pass

    def _listdir(self, path):
        pass

    def get_resource_stream(self, manager, resource_name):
        pass

    def _get(self, path):
        pass


class EmptyProvider(NullProvider):
    """Provider that returns nothing for all requests"""

    _isdir = _has = lambda self, path: False
    _get = lambda self, path: ''
    _listdir = lambda self, path: []
    module_path = None

    def __init__(self):
        pass

empty_provider = EmptyProvider()


class ZipManifests(dict):
    """
    zip manifest builder
    """

    @classmethod
    def build(cls, path):
        """
        Build a dictionary similar to the zipimport directory
        caches, except instead of tuples, store ZipInfo objects.

        Use a platform-specific path separator (os.sep) for the path keys
        for compatibility with pypy on Windows.
        """
        pass

    load = build


class MemoizedZipManifests(ZipManifests):
    """
    Memoized zipfile manifests.
    """

    def load(self, path):
        """
        Load a manifest at path or return a suitable manifest already loaded.
        """
        pass


class ContextualZipFile: #(zipfile.ZipFile):
    """
    Supplement ZipFile class to support context manager for Python 2.6
    """

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass

    def __new__(cls, *args, **kwargs):
        """
        Construct a ZipFile or ContextualZipFile as appropriate
        """
        pass


class ZipProvider(EggProvider):
    """Resource support for zips and eggs"""

    eagers = None
    _zip_manifests = MemoizedZipManifests()

    def __init__(self, module):
        pass

    def _zipinfo_name(self, fspath):
        # Convert a virtual filename (full path to file) into a zipfile subpath
        # usable with the zipimport directory cache for our target archive
        pass

    def _parts(self, zip_path):
        # Convert a zipfile subpath into an egg-relative path part list.
        # pseudo-fs path
        pass

    
    def zipinfo(self):
        pass

    def get_resource_filename(self, manager, resource_name):
        pass

    @staticmethod    
    def _get_date_and_size(zip_stat):
        pass

    def _extract_resource(self, manager, zip_path):
        pass

    def _is_current(self, file_path, zip_path):
        """
        Return True if the file_path is current for this zip_path
        """
        pass

    def _get_eager_resources(self):
        pass

    def _index(self):
        pass

    def _has(self, fspath):
        pass

    def _isdir(self, fspath):
        pass

    def _listdir(self, fspath):
        pass

    def _eager_to_zip(self, resource_name):
        pass

    def _resource_to_zip(self, resource_name):
        pass


class FileMetadata(EmptyProvider):
    """Metadata handler for standalone PKG-INFO files

    Usage::

        metadata = FileMetadata("/path/to/PKG-INFO")

    This provider rejects all data and metadata requests except for PKG-INFO,
    which is treated as existing, and will be the contents of the file at
    the provided location.
    """

    def __init__(self, path):
        pass

    def has_metadata(self, name):
        pass

    def get_metadata(self, name):
        pass

    def get_metadata_lines(self, name):
        pass


class PathMetadata(DefaultProvider):
    """Metadata provider for egg directories

    Usage::

        # Development eggs:

        egg_info = "/path/to/PackageName.egg-info"
        base_dir = os.path.dirname(egg_info)
        metadata = PathMetadata(base_dir, egg_info)
        dist_name = os.path.splitext(os.path.basename(egg_info))[0]
        dist = Distribution(basedir, project_name=dist_name, metadata=metadata)

        # Unpacked egg directories:

        egg_path = "/path/to/PackageName-ver-pyver-etc.egg"
        metadata = PathMetadata(egg_path, os.path.join(egg_path,'EGG-INFO'))
        dist = Distribution.from_filename(egg_path, metadata=metadata)
    """

    def __init__(self, path, egg_info):
        pass


class EggMetadata(ZipProvider):
    """Metadata provider for .egg files"""

    def __init__(self, importer):
        """Create a metadata provider from a zipimporter"""
        pass

_declare_state('dict', _distribution_finders = {})

def register_finder(importer_type, distribution_finder):
    """Register `distribution_finder` to find distributions in sys.path items

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `distribution_finder` is a callable that, passed a path
    item and the importer instance, yields ``Distribution`` instances found on
    that path item.  See ``pkg_resources.find_on_path`` for an example."""
    pass


def find_distributions(path_item, only=False):
    """Yield distributions accessible via `path_item`"""
    pass

def find_eggs_in_zip(importer, path_item, only=False):
    """
    Find eggs in zip files; possibly multiple nested eggs.
    """
    pass

def find_nothing(importer, path_item, only=False):
    return ()
register_finder(object, find_nothing)

def find_on_path(importer, path_item, only=False):
    """Yield distributions accessible on a sys.path directory"""
    pass

def register_namespace_handler(importer_type, namespace_handler):
    """Register `namespace_handler` to declare namespace packages

    `importer_type` is the type or class of a PEP 302 "Importer" (sys.path item
    handler), and `namespace_handler` is a callable like this::

        def namespace_handler(importer, path_entry, moduleName, module):
            # return a path_entry to use for child packages

    Namespace handlers are only called if the importer object has already
    agreed that it can handle the relevant path item, and they should only
    return a subpath if the module __path__ does not already contain an
    equivalent subpath.  For an example namespace handler, see
    ``pkg_resources.file_ns_handler``.
    """
    pass

def _handle_ns(packageName, path_item):
    """Ensure that named package includes a subpath of path_item (if needed)"""
    pass

def declare_namespace(packageName):
    """Declare that package 'packageName' is a namespace package"""
    pass

def fixup_namespace_packages(path_item, parent=None):
    """Ensure that previously-declared namespace packages include path_item"""
    pass

def file_ns_handler(importer, path_item, packageName, module):
    """Compute an ns-package subpath for a filesystem or zipfile importer"""
    pass

def null_ns_handler(importer, path_item, packageName, module):
    pass

register_namespace_handler(object, null_ns_handler)


def normalize_path(filename):
    """Normalize a file/dir name for comparison purposes"""
    pass

def _normalize_cached(filename, _cache={}):
    pass

def _set_parent_ns(packageName):
    pass

def yield_lines(strs):
    """Yield non-empty/non-comment lines of a string or sequence"""
    pass

def _parse_version_parts(s):
    pass

def parse_version(s):
    """Convert a version string to a chronologically-sortable key

    This is a rough cross between distutils' StrictVersion and LooseVersion;
    if you give it versions that would work with StrictVersion, then it behaves
    the same; otherwise it acts like a slightly-smarter LooseVersion. It is
    *possible* to create pathological version coding schemes that will fool
    this parser, but they should be very rare in practice.

    The returned value will be a tuple of strings.  Numeric portions of the
    version are padded to 8 digits so they will compare numerically, but
    without relying on how numbers compare relative to strings.  Dots are
    dropped, but dashes are retained.  Trailing zeros between alpha segments
    or dashes are suppressed, so that e.g. "2.4.0" is considered the same as
    "2.4". Alphanumeric parts are lower-cased.

    The algorithm assumes that strings like "-" and any alpha string that
    alphabetically follows "final"  represents a "patch level".  So, "2.4-1"
    is assumed to be a branch or patch of "2.4", and therefore "2.4.1" is
    considered newer than "2.4-1", which in turn is newer than "2.4".

    Strings like "a", "b", "c", "alpha", "beta", "candidate" and so on (that
    come before "final" alphabetically) are assumed to be pre-release versions,
    so that the version "2.4" is considered newer than "2.4a1".

    Finally, to handle miscellaneous cases, the strings "pre", "preview", and
    "rc" are treated as if they were "c", i.e. as though they were release
    candidates, and therefore are not as new as a version string that does not
    contain them, and "dev" is replaced with an '@' so that it sorts lower than
    than any other pre-release tag.
    """
    pass


class EntryPoint(object):
    """Object representing an advertised importable object"""

    def __init__(self, name, module_name, attrs=(), extras=(), dist=None):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def load(self, require=True, env=None, installer=None):
        pass

    def require(self, env=None, installer=None):
        pass

    @classmethod    
    def parse(cls, src, dist=None):
        """Parse a single entry point from string `src`

        Entry point syntax follows the form::

            name = some.module:some.attr [extra1, extra2]

        The entry name and module name are required, but the ``:attrs`` and
        ``[extras]`` parts are optional
        """
        pass

    @classmethod
    def parse_group(cls, group, lines, dist=None):
        """Parse an entry point group"""
        pass

    @classmethod
    def parse_map(cls, data, dist=None):
        """Parse a map of entry point groups"""
        pass


def _remove_md5_fragment(location):
    pass


class Distribution(object):
    """Wrap an actual or potential sys.path entry w/metadata"""
    PKG_INFO = 'PKG-INFO'

    def __init__(self, location=None, metadata=None, project_name=None):
        pass

    @classmethod
    def from_location(cls, location, basename, metadata=None,**kw):
        pass

    
    def hashcmp(self):
        pass

    def __hash__(self):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    # These properties have to be lazy so that we don't have to load any
    # metadata until/unless it's actually needed.  (i.e., some distributions
    # may not know their name or version without loading PKG-INFO)

    
    def key(self):
        pass

    
    def parsed_version(self):
        pass

    
    def version(self):
        pass

    
    def _dep_map(self):
        pass

    def requires(self, extras=()):
        """List of Requirements needed for this distro if `extras` are used"""
        pass

    def _get_metadata(self, name):
        pass

    def activate(self, path=None):
        """Ensure distribution is importable on `path` (default=sys.path)"""
        pass

    def egg_name(self):
        """Return what this distribution's standard .egg filename should be"""
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __getattr__(self, attr):
        """Delegate all unrecognized public attributes to .metadata provider"""
        pass

    @classmethod
    def from_filename(cls, filename, metadata=None, **kw):
        pass

    def as_requirement(self):
        """Return a ``Requirement`` that matches this distribution exactly"""
        pass

    def load_entry_point(self, group, name):
        """Return the `name` entry point of `group` or raise ImportError"""
        pass

    def get_entry_map(self, group=None):
        """Return the entry point map for `group`, or the full entry map"""
        pass

    def get_entry_info(self, group, name):
        """Return the EntryPoint object for `group`+`name`, or ``None``"""
        pass

    def insert_on(self, path, loc = None):
        """Insert self.location in path before its nearest parent directory"""
        pass

    def check_version_conflict(self):
        pass

    def has_version(self):
        pass

    def clone(self,**kw):
        """Copy this distribution, substituting in any changed keyword args"""
        pass

    
    def extras(self):
        pass


class DistInfoDistribution(Distribution):
    """Wrap an actual or potential sys.path entry w/metadata, .dist-info style"""
    PKG_INFO = 'METADATA'

    
    def _parsed_pkg_info(self):
        """Parse and cache metadata"""
        pass

    
    def _dep_map(self):
        pass

    def _preparse_requirement(self, requires_dist):
        """Convert 'Foobar (1); baz' to ('Foobar ==1', 'baz')
        Split environment marker, add == prefix to version specifiers as
        necessary, and remove parenthesis.
        """
        pass

    def _compute_dependencies(self):
        """Recompute this distribution's dependencies."""
        pass


_distributionImpl = {
    '.egg': Distribution,
    '.egg-info': Distribution,
    '.dist-info': DistInfoDistribution,
    }


def issue_warning(*args,**kw):
    pass


def parse_requirements(strs):
    """Yield ``Requirement`` objects for each specification in `strs`

    `strs` must be a string, or a (possibly-nested) iterable thereof.
    """
    pass

class Requirement:
    def __init__(self, project_name, specs, extras):
        """DO NOT CALL THIS UNDOCUMENTED METHOD; use Requirement.parse()!"""
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __contains__(self, item):
        pass

    def __hash__(self):
        pass

    def __repr__(self): return "Requirement.parse(%r)" % str(self)

    @staticmethod
    def parse(s):
        pass

state_machine = {
    #       =><
    '<': '--T',
    '<=': 'T-T',
    '>': 'F+F',
    '>=': 'T+F',
    '==': 'T..',
    '!=': 'F++',
}


def _get_mro(cls):
    """Get an mro for a type or classic class"""
    pass

def _find_adapter(registry, ob):
    """Return an adapter factory for `ob` from `registry`"""
    pass

def ensure_directory(path):
    """Ensure that the parent directory of `path` exists"""
    pass

def _bypass_ensure_directory(path, mode=0o777):
    """Sandbox-bypassing version of ensure_directory()"""
    pass

def split_sections(s):
    """Split a string or iterable thereof into (section, content) pairs

    Each ``section`` is a stripped version of the section header ("[section]")
    and each ``content`` is a list of stripped lines excluding blank lines and
    comment-only lines.  If there are any such lines before the first section
    header, they're returned in a first ``section`` of ``None``.
    """
    pass

def _mkstemp(*args,**kw):
    pass


# Set up global resource manager (deliberately not state-saved)
def _initialize(g):

    def resource_filename(self, package_or_requirement, resource_name):
        """Return a true filesystem path for specified resource"""
        pass

    def resource_listdir(self, package_or_requirement, resource_name):
        """List the contents of the named resource directory"""
        pass

class BlobField(ObjectField):
    """ file field implementation based on zodb blobs """

    
    
    def getUnwrapped(self, instance, **kwargs):
        pass

    
    def get(self, instance, **kwargs):
        pass

    
    def set(self, instance, value, **kwargs):
        """ use input value to populate the blob and set the associated
            file name and mimetype.  the latter can be overridden by an
            option "mimetype" keyword argument """
        pass

    def fixAutoId(self, instance):
        """ if an explicit id was given and the instance still has the
        auto-generated one it should be renamed;  also see
        `_setATCTFileContent` in ATCT's `ATCTFileContent` class """
        pass

    def download(self, instance, REQUEST=None, RESPONSE=None):
        """ download the file (use default index_html) """
        pass

    
    def index_html(self, instance, REQUEST=None, RESPONSE=None, **kwargs):
        """ make it directly viewable when entering the objects URL """
        pass

    def get_size(self, instance):
        """ return the size of the blob used for get_size in BaseObject """
        pass

    
    def getContentType(self, instance, fromBaseUnit=True):
        """ return the mimetype associated with the blob data """
        pass

    def getFilename(self, instance, fromBaseUnit=True):
        """ return the file name associated with the blob data """
        pass

class Collection : #(document.ATDocument, ObjectManager):
    """A (new style) Plone Collection"""
    
    # Override initializeArchetype to turn on syndication by default
    def initializeArchetype(self, **kwargs):
        pass

    def listMetaDataFields(self, exclude=True):
        """Return a list of metadata fields from portal_catalog.
        """
        pass

    def results(self, batch=True, b_start=0, b_size=0, sort_on=None, brains=False, custom_query={}):
        """Get results"""
        pass

    # for BBB with ATTopic
    
    def queryCatalog(self, batch=True, b_start=0, b_size=30, sort_on=None, **kwargs):
        pass

    # for BBB with ATTopic
    # This is used in Plone 4.2 but no longer in Plone 4.3
    
    def synContentValues(self):
        pass

    def selectedViewFields(self):
        """Get which metadata field are selected"""
        pass

    
    def getFoldersAndImages(self):
        """Get folders and images"""
        pass

# -*- coding: utf-8 -*-


class ICollection: #(ISyndicatable):
    """ Collection marker interface
    
    """
    pass

class Batch: #(QuantumBatch):

    b_start_str = 'b_start'

    def __init__(self, sequence, size, start=0, end=0, orphan=0,
                 overlap=0, pagerange=7, quantumleap=0,
                 b_start_str='b_start'):
        pass

    def __len__(self):
        pass
    pass

    def initialize(self, start, end, size):
        pass

    def pageurl(self, formvariables, pagenumber=-1):
        """ Makes the url for a given page """
        pass

    def navurls(self, formvariables, navlist=None):
        """ Returns the page number and url for the navigation quick links """
        pass

    def prevurls(self, formvariables):
        """ Helper method to get prev navigation list from templates """
        pass

    def nexturls(self, formvariables):
        """ Helper method to get next navigation list from templates """
        pass


class FolderContentsView: #(BrowserView):
    """
    """

    def __init__(self, context, request):
        pass

    def __call__(self):
        pass

    def contents_table(self):
        pass

    def title(self):
        """
        """
        pass

    def icon(self):
        """
        """
        pass

    def parent_url(self):
        """
        """
        pass

    def renderBase(self):
        """Returns the URL used in the base tag.
        """
        # Assume a folderish context
        pass

class FolderContentsTable(object):
    """
    The foldercontents table renders the table and its actions.
    """

    def __init__(self, context, request, contentFilter=None):
        pass

    def render(self):
        pass

    def contentsMethod(self):
        pass

    def folderitems(self):
        """
        """
        pass

    
    def orderable(self):
        """
        """
        pass

    
    def show_sort_column(self):
        pass

    
    def editable(self):
        """
        """
        pass

    
    def buttons(self):
        pass

    def setbuttonclass(self, button):
        pass

class TableBatchView: #(BatchView):

    def make_link(self, pagenumber):
        pass




class TableBrowserView: #(BrowserView):
    '''Base class which can be used from a AJAX view

    Subclasses only need to set the table property to a different
    class.'''

    table = None

    def update_table(self, pagenumber='1', sort_on='getObjPositionInParent',
                     show_all=False):
        pass


class IFolderContentsView(Interface):
    """Interface, which provides methods for folder contens
    """
    @staticmethod
    def test(a, b, c):
        """A simple replacement of python's test.
        """
        pass
    @staticmethod
    def getAllowedTypes():
        """Returns allowed types for context.
        """
        pass
    @staticmethod
    def title():
        """Returns the title for the template.
        """
        pass


class IFolderContentsViewletManager: #(IViewletManager):
    """A viewlet manager for folder contents
    """
    pass


class IContentsPage(Interface):
    """Marker interface which specifies that the current request is showing
    the "folder contents page" of the object.
    """
    pass


class IContentListing: #(IReadSequence):
    """Sequence of IContentListingObjects"""
    pass


class IContentListingObject: #(IDublinCore):
    """Unified representation of content objects in listings"""
    @staticmethod
    def getId():
        """get the object id in its container"""
        pass
    @staticmethod
    def getObject():
        """get the real object (may be expensive)"""
        pass

    @staticmethod
    def getDataOrigin():
        """The origin of the data for the object."""
        pass

    @staticmethod
    def getPath():
        """Path to the object, relative to the portal root"""
        pass

    @staticmethod
    def getURL():
        """Full url to the object, including the portal root"""
        pass

    @staticmethod
    def uuid():
        """Unique content identifier"""
        pass

    @staticmethod
    def getIcon():
        """icon for the object"""
        pass

    @staticmethod
    def getSize():
        """size in bytes"""
        pass

    @staticmethod
    def review_state():
        """Workflow review state"""
        pass

    @staticmethod
    def PortalType():
        """Portal Type of the opject"""
        pass
    @staticmethod
    def CroppedDescription():
        """A cropped description"""
        pass
    @staticmethod
    def ContentTypeClass():
        """The contenttype suitable as a css class name,
           matching plone conventions
        """
        pass

class WorkflowSubMenuItem : #(BrowserSubMenuItem):
#     implements(IWorkflowSubMenuItem)
# 
#     MANAGE_SETTINGS_PERMISSION = 'Manage portal'
# 
#     title = _(u'label_state', default=u'State:')
#     submenuId = 'plone_contentmenu_workflow'
#     order = 40

    def __init__(self, context, request):
        pass

    
    def extra(self):
        pass

    
    def description(self):
        pass

    
    def action(self):
        pass

    def available(self):
        pass

    def selected(self):
        pass

    def _manageSettings(self):
        pass

    
    def _transitions(self):
        pass

    
    def _currentStateTitle(self):
        pass

class IATUnifiedFolder : #(IATFolder):
    """ marker interface for the new, unified folders """
    pass


class ObsoleteATFolder: #(ATCTOrderedFolder):
    """A folder which can contain other items."""

    def getNextPreviousParentValue(self):
        """If the parent node is also an IATFolder and has next/previous
        navigation enabled, then let this folder have it enabled by
        default as well.
        """
        pass

class ATBTreeFolder: #(ATCTBTreeFolder):
    """A folder suitable for holding a very large number of items.

    Note -- DEPRECATED.  Will be removed in Plone 5.
    Normal folders (as implemented in plone.app.folder) are now suitable for
    storing large numbers of items in most cases.  If you need a folder that
    doesn't track order at all, use a normal folder (from plone.app.folder)
    with the ordering attribute set to u'unordered'.
    """
    pass


class IInterfaceInformation(Interface):
    """A view that gives information about interfaces provided by its context
    """
    @staticmethod
    def provides(dotted_name):
        """Given an interface dotted name, determine if the context provides
        this interface.
        """
        pass
    
    @staticmethod
    def class_provides(dotted_name):
        """Given an interface dotted name, determine if the context's class
        provides this interface.
        """
        pass


class ILayoutPolicy(Interface):
    """A view that gives access to various layout related functions.
    """
    @staticmethod
    def mark_view(view):
        """Adds a marker interface to the view if it is "the" view for the
        context May only be called from a template.
        """
        pass
    
    @staticmethod
    def hide_columns(column_left, column_right):
        """Returns a CSS class matching the current column status.
        """
        pass
    
    @staticmethod
    def have_portlets(manager_name, view=None):
        """Determine whether a column should be shown. The left column is called
        plone.leftcolumn; the right column is called plone.rightcolumn.
        """
        pass

    @staticmethod
    def icons_visible():
        """Returns True if icons should be shown or False otherwise.
        """
        pass

    @staticmethod
    def getIcon(item):
        """Returns an object which implements the IContentIcon interface and
        provides the informations necessary to render an icon. The item
        parameter needs to be adaptable to IContentIcon. Icons can be disabled
        globally or just for anonymous users with the icon_visibility property
        in site_properties.
        """
        pass

    @staticmethod
    def renderBase():
        """Returns the current URL to be used in the base tag.
        """
        pass

    @staticmethod
    def bodyClass(template, view):
        """Returns the CSS class to be used on the body tag.
        """
        pass


class ITools(Interface):
    """A view that gives access to common tools
    """
    @staticmethod
    def actions():
        """The portal_actions tool
        """
        pass

    @staticmethod
    def catalog():
        """The portal_catalog tool
        """
        pass

    @staticmethod
    def membership():
        """The portal_membership tool
        """
        pass

    @staticmethod
    def properties():
        """The portal_properties tool
        """
        pass

    @staticmethod
    def types():
        """The portal_types tool
        """
        pass

    @staticmethod
    def url():
        """The portal_url tool"""
        pass

    @staticmethod
    def workflow():
        """The portal_workflow tool"""
        pass


class IPortalState(Interface):
    """A view that gives access to the current state of the portal
    """

    @staticmethod
    def portal():
        """The portal object
        """
        pass

    @staticmethod
    def portal_title():
        """The title of the portal object
        """
        pass

    @staticmethod
    def portal_url():
        """The URL of the portal object
        """
        pass

    @staticmethod
    def navigation_root():
        """The navigation root object
        """
        pass

    @staticmethod
    def navigation_root_title():
        """The title of the navigation root object
        """
        pass

    @staticmethod
    def navigation_root_path():
        """ path of the navigation root
        """
        pass

    @staticmethod
    def navigation_root_url():
        """The URL of the navigation root
        """
        pass

    @staticmethod
    def default_language():
        """The default language in the portal
        """
        pass
    
    @staticmethod
    def language():
        """The current language
        """
        pass
    
    @staticmethod
    def locale():
        """Get the current locale
        """
        pass

    @staticmethod
    def is_rtl():
        """Whether or not the portal is being viewed in an RTL language
        """
        pass
    @staticmethod
    def member():
        """The current authenticated member
        """
        pass

    @staticmethod
    def anonymous():
        """Whether or not the current member is Anonymous
        """
        pass

    @staticmethod
    def friendly_types():
        """Get a list of portal types considered "end user" types
        """
        pass


class IContextState(Interface):
    """A view that gives access to the state of the current context
    """
    @staticmethod
    def current_page_url():
        """The URL to the current page, including template and query string.
        """
        pass

    @staticmethod
    def current_base_url():
        """The current "actual" URL from the request, excluding the query
        string.
        """
        pass

    @staticmethod
    def canonical_object():
        """The current "canonical" object.

        That is, the current object unless this object is the default page
        in its folder, in which case the folder is returned.
        """
        pass

    @staticmethod
    def canonical_object_url():
        """The URL to the current "canonical" object.

        That is, the current object unless this object is the default page
        in its folder, in which case the folder is returned.
        """
        pass

    @staticmethod
    def view_url():
        """URL to use for viewing

        Files and Images get downloaded when they are directly
        called, instead of with /view appended.  We want to avoid that.
        """
        pass

    @staticmethod
    def view_template_id():
        """The id of the view template of the context
        """
        pass

    @staticmethod
    def is_view_template():
        """Return True if the currentl URL (in the request) refers to the
        standard "view" of the context (i.e. the "view" tab).
        """
        pass

    @staticmethod
    def object_url():
        """The URL of the current object
        """
        pass
    
    @staticmethod
    def object_title():
        """The prettified title of the current object
        """
        pass
    
    @staticmethod
    def workflow_state():
        """The workflow state of the current object
        """
        pass
    
    @staticmethod
    def parent():
        """The direct parent of the current object
        """
        pass

    @staticmethod
    def folder():
        """The current canonical folder
        """
        pass

    @staticmethod
    def is_folderish():
        """True if this is a folderish object, structural or not
        """
        pass

    @staticmethod
    def is_structural_folder():
        """True if this is a structural folder
        """
        pass

    @staticmethod
    def is_default_page():
        """True if this is the default page of its folder
        """
        pass

    @staticmethod
    def is_portal_root():
        """True if this is the portal or the default page in the portal
        """
        pass

    @staticmethod
    def is_editable():
        """Whether or not the current object is editable
        """
        pass
    
    @staticmethod
    def is_locked():
        """Whether or not the current object is locked
        """
        pass

    @staticmethod
    def actions(category):
        """The filtered actions in the context. You can restrict the actions
        to just one category.
        """
        pass

    @staticmethod
    def portlet_assignable():
        """Whether or not the context is capable of having locally assigned
        portlets.
        """
        pass


class IViewView(Interface):
    """Marker interface which specifies that the current view is, in fact,
    a canonical "view" of the object, e.g. what may go on the "view" tab.
    """
    pass

from zope.interface import Interface, Attribute

class INavigationRoot(Interface):
    """A marker interface for signaling the navigation root.
    """
    pass

class IDefaultPage(Interface):
    """Interface for a view that can determine if its context is the
    default page or not.
    """
    @staticmethod
    def isDefaultPage(obj):
        """Finds out if the given obj is the default page for the
        adapted object.
        """
        pass

    @staticmethod
    def getDefaultPage():
        """Returns the id of the default page for the adapted object.
        """
        pass

class INavigationQueryBuilder(Interface):
    """An object which returns a catalog query when called, used to
    construct a navigation tree.
    """
    @staticmethod
    def __call__():
        """Returns a mapping describing a catalog query used to build a
           navigation structure.
        """
        pass

class INavtreeStrategy(Interface):
    """An object that is used by buildFolderTree() to determine how to
    construct a navigation tree.
    """

    rootPath = Attribute("The path to the root of the navtree (None means use portal root)")

    showAllParents = Attribute("Whether or not to show all parents of the current context always")

    @staticmethod
    def nodeFilter(node):
        """Return True or False to determine whether to include the given node
        in the tree. Nodes are dicts with at least one key - 'item', the
        catalog brain of the object the node represents.
        """
        pass
        
    @staticmethod
    def subtreeFilter(node):
        """Return True or False to determine whether to expand the given
        (folderish) node
        """
        pass

    @staticmethod
    def decoratorFactory(node):
        """Inject any additional keys in the node that are needed and return
        the new node.
        """
        pass

    @staticmethod
    def showChildrenOf(object):
        """Given an object (usually the root of the site), determine whether
        children should be shown or not. Even if this returns True, if
        showAllParents is True, the path to the current item may be shown.
        """
        pass

class ViewletBase: #(BrowserView):
    """ Base class with common functions for link viewlets.
    """

    def __init__(self, context, request, view, manager=None):
        pass

    
    
    def portal_url(self):
        pass

    def update(self):
        pass

    def render(self):
        # defer to index method, because that's what gets overridden by the template ZCML attribute
        pass

    def index(self):
        pass

class ContentHistoryView: #(ContentHistoryViewlet):


    def __init__(self, context, request):
        pass

class ContentHistoryViewlet: #(WorkflowHistoryViewlet):

    def getUserInfo(self, userid):
        pass

    def revisionHistory(self):
        pass

    def fullHistory(self):
        pass

    def toLocalizedTime(self, time, long_format=None, time_only=None):
        """Convert time to localized time
        """
        pass


class IQuerystringRegistryReader(Interface):
    """Adapts a registry object to parse the querystring data
    """
    @staticmethod
    def __call__():
        """Return query string in dict-format.
        """
        pass


class IQueryOperation(Interface):
    pass


class IParsedQueryIndexModifier(Interface):
    """Transform a parsed query index in something different
    """
    @staticmethod
    def __call__(value):
        """
        Return a tuple with a new index name and a new value.
        if the index name returned is different from the native one, caller
        must replace treated index with the new ones.
        """
        pass

def quote_chars(s):
    # We need to quote parentheses when searching text indices
    pass

class Search: #(BrowserView):

    valid_keys = ('sort_on', 'sort_order', 'sort_limit', 'fq', 'fl', 'facet')

    def results(self, query=None, batch=True, b_size=10, b_start=0):
        """ Get properly wrapped search results from the catalog.
        Everything in Plone that performs searches should go through this view.
        'query' should be a dictionary of catalog parameters.
        """
        pass

    def filter_query(self, query):
        pass

    def filter_types(self, types):
        pass

    def types_list(self):
        # only show those types that have any content
        pass

    def sort_options(self):
        """ Sorting options for search results view. """
        pass

    def show_advanced_search(self):
        """Whether we need to show advanced search options a.k.a. filters?"""
        pass

    def advanced_search_trigger(self):
        """URL builder for show/close advanced search filters."""
        pass

    def breadcrumbs(self, item):
        pass

    def navroot_url(self):
        pass


class RichTextValue(object):
    """The actual value.

    Note that this is not a persistent object, to avoid a separate ZODB object
    being loaded.
    """

    def __init__(self, raw=None, mimeType=None, outputMimeType=None,
                 encoding='utf-8', output=None):
        pass
    
    
    def raw(self):
        pass

    
    def encoding(self):
        pass

    
    def raw_encoded(self):
        pass

    
    def mimeType(self):
        pass

    
    def outputMimeType(self):
        pass

    
    def output(self):
        pass

    def output_relative_to(self, context):
        """Transforms the raw value to the output mimetype, within a specified context.

        If the value's mimetype is already the same as the output mimetype,
        no transformation is performed.

        The context parameter is relevant when the transformation is
        context-dependent. For example, Plone's resolveuid-and-caption
        transform converts relative links to absolute links using the context
        as a base.

        If a transformer cannot be found for the specified context, a
        transformer with the site as a context is used instead.
        """
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass



class INormalizer(Interface):
    """A normalizer can normalize any unicode text string according to a
       specific ruleset implemented in the normalizer itself.
    """
    @staticmethod
    def normalize(text, locale=None, max_length=None):
        """The normalize method takes and input unicode text and an optional
           locale string and returns a normalized version of the text.
           If the locale is not None the ouput might differ dependent on the
           locale. The max_length argument allows you to override the default
           values used by the normalizers on a case-by-case basis.
        """
        pass

class IIDNormalizer(INormalizer):
    """An ID normalizer can normalize any unicode string and returns a
       version that only contains of ASCII characters allowed in a typical
       scripting or programming language id, such as CSS class names or Python
       variable names for example.
    """
    pass

class IFileNameNormalizer(INormalizer):
    """An file name normalizer can normalize any unicode string and returns a
       version that only contains of ASCII characters allowed in a URL while
       still preserving whitespace and upper and lower case.
    """
    pass

class IURLNormalizer(INormalizer):
    """An URL normalizer can normalize any unicode string and returns a
       URL-safe version that only contains of ASCII characters allowed in a URL.
    """
    pass

class IUserPreferredNormalizer(Interface):
    """An adapter for the HTTPRequest to provide user preferred language
       dependent normalization.
    """
    pass

    @staticmethod
    def normalize(text):
        """Returns a normalized Unicode string."""
        pass

class IUserPreferredFileNameNormalizer(IUserPreferredNormalizer):
    """An adapter for the HTTPRequest to provide user preferred language
       dependent normalization, based on an file name normalizer.
    """
    pass

class IUserPreferredURLNormalizer(IUserPreferredNormalizer):
    """An adapter for the HTTPRequest to provide user preferred language
       dependent normalization, based on an URL normalizer.
    """
    pass

class indexer: #(adapter):
    """The @indexer decorator can be used like this:

        >>> from plone.indexer.decorator import indexer
        >>> @indexer(IMyType)
        ... def some_attribute(object):
        ...     return "some indexable value"

    Note that the @indexer decorator is a superset of the @adapter decorator
    from zope.component.

    To register an indexer for a special type of catalog, use:

        >>> from plone.indexer.decorator import indexer
        >>> @indexer(IMyType, IMyCatalog)
        ... def some_attribute(object):
        ...     return "some indexable value"

    The default is to register the indexer for all IZCatalog catalogs.

    Once you've created an indexer, you can register the adapter in ZCML:

        <adapter factory=".myindexers.some_attribute" name="some_attribute" />

    At this point, the indexable object wrapper will ensure that when
    some_attribute is indexed on an object providing IMyType
    """

    def __init__(self, *interfaces):
        pass

    def __call__(self, callable):
        pass



# global_cache = ram.RAMCache()
# global_cache.update(maxAge=86400)
# 
# DontCache = volatile.DontCache
# MARKER = object()


class AbstractDict:

    def get(self, key, default=None):
        pass

class MemcacheAdapter(AbstractDict):

    def __init__(self, client, globalkey=''):
        pass

    def _make_key(self, source):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass


class RAMCacheAdapter(AbstractDict):

    def __init__(self, ramcache, globalkey=''):
        pass

    def _make_key(self, source):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass


def choose_cache(fun_name):
    pass


def store_in_cache(fun, *args, **kwargs):
    pass


def cache(get_key):
    pass

class AuthenticatorView: #(BrowserView):

    def authenticator(self, extra='', name='_authenticator'):
        pass

    def verify(self, extra='', name="_authenticator"):
        pass

class InvalidRegistryKey: #(InvalidDottedName):
    """A registry key is a dotted name with up to one '/'.
    """
    pass


class IPersistentField: #(IField):
    """A field that can be persistent along with a record.

    We provide our own implementation of the basic field types that are
    supported by the registry.

    A persistent field may track which interface and field it originally
    was constructed from. This is done by the registerInterface() method
    on the IRegistry, for example. Only the interface/field names are stored,
    not actual object references.
    """
    pass


class IFieldRef(Interface):
    """A reference to another field.

    This allows a record to use a field that belongs to another record. Field
    refs are allowed in the Record() constructor.

    Note that all attributes are read-only.
    """
    pass


class IRecord(Interface):
    """A record stored in the registry.

    A record may be "bound" or "unbound". If bound, it will have a
    __parent__ attribute giving the IRegistry it belongs to. It will then
    get and set its field and value attributes from the internal storage in
    the registry. If unbound, it will store its own values.

    A record becomes bound when added to the registry. Records retrieved from
    the registry are always bound.
    """
    pass


class IRecordEvent(Interface):
    """Base interface for record level events
    """
    pass


class IRecordAddedEvent(IRecordEvent):
    """Event fired when a record is added to a registry.
    """
    pass


class IRecordRemovedEvent(IRecordEvent):
    """Event fired when a record is removed from a registry.
    """
    pass


class IRecordModifiedEvent(IRecordEvent):
    """Event fired when a record's value is modified.
    """
    pass


class IInterfaceAwareRecord(Interface):
    """A record will be marked with this interface if it knows which
    interface its field came from.
    """
    pass


class IRegistry(Interface):
    """The configuration registry
    """
    
    @staticmethod
    def __getitem__(key):
        """Get the value under the given key. A record must have been
        installed for this key for this to be valid. Otherwise, a KeyError is
        raised.
        """
        pass

    @staticmethod
    def get(key, default=None):
        """Attempt to get the value under the given key. If it does not
        exist, return the given default.
        """
        pass
    
    @staticmethod
    def __setitem__(key, value):
        """Set the value under the given key. A record must have been
        installed for this key for this to be valid. Otherwise, a KeyError is
        raised. If value is not of a type that's allowed by the record, a
        ValidationError is raised.
        """
        pass

    @staticmethod
    def __contains__(key):
        """Determine if the registry contains a record for the given key.
        """
        pass
    
    @staticmethod
    def forInterface(interface, check=True, omit=(), prefix=None):
        """Get an IRecordsProxy for the given interface. If `check` is True,
        an error will be raised if one or more fields in the interface does
        not have an equivalent setting.
        """
        pass

    @staticmethod
    def registerInterface(interface, omit=(), prefix=None):
        """Create a set of records based on the given interface. For each
        schema field in the interface, a record will be inserted with a
        name like `${interface.__identifier__}.${field.__name__}`, and a
        value equal to default value of that field. Any field with a name
        listed in `omit`, or with the `readonly` property set to True, will
        be ignored. Supply an alternative identifier with `prefix`.
        """
        pass

class IRecordsProxy(Interface):
    """This object is returned by IRegistry.forInterface(). It will be
    made to provide the relevant interface, i.e. it will have the
    attributes that the interface promises. Those attributes will be retrieved
    from or written to the underlying IRegistry.
    """
    pass


def iterDirectoriesOfType(type, filter_duplicates=True):
    """
    Returns a generator which iterates over all resource directories of a
    particular resource type.

    If ``filter_duplicates`` is True and multiple resource directory trees
    contain resource directories with identical names, only the
    first one found will be returned for each name. The following sources are
    checked in order:
    - the persistent portal_resources tool
    - the global resource directory
    - resource directories in distributions
    """
    pass

def queryResourceDirectory(type, name):
    """Find the IResourceDirectory of the given name and type. Returns
    None if not found.
    """
    pass


class And: #(_CompositeQuery):
    
  def _eval(self,context):
    pass

class Or:#(_CompositeQuery):

  def _eval(self,context):
    pass

class MatchRegexp: #(_ElementaryQuery):
  '''idx = term'''
  _OP = '=~~'
  def _functor(self,term): 
    pass

class Between: #(_ElementaryQuery):
  '''lb <= idx <= ub'''
  def __init__(self, idx, lb, ub, filter=False):
    pass
   
  def __str__(self):
    pass

  def _functor(self, term): 
    pass

class Generic: #(_ElementaryQuery):
  _OP = '~~'
  pass

class Eq: #(_ElementaryQuery):
  '''idx = term'''
  _OP = '='
  def _functor(self,term): 
    pass

def registerType(klass, package):
    # Registering a class results in classgen doing its thing
    # Set up accessor/mutators and sane meta/portal_type
    pass


class DisplayList:
    """Static display lists, can look up on
    either side of the dict, and get them in sorted order

    NOTE: Both keys and values *must* contain unique entries! You can have
    two times the same value. This is a "feature" not a bug. DisplayLists
    are meant to be used as a list inside html form entry like a drop down.

    >>> dl = DisplayList()

    Add some keys
    >>> dl.add('foo', 'bar')
    >>> dl.add('egg', 'spam')

    Assert some values
    >>> dl.index
    2
    >>> dl.keys()
    ['foo', 'egg']
    >>> dl.values()
    ['bar', 'spam']
    >>> dl.items()
    (('foo', 'bar'), ('egg', 'spam'))

    You can't use e.g. objects as keys or values
    >>> dl.add(object(), 'error')
    Traceback (most recent call last):
    TypeError: DisplayList keys must be strings, got <type 'object'>

    >>> dl.add('error', object())
    Traceback (most recent call last):
    TypeError: DisplayList values must be strings or ints, got <type 'object'>

    GOTCHA
    Adding a value a second time does overwrite the key, too!
    >>> dl.add('fobar' ,'spam')
    >>> dl.keys()
    ['foo', 'fobar']

    >>> dl.items()
    (('foo', 'bar'), ('fobar', 'spam'))
    """

    security = ClassSecurityInfo()
    security.setDefaultAccess('allow')

    def __init__(self, data=None):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __call__(self):
        pass

    def fromList(self, lst):
        pass

    def __len__(self):
        pass

    def __add__(self, other):
        pass

    def index_sort(self, a, b):
        pass

    def add(self, key, value, msgid=None):
        pass

    def getKey(self, value, default=None):
        """get key"""
        pass

    def getValue(self, key, default=None):
        "get value"
        pass

    def keys(self):
        "keys"
        pass

    def values(self):
        "values"
        pass

    def items(self):
        """items"""
        pass

    def sortedByValue(self):
        """return a new display list sorted by value"""
        pass

    def sortedByKey(self):
        """return a new display list sorted by key"""
        pass

    def __cmp__(self, dest):
        pass

    def __getitem__(self, key):
        #Ok, this is going to pass a number
        #which is index but not easy to get at
        #with the data-struct, fix when we get real
        #itor/generators
        pass

    def __getslice__(self, i1, i2):
        pass

    slice = __getslice__

class IntDisplayList(DisplayList):
    """Static display lists for integer keys, can look up on
    either side of the dict, and get them in sorted order

    The IntDisplayList can be used with integer values only. You should use it
    in favor of a DisplayList if you want to use ints as keys. The support for
    ints as keys for the ordinary DisplayList will be dropped in the next
    release.

    NOTE: Both keys and values *must* contain unique entries! You can have
    two times the same value. This is a "feature" not a bug. DisplayLists
    are meant to be used as a list inside html form entry like a drop down.

    >>> idl = IntDisplayList()

    Add some keys
    >>> idl.add(1, 'number one')
    >>> idl.add(2, 'just the second')

    Assert some values
    >>> idl.index
    2
    >>> idl.keys()
    [1, 2]
    >>> idl.values()
    ['number one', 'just the second']
    >>> idl.items()
    ((1, 'number one'), (2, 'just the second'))

    You can use only ints as keys
    >>> idl.add(object(), 'error')
    Traceback (most recent call last):
    TypeError: IntDisplayList keys must be ints, got <type 'object'>

    >>> idl.add(42, object())
    Traceback (most recent call last):
    TypeError: DisplayList values must be strings or ints, got <type 'object'>

    >>> idl.add('stringkey', 'error')
    Traceback (most recent call last):
    TypeError: IntDisplayList keys must be ints, got <type 'str'>

    >>> idl.add(u'unicodekey', 'error')
    Traceback (most recent call last):
    TypeError: IntDisplayList keys must be ints, got <type 'unicode'>

    GOTCHA
    Adding a value a second time does overwrite the key, too!
    >>> idl.add(3 , 'just the second')
    >>> idl.keys()
    [1, 3]
    >>> idl.items()
    ((1, 'number one'), (3, 'just the second'))

    It is possible to get the value also by a stringified int
    >>> idl.getValue("1")
    'number one'
    >>> idl.getValue(u"1")
    'number one'
    """

    security = ClassSecurityInfo()
    security.setDefaultAccess('allow')

    def __repr__(self):
        pass

    def add(self, key, value, msgid=None):
        pass

    def getValue(self, key, default=None):
        """get value"""
        pass


class InlineValidationView: #(BrowserView):

    def __call__(self, uid, fname, value):
        '''Validate a given field. Return any error messages.
        '''
        pass

PKG_NAME = "Archetypes"
SKIN_NAME = "archetypes"
TOOL_NAME = "archetype_tool"  # Name the tool will be installed under

UID_CATALOG = "uid_catalog"

REGISTER_DEMO_TYPES = True  # Initialize the demo types
DEBUG = False  # Hide debug messages
#DEBUG = True  # See debug messages

RENAME_AFTER_CREATION_ATTEMPTS = 100
# Try up to -100 at the end of the id when doing title-to-id renaming


##Reference Engine bits
REFERENCE_CATALOG = "reference_catalog"
UUID_ATTR = "_at_uid"
REFERENCE_ANNOTATION = "at_references"

# In zope 2.6.3+ and 2.7.0b4+ a lines field returns a tuple not a list. Per
# default archetypes returns a tuple, too. If this breaks your software you
# can disable the change.
# See http://zope.org/Collectors/Zope/924
ZOPE_LINES_IS_TUPLE_TYPE = True

# MYSQL SQLStorage Table Type
# To use connections with ACID transactions you should define it as
# INNODB. The MySQL default table type is MyISAM.
MYSQL_SQLSTORAGE_TABLE_TYPE = 'INNODB'

# Debug security settings of Fields, Widgets and Storages?
DEBUG_SECURITY = False
#DEBUG_SECURITY=True

# BBB constants for removed graphviz suppport
GRAPHVIZ_BINARY = None
HAS_GRAPHVIZ = False

# protect attributes of AttributeStorage from unallowed access?
ATTRIBUTE_SECURITY = True

# set language default for metadata, it will be overwritten by portal-settings!
LANGUAGE_DEFAULT = u''

# Archetypes before 1.4 managed the catalog map using meta types instead of
# portal types. If you need this old behaviour change this setting to False.
CATALOGMAP_USES_PORTALTYPE = True

class ObjectInitializedEvent: #(ObjectModifiedEvent):
    """An object is being initialised, i.e. populated for the first time
    """
    pass

def registerField(klass, **kw):
    pass


class BaseFolder: #(BaseFolderMixin, ExtensibleMetadata):
    """A not-so-basic Folder implementation, with Dublin Core
    Metadata included"""

    def __init__(self, oid, **kwargs):
        # Call skinned first cause baseobject will set new defaults on
        # those attributes anyway
        pass

    def Description(self, **kwargs):
        """We have to override Description here to handle arbitrary
        arguments since PortalFolder defines it."""
        pass

    def setDescription(self, value, **kwargs):
        """We have to override setDescription here to handle arbitrary
        arguments since PortalFolder defines it."""
        pass

class DateTimeField: #(BaseField):
    """
    An improved DateTime Field. It allows to specify
    whether only dates or only times are interesting.
    """
    pass



class ReferenceField(ObjectField):
    """A field for creating references between objects.

    get() returns the list of objects referenced under the relationship
    set() converts a list of target UIDs into references under the
    relationship associated with this field.

    If no vocabulary is provided by you, one will be assembled based on
    allowed_types.
    """


    def get(self, instance, aslist=False, **kwargs):
        """get() returns the list of objects referenced under the relationship
        """
        pass

    def set(self, instance, value, **kwargs):
        """Mutator.

        ``value`` is a either a list of UIDs or one UID string, or a
        list of objects or one object to which I will add a reference
        to. None and [] are equal.

        >>> for node in range(3):
        ...     _ = self.folder.invokeFactory('Refnode', 'n%s' % node)

        Use set with a list of objects:

        >>> nodes = self.folder.n0, self.folder.n1, self.folder.n2
        >>> nodes[0].setLinks(nodes[1:])
        >>> nodes[0].getLinks()
        [<Refnode...>, <Refnode...>]

        Use it with None or () to delete references:

        >>> nodes[0].setLinks(None)
        >>> nodes[0].getLinks()
        []

        Use a list of UIDs to set:

        >>> nodes[0].setLinks([n.UID() for n in nodes[1:]])
        >>> nodes[0].getLinks()
        [<Refnode...>, <Refnode...>]
        >>> nodes[0].setLinks(())
        >>> nodes[0].getLinks()
        []

        Setting multiple values for a non multivalued field will fail:

        >>> nodes[1].setLink(nodes)
        Traceback (most recent call last):
        ...
        ValueError: Multiple values ...

        Keyword arguments may be passed directly to addReference(),
        thereby creating properties on the reference objects:

        >>> nodes[1].setLink(nodes[0].UID(), foo='bar', spam=1)
        >>> ref = nodes[1].getReferenceImpl()[0]
        >>> ref.foo, ref.spam
        ('bar', 1)

        Empty BTreeFolders work as values (#1212048):

        >>> _ = self.folder.invokeFactory('SimpleBTreeFolder', 'btf')
        >>> nodes[2].setLink(self.folder.btf)
        >>> nodes[2].getLink()
        <SimpleBTreeFolder...>
        """
        pass

    def getRaw(self, instance, aslist=False, **kwargs):
        """Return the list of UIDs referenced under this fields
        relationship
        """
        pass
    
    def Vocabulary(self, content_instance=None):
        """Use vocabulary property if it's been defined."""
        pass

    def _brains_title_or_id(self, brain, instance):
        """ ensure the brain has a title or an id and return it as unicode"""
        pass

    def _Vocabulary(self, content_instance):
        pass
    
    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        """
        pass

class FileField(ObjectField):
    """Something that may be a file, but is not an image and doesn't
    want text format conversion"""

    def setContentType(self, instance, value):
        """Set mimetype in the base unit.
        """
        pass
    
    def getContentType(self, instance, fromBaseUnit=True):
        pass

    def _process_input(self, value, file=None, default=None, mimetype=None,
                       instance=None, filename='', **kwargs):
        pass

    def _migrate_old(self, value, default=None, mimetype=None, **kwargs):
        pass

    def _make_file(self, id, title='', file='', instance=None):
        """File content factory"""
        pass

    def get(self, instance, **kwargs):
        pass

    def set(self, instance, value, **kwargs):
        """
        Assign input value to object. If mimetype is not specified,
        pass to processing method without one and add mimetype returned
        to kwargs. Assign kwargs to instance.
        """
        pass

    def _wrapValue(self, instance, value, **kwargs):
        """Wraps the value in the content class if it's not wrapped
        """
        pass

    def getBaseUnit(self, instance, full=False):
        """Return the value of the field wrapped in a base unit object
        """
        pass

    def getFilename(self, instance, fromBaseUnit=True):
        """Get file name of underlaying file object
        """
        pass

    def setFilename(self, instance, filename):
        """Set file name in the base unit.
        """
        pass

    def validate_required(self, instance, value, errors):
        pass

    def download(self, instance, REQUEST=None, RESPONSE=None, no_output=False):
        """Kicks download.

        Writes data including file name and content type to RESPONSE
        """
        pass
    
    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        """
        pass
            
    def getIndexAccessor(self, instance):
        pass

    def getIndexable(self, instance):
        pass


class TextField(FileField):
    """Base Class for Field objects that rely on some type of
    transformation"""

    def defaultView(self):
        pass

    def setContentType(self, instance, value):
        """Set mimetype in the base unit.
        """
        pass
        
    def getAllowedContentTypes(self, instance):
        """ returns the list of allowed content types for this field.
            If the fields schema doesn't define any, the site's default
            values are returned.
        """
        pass

    def _make_file(self, id, title='', file='', instance=None):
        pass

    def _process_input(self, value, file=None, default=None,
                       mimetype=None, instance=None, **kwargs):
        pass

    def getRaw(self, instance, raw=False, **kwargs):
        """
        If raw, return the base unit object, else return encoded raw data
        """
        pass

    def get(self, instance, mimetype=None, raw=False, **kwargs):
        """ If raw, return the base unit object, else return value of
        object transformed into requested mime type.
        If no requested type, then return value in default type. If raw
        format is specified, try to transform data into the default output type
        or to plain text.
        If we are unable to transform data, return an empty string. """
        pass

    def getBaseUnit(self, instance, full=False):
        """Return the value of the field wrapped in a base unit object
        """
        pass

    
    def get_size(self, instance):
        """Get size of the stored data used for get_size in BaseObject
        """
        pass


class Schema: #(BasicSchema, SchemaLayerContainer):
    """
    Schema
    """
    def __init__(self, *args, **kwargs):
        pass

    def __add__(self, other):
        # We can't use update and keep the order so we do it manually
        
        # Need to be smarter when joining layers
        # and internal props
        pass

    
    def copy(self, factory=None):
        """Returns a deep copy of this Schema.
        """
        
        # Need to be smarter when joining layers
        # and internal props
        pass

    
    def wrapped(self, parent):
        pass

    def moveField(self, name, direction=None, pos=None, after=None, before=None):
        """Move a field

        >>> from Products.Archetypes.atapi import StringField as SF
        >>> schema = Schema((SF('a'), SF('b'), SF('c'),))

        >>> schema.keys()
        ['a', 'b', 'c']

        >>> sbefore = schema.copy()
        >>> sbefore.moveField('c', before='a')
        >>> sbefore.keys()
        ['c', 'a', 'b']

        >>> safter = schema.copy()
        >>> safter.moveField('a', after='b')
        >>> safter.keys()
        ['b', 'a', 'c']

        >>> spos = schema.copy()
        >>> spos.moveField('b', pos='top')
        >>> spos.keys()
        ['b', 'a', 'c']

        >>> spos = schema.copy()
        >>> spos.moveField('b', pos='bottom')
        >>> spos.keys()
        ['a', 'c', 'b']

        >>> spos = schema.copy()
        >>> spos.moveField('c', pos=0)
        >>> spos.keys()
        ['c', 'a', 'b']

        maxint can be used to move the field to the last position possible
        >>> from sys import maxint
        >>> spos = schema.copy()
        >>> spos.moveField('a', pos=maxint)
        >>> spos.keys()
        ['b', 'c', 'a']

        Errors
        ======

        >>> schema.moveField('d', pos=0)
        Traceback (most recent call last):
        ...
        KeyError: 'd'

        >>> schema.moveField('a', pos=0, before='b')
        Traceback (most recent call last):
        ...
        ValueError: You must apply exactly one argument.

        >>> schema.moveField('a')
        Traceback (most recent call last):
        ...
        ValueError: You must apply exactly one argument.

        >>> schema.moveField('a', before='a')
        Traceback (most recent call last):
        ...
        ValueError: name and before can't be the same

        >>> schema.moveField('a', after='a')
        Traceback (most recent call last):
        ...
        ValueError: name and after can't be the same

        >>> schema.moveField('a', pos='foo')
        Traceback (most recent call last):
        ...
        ValueError: pos must be a number or top/bottom

        """
        pass

    def _moveFieldToPosition(self, name, pos):
        """Moves a field with the name 'name' to the position 'pos'

        This method doesn't obey the assignement of fields to a schemata
        """
        pass

    def _moveFieldInSchemata(self, name, direction):
        """Moves a field with the name 'name' inside its schemata
        """
        pass


class HoldingReference: #(Reference):
    def beforeTargetDeleteInformSource(self):
        pass

def registerWidget(klass, **kw):
    pass

def addStatusMessage(request, message, type='info'):
    """Add a status message to the request.
    """
    pass

def shasattr(obj, attr, acquire=False):
    """Safe has attribute method

    * It's acquisition safe by default because it's removing the acquisition
      wrapper before trying to test for the attribute.

    * It's not using hasattr which might swallow a ZODB ConflictError (actually
      the implementation of hasattr is swallowing all exceptions). Instead of
      using hasattr it's comparing the output of getattr with a special marker
      object.

    TODO the getattr() trick can be removed when Python's hasattr() is fixed to
    catch only AttributeErrors.

    Quoting Shane Hathaway:

    That said, I was surprised to discover that Python 2.3 implements hasattr
    this way (from bltinmodule.c):

            v = PyObject_GetAttr(v, name);
            if (v == NULL) {
                    PyErr_Clear();
                    Py_INCREF(Py_False);
                    return Py_False;
            }
        Py_DECREF(v);
        Py_INCREF(Py_True);
        return Py_True;

    It should not swallow all errors, especially now that descriptors make
    computed attributes quite common.  getattr() only recently started catching
    only AttributeErrors, but apparently hasattr is lagging behind.  I suggest
    the consistency between getattr and hasattr should be fixed in Python, not
    Zope.

    Shane
    """
    pass


class TypesWidget: #(macrowidget, Base):
   
    def getName(self):
        pass

    def getType(self):
        """Return the type of this field as a string"""
        pass

    
    def bootstrap(self, instance):
        """Override if your widget needs data from the instance."""
        pass

    
    def populateProps(self, field):
        """This is called when the field is created."""
        pass

    def isVisible(self, instance, mode='view'):
        """decide if a field is visible in a given mode -> 'state'

        Return values are visible, hidden, invisible

        The value for the attribute on the field may either be a dict with a
        mapping for edit and view::

            visible = { 'edit' :'hidden', 'view': 'invisible' }

        Or a single value for all modes::

            True/1:  'visible'
            False/0: 'invisible'
            -1:      'hidden'

        visible: The field is shown in the view/edit screen
        invisible: The field is skipped when rendering the view/edit screen
        hidden: The field is added as <input type="hidden" />

        The default state is 'visible'.
        """
        pass

    def setCondition(self, condition):
        # Set the widget expression condition.
        pass

    def getCondition(self):
        # Return the widget text condition.
        pass

    
    def testCondition(self, folder, portal, object):
        # Test the widget condition.
        pass

    
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """Basic impl for form processing in a widget"""
        pass

    
    def copy(self):
        """
        Return a copy of widget instance, consisting of field name and
        properties dictionary.
        """
        pass

    
    def render_own_label(self):
        """
        By default the title/description of a field is not rendered by the
        widget macros, but by the field macros instead. Widgets can change
        that by overriding render_own_label if they need special styling.
        """
        pass
    
class ComputedWidget(TypesWidget):
    pass


class BooleanWidget(TypesWidget):
    pass

 
class MultiSelectionWidget(TypesWidget):

    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """Basic impl for form processing in a widget"""
        pass

    def render_own_label(self):
        pass
    
        
class DecimalWidget(TypesWidget):
    pass


class IntegerWidget(TypesWidget):
    pass


class RichWidget(TypesWidget):
    
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """complex form processing, includes handling for text
        formatting and file objects"""
        # This is basically the old processing chain from base object
        
        # was a mimetype specified
        

        # or a file?
        pass


class SelectionWidget(TypesWidget):
    pass


class StringWidget(TypesWidget):
    pass


class TextAreaWidget(TypesWidget):
    
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """handle text formatting"""
        
        # text field with formatting
        

        """ handle append_only """
        # Don't append if the existing data is empty or nothing was passed in
        
                    # keep historical entries
        pass


class ATDocumentBase : #(ATCTContent, HistoryAwareMixin):
    """A page in the site. Can contain rich text."""

    
    def CookedBody(self, stx_level='ignored'):
        """CMF compatibility method
        """
        pass

    
    def EditableBody(self):
        """CMF compatibility method
        """
        pass

    
    def setFormat(self, value):
        """CMF compatibility method

        The default mutator is overwritten to:

          o add a conversion from stupid CMF content type (e.g. structured-text)
            to real mime types used by MTR.

          o Set format to default format if value is empty

        """
        pass

    
    def setText(self, value, **kwargs):
        """Body text mutator

        * hook into mxTidy an replace the value with the tidied value
        """
        

        # When an object is initialized the first time we have to
        # set the filename and mimetype.
        
        # hook for mxTidy / isTidyHtmlWithCleanup validator
        pass

    
    def guessMimetypeOfText(self):
        """For ftp/webdav upload: get the mimetype from the id and data
        """
        pass

    
    def getTidyOutput(self, field):
        """Get the tidied output for a specific field from the request
        if available
        """
        pass

    def _notifyOfCopyTo(self, container, op=0):
        """Override this to store a flag when we are copied, to be able
        to discriminate the right thing to do in manage_afterAdd here
        below.
        """
        pass

    
    def manage_afterAdd(self, item, container):
        """Fix text when created througt webdav
        Guess the right mimetype from the id/data
        """
        
        # hook for mxTidy / isTidyHtmlWithCleanup validator
        pass

    
    def cmf_edit(self, text_format, text, file='', safety_belt='', **kwargs):
        pass

   
    def manage_afterPUT(self, data, marshall_data, file, context, mimetype,
                        filename, REQUEST, RESPONSE):
        """After webdav/ftp PUT method

        Set title according to the id on webdav/ftp PUTs.
        """

        pass


class ATDocument(ATDocumentBase):
    """A page in the site. Can contain rich text."""

    pass

def marshall_register(schema):
    pass

def finalizeATCTSchema(schema, folderish=False, moveDiscussion=True):
    """Finalizes an ATCT type schema to alter some fields
    """
    pass

class HistoryAwareMixin: #(ATHistoryAwareMixin):
    """History aware mixin class

    Shows a unified diff history of the content

    This mixin is using some low level functions of the ZODB to get the last
    transaction states (versions) of the current object. Older histories will
    disapear after packing the database so DO NOT rely on the history
    functionality. It's more a gimmick and nice helper to reviewers and site
    managers.
    """

    
    def getHistorySource(self):
        """get source for HistoryAwareMixin

        Must return a (raw) string
        """
        pass

    
    def getLastEditor(self):
        """Returns the user name of the last editor.

        Returns None if no last editor is known.
        """
        pass

    def getDocumentComparisons(self, max=10, filterComment=0):
        """Get history as unified diff
        """
        pass

def DT2dt(date):
    """Convert Zope's DateTime to Pythons's datetime
    """
    pass

def dt2DT(date):
    """Convert Python's datetime to Zope's DateTime
    """
    pass


class DateTimeWidget: #(CalendarWidget):
    pass


class RecordsField : #(RecordField):
    """A field that stores a 'record' (dictionary-like) construct"""
    

    def getSize(self, instance):
        """number of records to store"""
        pass

    def isSizeFixed(self):
        """do we need an additional line of entry?"""
        pass

    def showMore(self, values):
        """
        return True if the 'More' button should be shown
        False otherwise
        """
        pass

    def getEditSize(self, instance):
        """
        number of record entries to offer in the form
        at least 'minimalSize' or length of the current
        list of records (+1 if 'more' is enabled)
        """
        pass

    def getSubfieldValue(self, values, idx, subfield, default=None):
        """
        return values[idx].get(key) if existing
        'default' otherwise
        """
        pass

    def getViewFor(self, instance, idx, subfield, joinWith=', '):
        """
        formatted value of the subfield for display
        """
        pass
    
    def _encode_strings(self, value, instance, **kwargs):
        pass

    def _decode_strings(self, value, instance, **kwargs):
        pass

    # convert the records to persistent dictionaries
    def _to_dict(self, value):
        
        def validate(self, value, instance, errors={}, **kwargs):
            """
            Validate passed-in value using all subfield validators.
            Return None if all validations pass; otherwise, return failed
            result returned by validator
            """
            pass


class RecordField(ObjectField):
    """A field that stores a 'record' (dictionary-like) construct"""
     
    def getSubfields(self):
        """the tuple of sub-fields"""
        pass

    
    def getSubfieldType(self, subfield):
        """
        optional type declaration
        default: string
        """
        pass

    
    def getSubfieldLabel(self, subfield):
        """
        optional custom label for the subfield
        default: the id of the subfield
        """
        pass

    def getSubfieldSize(self, subfield, default=40):
        """
        optional custom size for the subfield
        default: 40
        only effective for string type subfields
        """
        pass

    def getSubfieldMaxlength(self, subfield):
        """
        otional custom maxlength size for the subfield
        only effective for string type subfields
        """
        pass

    def isRequired(self,subfield):
        """
        looks whether subfield is included in the list of required subfields
        """
        pass

    def isSelection(self,subfield):
        """select box needed?"""
        
        pass

     
    def testSubfieldCondition(self, subfield, folder, portal, object):
        """Test the subfield condition."""
        pass

    def getVocabularyFor(self, subfield, instance=None):
        """the vocabulary (DisplayList) for the subfield"""
        ## XXX rr: couldn't we just rely on the field's
        ## Vocabulary method here?
        pass

    def getViewFor(self, instance, subfield, joinWith=', '):
        """
        formatted value of the subfield for display
        """
        pass

    def getSubfieldViews(self,instance,joinWith=', '):
        """
        list of subfield views for non-empty subfields
        """
        pass

    # this is really special purpose and in no ways generic
    def hideEmail(self,email='',instance=None):
        pass

    def labelPhone(self,phone=''):
        pass

    def labelFax(self,fax=''):
        pass

    # enable also a string representation of a dictionary
    # to be passed in (external edit may need this)
    # store string values as unicode

    def set(self, instance, value, **kwargs):
        pass

    def _to_dict(self, value):
        pass

    def _decode_strings(self, value, instance, **kwargs):
        pass

    # Return strings using the site's encoding

    def get(self, instance, **kwargs):
        pass

    def _encode_strings(self, value, instance, **kwargs):
        pass

        def _validationLayer(self):
            """
            Resolve that each validator is in the service. If validator is
            not, log a warning.

            We could replace strings with class refs and keep things impl
            the ivalidator in the list.

            Note: XXX this is not compat with aq_ things like scripts with __call__
            """
            pass
        
        def _subfieldValidationLayer(self, subfield):
            """
            for the individual subfields
            """
            pass

        def validate(self, value, instance, errors={}, **kwargs):
            """
            Validate passed-in value using all subfield validators.
            Return None if all validations pass; otherwise, return failed
            result returned by validator
            """
            pass

        def validate_validators(self, value, instance, errors, **kwargs):
            pass


class RecordWidget(StringWidget):
    pass

def makeDisplayList(values=None,add_select=True):
    pass

class RecordsWidget(RecordWidget):
    
    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False):
        """
        Basic impl for form processing in a widget plus clearing
        of the value if the 'delete all entries' flag is set
        """
        pass


def setDefaultRoles(permission, roles):
    '''
    Sets the defaults roles for a permission.
    '''
    pass

def _getAuthenticatedUser(self):
    pass

def registerToolInterface(tool_id, tool_interface):
    pass

def getToolInterface(tool_id):
    """ Get the interface registered for a tool ID
    """
    pass

def getToolByName(obj, name, default=_marker):

    """ Get the tool, 'toolname', by acquiring it.

    o Application code should use this method, rather than simply
      acquiring the tool by name, to ease forward migration (e.g.,
      to Zope3).
    """
    pass

def getToolByInterfaceName(dotted_name, default=_marker):
    pass

def getUtilityByInterfaceName(dotted_name, default=_marker):
    """ Get a tool by its fully-qualified dotted interface path

    This method replaces getToolByName for use in untrusted code.
    Trusted code should use zope.component.getUtility instead.
    """
    pass

def cookString(text):

    """ Make a Zope-friendly ID from 'text'.

    o Remove any spaces

    o Lowercase the ID.
    """
    pass

def tuplize( valueName, value ):

    """ Make a tuple from 'value'.

    o Use 'valueName' to generate appropriate error messages.
    """
    pass


def _checkPermission(permission, obj):
    pass

def _limitGrantedRoles(roles, context, special_roles=()):
    # Only allow a user to grant roles already possessed by that user,
    # with the exception that all special_roles can also be granted.
    pass

def _mergedLocalRoles(object):
    """Returns a merging of object and its ancestors'
    __ac_local_roles__."""
    pass

def _ac_inherited_permissions(ob, all=0):
    # Get all permissions not defined in ourself that are inherited
    # This will be a sequence of tuples with a name as the first item and
    # an empty tuple as the second.
    pass

def _modifyPermissionMappings(ob, map):
    """
    Modifies multiple role to permission mappings.
    """
    # This mimics what AccessControl/Role.py does.
    # Needless to say, it's crude. :-(
    pass


# Parse a string of etags from an If-None-Match header
# Code follows ZPublisher.HTTPRequest.parse_cookie

def parse_etags( text
               , result=None
                # quoted etags (assumed separated by whitespace + a comma)
               , etagre_quote = None #re.compile('(\s*\"([^\"]*)\"\s*,{0,1})')
                # non-quoted etags (assumed separated by whitespace + a comma)
               , etagre_noquote = None #re.compile('(\s*([^,]*)\s*,{0,1})')
               , acquire= None #parse_etags_lock.acquire
               , release= None #parse_etags_lock.release
               ):

    pass

def _checkConditionalGET(obj, extra_context):
    """A conditional GET is done using one or both of the request
       headers:

       If-Modified-Since: Date
       If-None-Match: list ETags (comma delimited, sometimes quoted)

       If both conditions are present, both must be satisfied.

       This method checks the caching policy manager to see if
       a content object's Last-modified date and ETag satisfy
       the conditional GET headers.

       Returns the tuple (last_modified, etag) if the conditional
       GET requirements are met and None if not.

       It is possible for one of the tuple elements to be None.
       For example, if there is no If-None-Match header and
       the caching policy does not specify an ETag, we will
       just return (last_modified, None).
       """

    pass

def _setCacheHeaders(obj, extra_context):
    """Set cache headers according to cache policy manager for the obj."""
    pass


class _ViewEmulator(Implicit):
    """Auxiliary class used to adapt FSFile and FSImage
    for caching_policy_manager
    """
    def __init__(self, view_name=''):
        pass

    def getId(self):
        pass


class ImmutableId(Base):

    """ Base class for objects which cannot be renamed.
    """

    def _setId(self, id):
        """ Never allow renaming!
        """
        pass


class UniqueObject (ImmutableId):

    """ Base class for objects which cannot be "overridden" / shadowed.
    """
    def _getUNIQUE(self):
        pass


class SimpleItemWithProperties:# (PropertyManager, SimpleItem):
    """
    A common base class for objects with configurable
    properties in a fixed schema.
    """

    def manage_propertiesForm(self, REQUEST, *args, **kw):
        """ An override that makes the schema fixed.
        """
        pass


class ToolInit:

    """ Utility class for generating the factories for several tools.
    """
    

    def __init__(self, meta_type, tools, product_name=None, icon=None):
        pass

    def initialize(self, context):
        # Add only one meta type to the folder add list.
       
            # This is a little sneaky: we add self to the
            # FactoryDispatcher under the name "toolinit".
            # manage_addTool() can then grab it.
            pass

def manage_addToolForm(self, REQUEST):

    """ Show the add tool form.
    """
    pass

def manage_addTool(self, type, REQUEST=None):

    """ Add the tool specified by name.
    """
    # self is a FactoryDispatcher.
    pass

#
#   Now, do the same for creating content factories.
#
class ContentInit:

    """ Utility class for generating factories for several content types.
    """
    def initialize(self, context):
        # Add only one meta type to the folder add list.
        
            # This is a little sneaky: we add self to the
            # FactoryDispatcher under the name "contentinit".
            # manage_addContentType() can then grab it.
            pass

def manage_addContentForm(self, REQUEST):

    """ Show the add content type form.
    """
    # self is a FactoryDispatcher.
    pass

def manage_addContent( self, id, type, REQUEST=None ):

    """ Add the content type specified by name.
    """
    pass


def initializeBasesPhase1(base_classes, module):
    """ Execute the first part of initialization of ZClass base classes.

    Stuffs a _ZClass_for_x class in the module for each base.
    """
    pass

def initializeBasesPhase2(zclasses, context):
    """ Finishes ZClass base initialization.

    o 'zclasses' is the list returned by initializeBasesPhase1().

    o 'context' is a ProductContext object.
    """
    pass

def registerIcon(klass, iconspec, _prefix=None):

    """ Make an icon available for a given class.

    o 'klass' is the class being decorated.

    o 'iconspec' is the path within the product where the icon lives.
    """
    pass

def keywordsplitter( headers
                   , names=('Subject', 'Keywords',)
                   , splitter= None #KEYSPLITRE.split
                   ):
    """ Split keywords out of headers, keyed on names.  Returns list.
    """
    pass

def contributorsplitter( headers
                       , names=('Contributors',)
                       , splitter=None#CONTRIBSPLITRE.split
                       ):
    """ Split contributors out of headers, keyed on names.  Returns list.
    """
    pass

def normalize(p):
    # the first .replace is needed to help normpath when dealing with Windows
    # paths under *nix, the second to normalize to '/'
    pass


def expandpath(p):
    """ Convert minimal filepath to (expanded) filepath.

    The (expanded) filepath is the valid absolute path on the current platform
    and setup.
    """
    pass

def minimalpath(p):
    """ Convert (expanded) filepath to minimal filepath.

    The minimal filepath is the cross-platform / cross-setup path stored in
    persistent objects and used as key in the directory registry.

    Returns a slash-separated path relative to the Products path. If it can't
    be found, a normalized path is returned.
    """
    pass

def getContainingPackage(module):
    pass

def getPackageLocation(module):
    """ Return the filesystem location of a module.

    This is a simple wrapper around the global package_home method which
    tricks it into working with just a module name.
    """
    pass

def getPackageName(globals_):
    pass

def _OldCacheHeaders(obj):
    # Old-style checking of modified headers

    pass

def _FSCacheHeaders(obj):
    # Old-style setting of modified headers for FS-based objects

    # Some proxies seem to send invalid date strings for this
    # header. If the date string is not valid, we ignore it
    # rather than raise an error to be generally consistent
    # with common servers such as Apache (which can usually
    # understand the screwy date string as a lucky side effect
    # of the way they parse it).

    #Last-Modified will get stomped on by a cache policy if there is
    #one set....
    pass


class SimpleRecord:
    """ record-like class """

    def __init__(self, **kw):
        pass


class WorkflowException( Exception ):

    """ Exception while invoking workflow.
    """
    pass


class ArchivistRetrieveError: #(ArchivistError):
    """Raised if tried to retrieve a non existent version of a resource.
    """
    pass


class FileTooLargeToVersionError: #(ModifierException):
    """A simple exception indicating that an object contained a file
    object that was too large to support versioning, and that versioning
    will be aborted as a result"""
    pass

def isObjectChanged(obj):
    pass

def maybeSaveVersion(obj, policy='at_edit_autoversion', comment='', force=False):
    pass

def getNavigationRoot(context, relativeRoot=None):
    """Get the path to the root of the navigation tree.

    If a relativeRoot argument is provided, navigation root is computed from
    portal path and this relativeRoot.

    If no relativeRoot argument is provided, and there is a root value set in
    portal_properties, navigation root path is computed from
    portal path and this root value.

    IMPORTANT !!!
    Previous paragraphs imply relativeRoot is relative to the Plone portal.

    Else, a root must be computed : loop from the context to the portal,
    through parents, looking for an object implementing INavigationRoot.
    Return the path of that root.
    """
    pass


class CatalogTool: #(PloneBaseTool, BaseTool):
    """Plone's catalog tool"""

    def __init__(self):
        pass

    def _removeIndex(self, index):
        """Safe removal of an index.
        """
        pass

    def _listAllowedRolesAndUsers(self, user):
        """Makes sure the list includes the user's groups.
        """
        pass

    def indexObject(self, object, idxs=None):
        """Add object to catalog.

        The optional idxs argument is a list of specific indexes
        to populate (all of them by default).
        """
        pass

    def catalog_object(self, object, uid=None, idxs=None,
                       update_metadata=1, pghandler=None):
        pass

    def uncatalog_object(self, *args, **kwargs):
        pass

    def _increment_counter(self):
        pass

    
    def getCounter(self):
        pass

    
    def searchResults(self, REQUEST=None, **kw):
        """Calls ZCatalog.searchResults with extra arguments that
        limit the results to what the user is allowed to see.

        This version uses the 'effectiveRange' DateRangeIndex.

        It also accepts a keyword argument show_inactive to disable
        effectiveRange checking entirely even for those without portal
        wide AccessInactivePortalContent permission.
        """
        pass

    def search(self, *args, **kw):
        # Wrap search() the same way that searchResults() is
        pass

    def clearFindAndRebuild(self):
        """Empties catalog, then finds all contentish objects (i.e. objects
           with an indexObject method), and reindexes them.
           This may take a long time.
        """
        def indexObject(obj, path):
            pass

    def manage_catalogRebuild(self, RESPONSE=None, URL1=None):
        """Clears the catalog and indexes all objects with an 'indexObject'
        method. This may take a long time.
        """
        pass

def ulocalized_time(time, long_format=None, time_only=False, context=None,
                    domain='plonelocales', request=None, target_language=None):
    """unicode aware localized time method (l10n)"""


    # NOTE: this requires the presence of three msgids inside the translation
    #       catalog date_format_long, date_format_short, and time_format
    #       These msgids are translated using interpolation.
    #       The variables used here are the same as used in the strftime
    #       formating.
    #       Supported are:
    #           %A, %a, %B, %b, %H, %I, %m, %d, %M, %p, %S, %Y, %y, %Z
    #       Each used as variable in the msgstr without the %.
    #       For example: "${A} ${d}. ${B} ${Y}, ${H}:${M} ${Z}"
    #       Each language dependend part is translated itself as well.

    # From http://docs.python.org/lib/module-time.html
    #
    # %a    Locale's abbreviated weekday name.
    # %A        Locale's full weekday name.
    # %b        Locale's abbreviated month name.
    # %B        Locale's full month name.
    # %d        Day of the month as a decimal number [01,31].
    # %H        Hour (24-hour clock) as a decimal number [00,23].
    # %I        Hour (12-hour clock) as a decimal number [01,12].
    # %m        Month as a decimal number [01,12].
    # %M        Minute as a decimal number [00,59].
    # %p        Locale's equivalent of either AM or PM.
    # %S        Second as a decimal number [00,61].
    # %y        Year without century as a decimal number [00,99].
    # %Y        Year with century as a decimal number.
    # %Z        Time zone name (no characters if no time zone exists).

    # convert to DateTime instances. Either a date string or
    # a DateTime instance needs to be passed.
    

    # 1. if our Enabled flag in the configuration registry is set,
    # the format string there should override the translation machinery
    

    # 2. the normal case: translation machinery,
    # that is the ".../LC_MESSAGES/plonelocales.po" files
    

    # 3. if both failed, fall back to hardcoded ISO style
    

    # get the format elements used in the formatstring
    

    # reformat the ${foo} to foo
    

    # add used elements to mapping
    

    # add weekday name, abbr. weekday name, month name, abbr month name
    pass


def setupPortalContent(p):
    """
    Import default plone content
    """

    # If we get a territory, we enable the combined language codes

    # As we have a sensible language code set now, we disable the
    # start neutral functionality
    
    # Set the first day of the week, defaulting to Sunday, as the
    # locale data doesn't provide a value for English. European
    # languages / countries have an entry of Monday, though.

    # Enable visible_ids for non-latin scripts

    # See if we have an url normalizer
    

    # If we get a script other than Latn we enable visible_ids
    

    # If we have a normalizer it is safe to disable the visible ids
    
    # The front-page
    pass

class MockMailHost: #(MailBase):
    """A MailHost that collects messages instead of sending them.
    """

    def __init__(self, id):
        pass

    def reset(self):
       pass

    def _send(self, mfrom, mto, messageText, immediate=False):
        """ Send the message """
        pass

    def send(self, messageText, mto=None, mfrom=None, subject=None,
             encode=None, immediate=False, charset=None, msg_type=None):
        pass

    # Outside of the tests we patch the MailHost to provide a
    # secureSend method for backwards compatibility, so we should do
    # that for our MockMailHost as well.
    

class TranslationServiceTool: #(PloneBaseTool, UniqueObject, SimpleItem):
    """ Utility methods to access the translation machinery """

    
    def utranslate(self, *args, **kw):
        pass

    def translate(self, msgid, domain=None, mapping=None, context=None,
                  target_language=None, default=None):
        # Translate method for resticted code like skins.
        pass

    def encode(self, m, input_encoding=None, output_encoding=None,
               errors='strict'):
        # encode a give unicode type or string type to string type in encoding
        # output_encoding

        # check if input is not type unicode
        

        # return as type string
        pass

    def asunicodetype(self, m, input_encoding=None, errors='strict'):
        # create type unicode from type string
        pass

    def ulocalized_time(self, time, long_format=None, time_only=None,
                        context=None, domain='plonelocales', request=None):
        # get some context if none is passed
       pass

    def day_msgid(self, number, format=None):
        """ Returns the msgid which can be passed to the translation service
        for l10n of weekday names. Format is either None, 'a' or 's'.

        >>> ttool = TranslationServiceTool()

        >>> ttool.day_msgid(0)
        'weekday_sun'

        >>> ttool.day_msgid(6)
        'weekday_sat'

        >>> ttool.day_msgid(0, format='a')
        'weekday_sun_abbr'

        >>> ttool.day_msgid(3, format='s')
        'weekday_wed_short'
        """
        pass

    def month_msgid(self, number, format=None):
        """ Returns the msgid which can be passed to the translation service
        for l10n of month names. Format is either '' or 'a' (long or
        abbreviation).

        >>> ttool = TranslationServiceTool()

        >>> ttool.month_msgid(1)
        'month_jan'

        >>> ttool.month_msgid(12)
        'month_dec'

        >>> ttool.month_msgid(6, format='a')
        'month_jun_abbr'
        """
        pass

    def month_english(self, number, format=None):
        """ Returns the english name of month by number. Format is either '' or
        'a' (long or abbreviation).

        >>> ttool = TranslationServiceTool()

        >>> ttool.month_english(1)
        'January'

        >>> ttool.month_english(1, 'a')
        'Jan'
        """
        pass

    def month(self, number, format=None, default=None):
        """ Returns a Message with the month name, that can be translated by
        the TAL engine. Format is either None or 'a' (long or abbreviation).
        """
        pass

    def weekday_english(self, number, format=None):
        """ Returns the english name of a week by number. Format is
        either None, 'a' or 'p'.

        >>> ttool = TranslationServiceTool()

        >>> ttool.weekday_english(0)
        'Sunday'

        >>> ttool.weekday_english(6)
        'Saturday'

        >>> ttool.weekday_english(0, format='a')
        'Sun'

        >>> ttool.weekday_english(3, format='p')
        'Wed.'
        """
        pass

def base_hasattr(obj, name):
    """Like safe_hasattr, but also disables acquisition."""
    pass

def safe_callable(obj):
    """Make sure our callable checks are ConflictError safe."""
    pass

def isIDAutoGenerated(context, id):
    # In 2.1 non-autogenerated is the common case, caught exceptions are
    # expensive, so let's make a cheap check first
    pass

def _createObjectByType(type_name, container, id, *args, **kw):
    """Create an object without performing security checks

    invokeFactory and fti.constructInstance perform some security checks
    before creating the object. Use this function instead if you need to
    skip these checks.

    This method uses
    CMFCore.TypesTool.FactoryTypeInformation._constructInstance
    to create the object without security checks.
    """
    pass

def safe_unicode(value, encoding='utf-8'):
    """Converts a value to unicode, even it is already a unicode string.

        >>> from Products.CMFPlone.utils import safe_unicode

        >>> safe_unicode('spam')
        u'spam'
        >>> safe_unicode(u'spam')
        u'spam'
        >>> safe_unicode(u'spam'.encode('utf-8'))
        u'spam'
        >>> safe_unicode('\xc6\xb5')
        u'\u01b5'
        >>> safe_unicode(u'\xc6\xb5'.encode('iso-8859-1'))
        u'\u01b5'
        >>> safe_unicode('\xc6\xb5', encoding='ascii')
        u'\u01b5'
        >>> safe_unicode(1)
        1
        >>> print safe_unicode(None)
        None
    """
    pass

def pretty_title_or_id(context, obj, empty_value=_marker):
    """Return the best possible title or id of an item, regardless
       of whether obj is a catalog brain or an object, but returning an
       empty title marker if the id is not set (i.e. it's auto-generated).
    """
    pass

def isExpired(content):
    """ Find out if the object is expired (copied from skin script) """

    expiry = None

    # NOTE: We also accept catalog brains as 'content' so that the
    # catalog-based folder_contents will work. It's a little magic, but
    # it works.

    # ExpirationDate should have an ISO date string, which we need to
    # convert to a DateTime

    # Try DC accessor first
    pass

def transaction_note(note):
    """Write human legible note"""
    pass

class BrowserView: #(Location):
    """Browser View.

    >>> view = BrowserView("context", "request")
    >>> view.context
    'context'
    >>> view.request
    'request'

    >>> view.__parent__
    'context'
    >>> view.__parent__ = "parent"
    >>> view.__parent__
    'parent'
    """

    def __init__(self, context, request):
        pass

    def __getParent(self):
        pass

    def __setParent(self, parent):
        pass
    
class querybuilder:
    pass

class QueryBuilder(BrowserView):
    """ This view is used by the javascripts,
        fetching configuration or results"""

    def __init__(self, context, request):
        pass

    def __call__(self, query, batch=False, b_start=0, b_size=30,
                 sort_on=None, sort_order=None, limit=0, brains=False,
                 custom_query=None):
        """Create a zope catalog query and return results.
        :param query: The querystring to be parsed into a zope catalog query.
        :type query: dictionary
        :param batch: Return a plone.batching ``Batch`` instead of a zope
                      catalog result.
        :type batch: boolean
        :param b_start: Start item of the batch.
        :type b_start: integer
        :param b_size: Size of the batch.
        :type b_size: integer
        :param sort_on: Name of the sort index for sorting the results.
        :type sort_on: string
        :param sort_order: The order of the result sorting. Either 'ascending'
                           or 'descending'. 'reverse' is an alias equivalent
                           to 'descending'.
        :type sort_order: string
        :param limit: Limit the results.
        :type limit: integer
        :param brains: Return brains or IContentListing objects.
        :type brains: boolean
        :param custom_query: A dictionary of index names and their associated
                             query values. The custom_query updates the parsed
                             query, thus overriding the query string.
                             May be None.
        :type custom_query: dictionary or None
        """
        pass

    def html_results(self, query):
        """html results, used for in the edit screen of a collection,
           used in the live update results"""
        pass

    def _makequery(self, query=None, batch=False, b_start=0, b_size=30,
                   sort_on=None, sort_order=None, limit=0, brains=False,
                   custom_query=None):
        """Parse the (form)query and return using multi-adapter"""
        pass

    def number_of_results(self, query):
        """Get the number of results"""
        pass



class ViewPageTemplateFile: #(TrustedAppPT, PageTemplateFile):
    """Page Template used as class variable of views defined as Python classes.
    """
    def __init__(self, filename, _prefix=None, content_type=None):
       pass

    def getId(self):
        pass


    def __call__(self, __instance, *args, **keywords):
        pass

    def pt_getEngine(self):
        pass

    def pt_getContext(self, instance, request, **kw):
        pass

    def __get__(self, instance, type):
        pass


class IMailHost(Interface):
    @staticmethod
    def send(messageText, mto=None, mfrom=None, subject=None, encode=None,
             charset=None, msg_type=None):
        """Send mail.
        """
        pass

def html_quote(v, name='(Unknown name)', md={}):
    pass

class IMessage(Interface):
    """A single status message."""

    pass


class IStatusMessage(Interface):
    """An adapter for the BrowserRequest to handle status messages."""
    @staticmethod
    def addStatusMessage(text, type=u'info'):
        """Add a status message."""
        pass

    @staticmethod
    def add(text, type=u'info'):
        """Add a status message."""
        pass

    @staticmethod
    def showStatusMessages():
        """Removes all status messages and returns them for display.
        """
        pass
    
    @staticmethod
    def show():
        """Removes all status messages and returns them for display.
        """
        pass


class IValidator(Interface):

    @staticmethod
    def __call__(value, *args, **kwargs):
        """return True if valid, error string if not"""
        pass


class IValidationChain(IValidator):
    """Marker interface for a chain
    """
    pass


class RegexValidator:
    

    def __init__(self, name, *args, **kw):
        pass

    def compileRegex(self):
        pass

    def __getstate__(self):
        """Because copy.deepcopy and pickle.dump cannot pickle a regex pattern
        I'm using the getstate/setstate hooks to set self.regex to []
        """
        pass

    def __setstate__(self, dict):
        pass

    def __call__(self, value, *args, **kwargs):
        pass


class ZCatalog: #(Folder, Persistent, Implicit):
    """ZCatalog object

    A ZCatalog contains arbirary index like references to Zope
    objects.  ZCatalog's can index either 'Field' values of object, or
    'Text' values.

    ZCatalog does not store references to the objects themselves, but
    rather to a unique identifier that defines how to get to the
    object.  In Zope, this unique idenfier is the object's relative
    path to the ZCatalog (since two Zope object's cannot have the same
    URL, this is an excellent unique qualifier in Zope).

    Most of the dirty work is done in the _catalog object, which is an
    instance of the Catalog class.  An interesting feature of this
    class is that it is not Zope specific.  You can use it in any
    Python program to catalog objects.
    """


    def __init__(self, id, title='', vocab_id=None, container=None):
        # ZCatalog no longer cares about vocabularies
        # so the vocab_id argument is ignored (Casey)

        pass

    def __len__(self):
        pass

    def manage_edit(self, RESPONSE, URL1, threshold=1000, REQUEST=None):
        """ edit the catalog """
        pass

    def manage_subbingToggle(self, REQUEST, RESPONSE, URL1):
        """ toggle subtransactions """
        pass

    def manage_catalogObject(self, REQUEST, RESPONSE, URL1, urls=None):
        """ index Zope object(s) that 'urls' point to """
        pass

    def manage_uncatalogObject(self, REQUEST, RESPONSE, URL1, urls=None):
        """ removes Zope object(s) 'urls' from catalog """
        pass

    def manage_catalogReindex(self, REQUEST, RESPONSE, URL1):
        """ clear the catalog, then re-index everything """

        pass

    def refreshCatalog(self, clear=0, pghandler=None):
        """ re-index everything we can find """

        pass

    def manage_catalogClear(self, REQUEST=None, RESPONSE=None, URL1=None):
        """ clears the whole enchilada """
        pass

    def manage_catalogFoundItems(self, REQUEST, RESPONSE, URL2, URL1,
                                 obj_metatypes=None,
                                 obj_ids=None, obj_searchterm=None,
                                 obj_expr=None, obj_mtime=None,
                                 obj_mspec=None, obj_roles=None,
                                 obj_permission=None):
        """ Find object according to search criteria and Catalog them
        """
        pass
   
    def manage_addColumn(self, name, REQUEST=None, RESPONSE=None, URL1=None):
        """ add a column """
        pass

    def manage_delColumn(self, names, REQUEST=None, RESPONSE=None, URL1=None):
        """ delete a column or some columns """
        pass

    def manage_addIndex(self, name, type, extra=None,
                        REQUEST=None, RESPONSE=None, URL1=None):
        """add an index """
        pass

    def manage_delIndex(self, ids=None, REQUEST=None, RESPONSE=None,
        URL1=None):
        """ delete an index or some indexes """
        pass

    def manage_clearIndex(self, ids=None, REQUEST=None, RESPONSE=None,
        URL1=None):
        """ clear an index or some indexes """
        pass
    
    def reindexIndex(self, name, REQUEST, pghandler=None):
        pass

    
    def manage_reindexIndex(self, ids=None, REQUEST=None, RESPONSE=None,
                            URL1=None):
        """Reindex indexe(s) from a ZCatalog"""
        pass

    
    def catalog_object(self, obj, uid=None, idxs=None, update_metadata=1,
                       pghandler=None):
        
        # None passed in to catalogObject as third argument indicates
        # that we shouldn't try to commit subtransactions within any
        # indexing code.  We throw away the result of the call to
        # catalogObject (which is a word count), because it's
        # worthless to us here.

        
        # increment the _v_total counter for this thread only and get
        # a reference to the current transaction.
        # the _v_total counter is zeroed if we notice that we're in
        # a different transaction than the last one that came by.
        # self.threshold represents the number of times that
        # catalog_object needs to be called in order for the catalog
        # to commit a subtransaction.  The semantics here mean that
        # we should commit a subtransaction if our threshhold is
        # exceeded within the boundaries of the current transaction.
        pass

    
    def uncatalog_object(self, uid):
        pass

    def uniqueValuesFor(self, name):
        # Return the unique values for a given FieldIndex
        pass

    
    def getpath(self, rid):
        # Return the path to a cataloged object given a 'data_record_id_'
        pass

    def getrid(self, path, default=None):
        # Return 'data_record_id_' the to a cataloged object given a 'path'
        pass

    def getobject(self, rid, REQUEST=None):
        # Return a cataloged object given a 'data_record_id_'
        pass

    
    def getMetadataForUID(self, uid):
        # return the correct metadata given the uid, usually the path
        pass

    def getIndexDataForUID(self, uid):
        # return the current index contents given the uid, usually the path
        pass

    def getMetadataForRID(self, rid):
        # return the correct metadata for the cataloged record id
        pass

    def getIndexDataForRID(self, rid):
        # return the current index contents for the specific rid
        pass

    
    def schema(self):
        pass

    def indexes(self):
        pass

    def index_objects(self):
        # This method returns unwrapped indexes!
        # You should probably use getIndexObjects instead
        pass

    
    def getIndexObjects(self):
        # Return a list of wrapped(!) indexes
        pass

    def _searchable_arguments(self):
        pass

    def _searchable_result_columns(self):
        pass
    
    def searchResults(self, REQUEST=None, used=None, **kw):
        """Search the catalog

        Search terms can be passed in the REQUEST or as keyword
        arguments.

        The used argument is now deprecated and ignored
        """

        pass

    
    def search(
        self, query_request, sort_index=None, reverse=0, limit=None, merge=1):
        """Programmatic search interface, use for searching the catalog from
        scripts.

        query_request: Dictionary containing catalog query
        sort_index:    Name of sort index
        reverse:       Reverse sort order?
        limit:         Limit sorted result count (optimization hint)
        merge:         Return merged results (like searchResults) or raw
                       results for later merging.
        """
        pass

    ## this stuff is so the find machinery works

    # meta_types=() # Sub-object types that are specific to this object

    
    def valid_roles(self):
        # Return list of valid roles
        pass


    def ZopeFindAndApply(self, obj, obj_ids=None, obj_metatypes=None,
                         obj_searchterm=None, obj_expr=None,
                         obj_mtime=None, obj_mspec=None,
                         obj_permission=None, obj_roles=None,
                         search_sub=0,
                         REQUEST=None, result=None, pre='',
                         apply_func=None, apply_path=''):
        """Zope Find interface and apply

        This is a *great* hack.  Zope find just doesn't do what we
        need here; the ability to apply a method to all the objects
        *as they're found* and the need to pass the object's path into
        that method.
        """

        pass


    
    def resolve_url(self, path, REQUEST):
        # Attempt to resolve a url into an object in the Zope
        # namespace. The url may be absolute or a catalog path
        # style url. If no object is found, None is returned.
        # No exceptions are raised.
        pass


    def resolve_path(self, path):
        # Attempt to resolve a url into an object in the Zope
        # namespace. The url may be absolute or a catalog path
        # style url. If no object is found, None is returned.
        # No exceptions are raised.
        pass


    def manage_normalize_paths(self, REQUEST):
        """Ensure that all catalog paths are full physical paths

        This should only be used with ZCatalogs in which all paths can
        be resolved with unrestrictedTraverse."""

        pass

    
    def manage_setProgress(self, pgthreshold=0, RESPONSE=None, URL1=None):
        """Set parameter to perform logging of reindexing operations very
           'pgthreshold' objects
        """
        pass

    def _getProgressThreshold(self):
        pass

    # Indexing methods

    
    def addIndex(self, name, type, extra=None):
        pass

        # Convert the type by finding an appropriate product which supports
        # this interface by that name.  Bleah
       
    def delIndex(self, name):
        pass

    
    def clearIndex(self, name):
        pass

   
    def addColumn(self, name, default_value=None):
        pass

    
    def delColumn(self, name):
        pass

    # Catalog plan methods

    
    def getCatalogPlan(self):
        """Get a string representation of a query plan"""
        pass

    
    def getCatalogReport(self):
        """Query time reporting."""
        pass

    
    def manage_resetCatalogReport(self, REQUEST=None):
        """Resets the catalog report."""
        pass

    
    def manage_editCatalogReport(self, long_query_time=0.1, REQUEST=None):
        """Edit the long query time."""
        pass


class ParseError(Exception):
    pass


class Template:
    """A string class for supporting $-substitutions."""
    

    def __init__(self, template):
        pass

    # Search for $$, $identifier, ${identifier}, and any bare $'s

    def _invalid(self, mo):
        pass
    
    @staticmethod
    def substitute(*args, **kws):
        
        def convert(mo):
            # Check the most common path first.
            pass

    @staticmethod
    def safe_substitute(*args, **kws):
        
        def convert(mo):
            pass

    def savepoint(self, optimistic=False):
        pass

def rfc1123_date(ts=None):
    # Return an RFC 1123 format date string, required for
    # use in HTTP Date headers per the HTTP 1.1 spec.
    # 'Fri, 10 Nov 2000 16:21:09 GMT'
    pass


class BadRequest(Exception):
    pass

class Forbidden(Exception):
    pass

class Redirect(Exception):
    pass

class ConflictError: #(POSError, transaction.interfaces.TransientError):
    """Two transactions tried to modify the same object at once.

    This transaction should be resubmitted.

    Instance attributes:
      oid : string
        the OID (8-byte packed string) of the object in conflict
      class_name : string
        the fully-qualified name of that object's class
      message : string
        a human-readable explanation of the error
      serials : (string, string)
        a pair of 8-byte packed strings; these are the serial numbers
        related to conflict.  The first is the revision of object that
        is in conflict, the currently committed serial.  The second is
        the revision the current transaction read when it started.
      data : string
        The database record that failed to commit, used to put the
        class name in the error message.

    The caller should pass either object or oid as a keyword argument,
    but not both of them.  If object is passed, it should be a
    persistent object with an _p_oid attribute.
    """

    def __init__(self, message=None, object=None, oid=None, serials=None,
                 data=None):
        pass

    def __str__(self):
        pass

    def get_oid(self):
        pass

    def get_class_name(self):
        pass

    def get_old_serial(self):
        pass

    def get_new_serial(self):
        pass

    def get_serials(self):
        pass

def getSite():
    pass

def getMultiAdapter(objects, interface=Interface, name=u'', context=None):
    pass

def adapts(*interfaces):
    pass

def getAdapters(objects, provided, context=None):
    pass

def getUtility(interface, name='', context=None):
    pass


def queryUtility(interface, name='', default=None, context=None):
    pass

class ComponentLookupError(LookupError):
    """A component could not be found."""
    pass

class ContainerModifiedEvent: #(ObjectModifiedEvent):
    """The container has been modified."""

    pass

def resolve(name, module=None):
    pass

def notify(event):
    """ Notify all subscribers of ``event``.
    """
    pass

def translate(msgid, domain=None, mapping=None, context=None,
               target_language=None, default=None):
    """Translate text.

    First setup some test components:

    >>> from zope import component, interface
    >>> import zope.i18n.interfaces

    >>> class TestDomain:
    ...     interface.implements(zope.i18n.interfaces.ITranslationDomain)
    ...
    ...     def __init__(self, **catalog):
    ...         self.catalog = catalog
    ...
    ...     def translate(self, text, *_, **__):
    ...         return self.catalog[text]

    Normally, the translation system will use a domain utility:

    >>> component.provideUtility(TestDomain(eek=u'ook'), name='my.domain')
    >>> translate(u'eek', 'my.domain')
    u'ook'

    Normally, if no domain is given, or if there is no domain utility
    for the given domain, then the text isn't translated:

    >>> translate(u'eek')
    u'eek'

    Moreover the text will be converted to unicode:

    >>> translate('eek', 'your.domain')
    u'eek'

    A fallback domain factory can be provided. This is normally used
    for testing:

    >>> def fallback(domain=u''):
    ...     return TestDomain(eek=u'test-from-' + domain)
    >>> interface.directlyProvides(
    ...     fallback,
    ...     zope.i18n.interfaces.IFallbackTranslationDomainFactory,
    ...     )

    >>> component.provideUtility(fallback)

    >>> translate(u'eek')
    u'test-from-'

    >>> translate(u'eek', 'your.domain')
    u'test-from-your.domain'
    """

    pass


class MessageFactory(object):
    """Factory for creating i18n messages."""

    def __init__(self, domain):
        pass

    def __call__(self, ustr, default=None, mapping=None):
        pass

PloneMessageFactory = MessageFactory('plone')


def negotiate(context):
    """Negotiate language.

    This only works if the languages are set globally, otherwise each message
    catalog needs to do the language negotiation.
    """
    pass

def interpolate(text, mapping=None):
    """Insert the data passed from mapping into the text.

    First setup a test mapping:

    >>> mapping = {"name": "Zope", "version": 3}

    In the text we can use substitution slots like $varname or ${varname}:

    >>> interpolate(u"This is $name version ${version}.", mapping)
    u'This is Zope version 3.'

    Interpolation variables can be used more than once in the text:

    >>> interpolate(u"This is $name version ${version}. ${name} $version!",
    ...             mapping)
    u'This is Zope version 3. Zope 3!'

    In case if the variable wasn't found in the mapping or '$$' form
    was used no substitution will happens:

    >>> interpolate(u"This is $name $version. $unknown $$name $${version}.",
    ...             mapping)
    u'This is Zope 3. $unknown $$name $${version}.'

    >>> interpolate(u"This is ${name}")
    u'This is ${name}'
    """

    def replace(match):
        pass



def alsoProvides(object, *interfaces):
    """Declare interfaces declared directly for an object

    The arguments after the object are one or more interfaces or interface
    specifications (``IDeclaration`` objects).

    The interfaces given (including the interfaces in the specifications) are
    added to the interfaces previously declared for the object.

    Consider the following example:

      >>> from zope.interface import Interface
      >>> class I1(Interface): pass
      ...
      >>> class I2(Interface): pass
      ...
      >>> class IA1(Interface): pass
      ...
      >>> class IA2(Interface): pass
      ...
      >>> class IB(Interface): pass
      ...
      >>> class IC(Interface): pass
      ...
      >>> class A(object):
      ...     implements(IA1, IA2)
      >>> class B(object):
      ...     implements(IB)

      >>> class C(A, B):
      ...    implements(IC)

      >>> ob = C()
      >>> directlyProvides(ob, I1)
      >>> int(I1 in providedBy(ob))
      1
      >>> int(I2 in providedBy(ob))
      0
      >>> int(IA1 in providedBy(ob))
      1
      >>> int(IA2 in providedBy(ob))
      1
      >>> int(IB in providedBy(ob))
      1
      >>> int(IC in providedBy(ob))
      1

      >>> alsoProvides(ob, I2)
      >>> int(I1 in providedBy(ob))
      1
      >>> int(I2 in providedBy(ob))
      1
      >>> int(IA1 in providedBy(ob))
      1
      >>> int(IA2 in providedBy(ob))
      1
      >>> int(IB in providedBy(ob))
      1
      >>> int(IC in providedBy(ob))
      1

    The object, ``ob`` provides ``I1``, ``I2``, and whatever interfaces
    instances have been declared for instances of ``C``. Notice that the
    alsoProvides just extends the provided interfaces.
    """
    pass

def implements(*interfaces):
    """Declare interfaces implemented by instances of a class

      This function is called in a class definition.

      The arguments are one or more interfaces or interface
      specifications (IDeclaration objects).

      The interfaces given (including the interfaces in the
      specifications) are added to any interfaces previously
      declared.

      Previous declarations include declarations for base classes
      unless implementsOnly was used.

      This function is provided for convenience. It provides a more
      convenient way to call classImplements. For example::

        implements(I1)

      is equivalent to calling::

        classImplements(C, I1)

      after the class has been created.

      Consider the following example::


        >>> from zope.interface import Interface
        >>> class IA1(Interface): pass
        ...
        >>> class IA2(Interface): pass
        ...
        >>> class IB(Interface): pass
        ...
        >>> class IC(Interface): pass
        ...
        >>> class A(object):
        ...     implements(IA1, IA2)
        >>> class B(object):
        ...     implements(IB)

        >>> class C(A, B):
        ...    implements(IC)

        >>> ob = C()
        >>> int(IA1 in providedBy(ob))
        1
        >>> int(IA2 in providedBy(ob))
        1
        >>> int(IB in providedBy(ob))
        1
        >>> int(IC in providedBy(ob))
        1

      Instances of ``C`` implement ``I1``, ``I2``, and whatever interfaces
      instances of ``A`` and ``B`` implement.

      """
    pass


class TestRequest: #(BrowserRequest):
    """Browser request with a constructor convenient for testing
    """

    def __init__(self, body_instream=None, environ=None, form=None,
                 skin=None, **kw):

        pass


class SimpleTerm(object):
    """Simple tokenized term used by SimpleVocabulary."""

    def __init__(self, value, token=None, title=None):
        """Create a term for value and token. If token is omitted,
        str(value) is used for the token.  If title is provided, 
        term implements ITitledTokenizedTerm.
        """
        pass

class SimpleVocabulary(object):
    """Vocabulary that works from a sequence of terms."""

    def __init__(self, terms, *interfaces):
        """Initialize the vocabulary given a list of terms.

        The vocabulary keeps a reference to the list of terms passed
        in; it should never be modified while the vocabulary is used.

        One or more interfaces may also be provided so that alternate
        widgets may be bound without subclassing.
        """
        pass

    @staticmethod
    def fromItems(cls, items, *interfaces):
        """Construct a vocabulary from a list of (token, value) pairs.

        The order of the items is preserved as the order of the terms
        in the vocabulary.  Terms are created by calling the class
        method createTerm() with the pair (value, token).

        One or more interfaces may also be provided so that alternate
        widgets may be bound without subclassing.
        """
        pass

    @staticmethod
    def fromValues(cls, values, *interfaces):
        """Construct a vocabulary from a simple list.

        Values of the list become both the tokens and values of the
        terms in the vocabulary.  The order of the values is preserved
        as the order of the terms in the vocabulary.  Tokens are
        created by calling the class method createTerm() with the
        value as the only parameter.

        One or more interfaces may also be provided so that alternate
        widgets may be bound without subclassing.
        """
        pass
    
    @staticmethod
    def createTerm(cls, *args):
        """Create a single term from data.

        Subclasses may override this with a class method that creates
        a term of the appropriate type from the arguments.
        """
        pass

    def __contains__(self, value):
        """See zope.schema.interfaces.IBaseVocabulary"""
        pass

    def getTerm(self, value):
        """See zope.schema.interfaces.IBaseVocabulary"""
        pass

    def getTermByToken(self, token):
        """See zope.schema.interfaces.IVocabularyTokenized"""
        pass

    def __iter__(self):
        """See zope.schema.interfaces.IIterableVocabulary"""
        pass

    def __len__(self):
        """See zope.schema.interfaces.IIterableVocabulary"""
        pass
