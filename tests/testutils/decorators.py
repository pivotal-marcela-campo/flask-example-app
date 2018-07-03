def before_decorator_factory(klass, func):
    class DecoratedKlass:
        def __init__(self, *args, **kwargs):
            self.oInstance = klass(*args, **kwargs)

        def __getattribute__(self,attr):
            try:
                x = super(DecoratedKlass,self).__getattribute__(attr)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(attr)
            if callable(x):
                return func(x)
            else:
                return x

    return DecoratedKlass


def logging_func(method):
    def curried_logging_func(*args, **kwargs):
        print('Calling method "{}" with arguments {},{}'.
              format(method, args, kwargs))
        print(args, kwargs)
        return method(*args, **kwargs)
    return curried_logging_func

def before_logging(klass):
    return before_decorator_factory(klass, logging_func)
