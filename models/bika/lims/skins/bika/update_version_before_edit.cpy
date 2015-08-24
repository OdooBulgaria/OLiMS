## Script (Python) "update_version_on_edit"
##title=Edit Content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##

from dependencies.dependency import getToolByName
from dependencies.dependency import CMFEditionsMessageFactory as _
from dependencies.dependency import FileTooLargeToVersionError
from dependencies.dependency import isObjectChanged, maybeSaveVersion

pf = getToolByName(context, 'portal_factory')

if pf.isTemporary(context):
    # don't do anything if we're in the factory
    return state.set(status='success')

comment = _("Initial revision")
changed = isObjectChanged(context)

if not changed:
    return state.set(status='success')

try:
    maybeSaveVersion(context, comment=comment, force=False)
except FileTooLargeToVersionError:
    pass # the on edit save will emit a warning

return state.set(status='success')
