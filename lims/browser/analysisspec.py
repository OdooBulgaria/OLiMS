from OLiMS.lims.config import POINTS_OF_CAPTURE
from OLiMS.lims.interfaces import IAnalysisSpec
from OLiMS.lims.interfaces import IJSONReadExtender
from OLiMS.dependencies.dependency import adapts
from OLiMS.dependencies.dependency import implements

class JSONReadExtender(object):
    """Adds the UID to the ResultsRange dict.  This will go away
    when we stop using keywords for this stuff.
    """

    implements(IJSONReadExtender)
    adapts(IAnalysisSpec)

    def __init__(self, context):
        self.context = context

    def __call__(self, request, data):
        bsc = self.context.bika_setup_catalog
        rr = []
        for i, x in enumerate(data.get("ResultsRange", [])):
            keyword = x.get("keyword")
            proxies = bsc(portal_type="AnalysisService", getKeyword=keyword)
            if proxies:
                data['ResultsRange'][i]['uid'] = proxies[0].UID
