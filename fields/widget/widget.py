"""  
@author: yasir1brahim

"""

class Widget(object):
    _properties = {
        'description': '',
        'label': '',
        'visible': {'edit': 'visible', 'view': 'visible'},
        'condition': '',
    }
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)
    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __call__(self, mode, instance, context=None):
        """Not implemented."""
        return ''
    
class AnalysisProfileAnalysesWidget(Widget):
    
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
        
class StringWidget(Widget):
    _properties = Widget._properties.copy()
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)
    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0        
        
class TextAreaWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0      
        
class ComputedWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0  
        
class BooleanWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0      
        
class DecimalWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0      
        
class ReferenceWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
        
    def __len__(self):
        return 0      
 
class FileWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
        
    def __len__(self):
        return 0      
        
class MultiSelectionWidget(Widget):
    _properties = Widget._properties.copy()
    
    def __init__(self, *args, **kwargs):
        self._process_args(**kwargs)

    def _process_args(self, **kwargs):
        self.__dict__.update(self._properties)
        self.__dict__.update(kwargs)
    def __len__(self):
        return 0