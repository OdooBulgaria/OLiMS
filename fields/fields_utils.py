import logging


_logger = logging.getLogger(__name__)


def boolean_value_base_mapper(obj, srcName, srcValue, dstName=None, dstValueTrue=True, \
                   dstValueFalse=False, deleteSrc=True):
    if dstName == None: dstName = srcName 
    
    try:
        if getattr(obj, srcName) == srcValue:
            setattr(obj, dstName, dstValueTrue)  
        else: 
            setattr(obj, dstName, dstValueFalse)
        if srcName != dstName and deleteSrc == True: delattr(obj, srcName) 
    except AttributeError:
        setattr(obj, dstName, dstValueFalse)

def direct_mapper(obj, srcName, dstName):    
    try:
        widget = getattr(obj, 'widget')
        _logger.warning('***** GOT srcName, dstName: %s, %s ****' % (srcName, dstName))
        _logger.warning('***** GOT widget: %r ****' % widget)
        value_from_widget = getattr(widget, srcName)
        _logger.warning('***** GOT value from widget: %r ****' % value_from_widget)
        
        setattr(obj, dstName, value_from_widget)  
        _logger.warning('***** CALLED setattr(%s, %s, %s) ****' % (obj, dstName, value_from_widget))
        _logger.warning('***** obj.help is now:%s' % obj.help)
    except AttributeError:
        setattr(obj, dstName, '')

