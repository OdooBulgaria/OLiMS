from OLiMS.dependencies.dependency import DateTime
from OLiMS.dependencies.dependency import REFERENCE_CATALOG
from OLiMS.dependencies.dependency import WorkflowException
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims import logger
from OLiMS.lims.subscribers import skip
from OLiMS.lims.subscribers import doActionFor
# import App Plone/buildout-cache/eggs/Zope2-2.13.22-py2.7.egg/App
from OLiMS.dependencies import transaction

def AfterTransitionEventHandler(instance, event):

    # creation doesn't have a 'transition'
    if not event.transition:
        return

    debug_mode = True #App.config.getConfiguration().debug_mode "Commented by Yasir"
    if not debug_mode:
        return

    if not skip(instance, event.transition.id, peek=True):
        logger.debug("Started transition %s on %s" %
                    (event.transition.id, instance))
##    else:
##        logger.info("Ignored transition %s on %s" %
##                    (event.transition.id, instance))
