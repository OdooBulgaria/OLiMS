class ATFolder : #(ATCTFolderMixin, BaseBTreeFolder):
    """ a folder suitable for holding a very large number of items """

    def getNextPreviousParentValue(self):
        """ If the parent node is also an IATFolder and has next/previous
            navigation enabled, then let this folder have it enabled by
            default as well """
        pass
class ATContentTypeSchema:
    """
    https://github.com/plone/Products.ATContentTypes/blob/master/Products/ATContentTypes/content/schemata.py
    """
    def __init__(self):
        pass
        
ATFolderSchema = ATContentTypeSchema.copy()    