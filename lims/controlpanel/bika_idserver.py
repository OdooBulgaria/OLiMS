from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import InitializeClass
from OLiMS.dependencies.dependency import SimpleItem
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.interfaces import IIdServer
from OLiMS.dependencies.dependency import implements
from OLiMS.dependencies.dependency import sha1
import App,os,sys,random,time,urllib,hmac

try:
    from OLiMS.dependencies.dependency import getSite
except:
    # Plone < 4.3
    from OLiMS.dependencies.dependency import getSite

class IDServerUnavailable(Exception):
    pass

class bika_idserver(object):

    implements(IIdServer)
    security = ClassSecurityInfo()

    security.declarePublic('generate_id')
    def generate_id(self, portal_type, batch_size = None):
        """ Generate a new id for 'portal_type'
        """
        plone = getSite()
        portal_id = plone.getId()

        if portal_type == 'News Item':
            portal_type = 'NewsItem'

        idserver_url = os.environ.get('IDServerURL')
        try:
            if batch_size:
                # GET
                f = urllib.urlopen('%s/%s%s?%s' % (
                        idserver_url,
                        portal_id,
                        portal_type,
                        urllib.urlencode({'batch_size': batch_size}))
                        )
            else:
                f = urllib.urlopen('%s/%s%s' % (
                    idserver_url, portal_id, portal_type
                    )
                )
            id = f.read()
            f.close()
        except:
            from sys import exc_info
            info = exc_info()
            import zLOG; zLOG.LOG('INFO', 0, '', 'generate_id raised exception: %s, %s \n idserver_url: %s' % (info[0], info[1], idserver_url))
            raise IDServerUnavailable(_('ID Server unavailable'))
        return id
