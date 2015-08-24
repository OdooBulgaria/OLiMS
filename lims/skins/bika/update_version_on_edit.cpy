## Script (Python) "update_version_on_edit"
##title=Edit Content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##

from OLiMS.dependencies.dependency import getToolByName
from OLiMS.dependencies.dependency import CMFEditionsMessageFactory as _
from OLiMS.dependencies.dependency import isObjectChanged, maybeSaveVersion
from OLiMS.dependencies.dependency import FileTooLargeToVersionError

putils = getToolByName(context, 'plone_utils')
REQUEST = context.REQUEST
comment = REQUEST.get('cmfeditions_version_comment', '')
force = REQUEST.get('cmfeditions_save_new_version', None) is not None

if not (isObjectChanged(context) or force):
    return state.set(status='success')

try:
    maybeSaveVersion(context, comment=comment, force=force)
except FileTooLargeToVersionError:
    putils.addPortalMessage(
        _("Versioning for this file has been disabled because it is too large"),
        type="warn"
        )

return state.set(status='success')
