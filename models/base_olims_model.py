def add_a_field(cls, field):
    setattr(cls, field.string, field)
    pass

def add_a_getter(cls, fieldname):
    def getterTemplate(cls):
        field = getattr(cls, fieldname)
        return field.__repr__()
        pass
    
    getterTemplate.__doc__ = "get%s - method to get value of field: %s" % (fieldname,fieldname)
    getterTemplate.__name__ = "get%s" % fieldname
    setattr(cls, getterTemplate.__name__, classmethod(getterTemplate))
    pass

class BaseOLiMSModel(object):
    '''
    This is the base class of all OLiMS model. In addition to models.Model, every OLiMS model will 
    be derived from this class and get all its code from a Bika Content class i.e. a Bika 
    content class will be converted to OLiMS model class by removing irrelevant code, 
    and adding derivation from this class, with the calling of following in the end
    
    DerivedModel_Of_BaseOLiMSModel.initialze(bika_schema)
    '''
           
    @classmethod
    def initialze(cls, schema):
        # take out each filed from the passed schema and:
        # 1. make a model variable for it, and assign this field to this variable
        # 2. make getter methods for each model variable defined in step 1
        for field in schema:
            add_a_field(cls, field)
            add_a_getter(cls, field.string)
            pass
        pass       
    pass
                                    

                    