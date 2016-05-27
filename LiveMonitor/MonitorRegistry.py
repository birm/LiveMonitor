#Keep track of which monitors exist, so we can run them all
class MonitorRegistry(type):
    registry={} #keep track of things we need to register
    def __new__(cls,name,base,attributes):
        the_item=type.__new__(cls,name,base,attributes)
        cls.registry[the_item.__name__]=the_item
        return the_item

    @classmethod
    def whos(item):
        return dict(item.registry)
