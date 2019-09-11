class BaseObject(object):
    '''Base class. The attributes are used to store parameters of any type'''
    def __init__(self,name,**kwargs):
        self.name = name

        '''All keyword arguments are added as attributes.'''
        self.__dict__.update( kwargs )
        pass        
        
    def __str__(self):
        '''A useful printout'''
        header = '{type}: {name}'.format( type=self.__class__.__name__, name=self.name)
        varlines = ['\t{var:<15}:   {value}'.format(var=var, value=value) \
                    for var,value in sorted(vars(self).iteritems()) \
                    if var is not 'name']
        all = [ header ]
        all.extend(varlines)
        return '\n'.join( all )#
