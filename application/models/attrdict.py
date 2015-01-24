class attrdict(dict):
    def __init__(self, *args, **kwargs) :
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self
    def retrieve(self, key, value) :
        if key in self :
            return self[key]
        else :
            self[key] = value
            return value