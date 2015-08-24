from OLiMS.dependencies.dependency import IQuerystringRegistryReader
from OLiMS.lims.querystring.querybuilder import RegistryConfiguration
from OLiMS.dependencies.dependency import \
    QuerystringRegistryReader as _QuerystringRegistryReader
from OLiMS.dependencies.dependency import IRegistry
from OLiMS.dependencies.dependency import getUtility
from OLiMS.dependencies.dependency import MessageFactory
from OLiMS.dependencies.dependency import implements


_p = MessageFactory('plone')


class QuerystringRegistryReader(_QuerystringRegistryReader):

    implements(IQuerystringRegistryReader)
    prefix = 'bika.lims.bika_catalog_query'

    def __call__(self):
        """Return the registry configuration in JSON format"""
        registry = getUtility(IRegistry)
        # First grab the base config, so we can use the operations
        registryreader = IQuerystringRegistryReader(registry)
        registryreader.prefix = "plone.app.querystring.operation"
        op_config = registryreader.parseRegistry()
        # Then combine our fields
        registryreader = IQuerystringRegistryReader(registry)
        registryreader.prefix = self.prefix
        config = registryreader.parseRegistry()
        config = registryreader.getVocabularyValues(config)
        config.update(op_config)
        registryreader.mapOperations(config)
        registryreader.mapSortableIndexes(config)
        return {
            'indexes': config.get(self.prefix + '.field'),
            'sortable_indexes': config.get('sortable'),
        }


_p = MessageFactory('plone')


class QueryRegistryConfiguration(RegistryConfiguration):
    prefix = 'bika.lims.bika_catalog_query'

