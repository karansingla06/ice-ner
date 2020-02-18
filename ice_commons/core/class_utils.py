import logging
import collections

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_module(module_path):
    """
    :param module_path:
    :return:
    """
    return __import__(module_path, globals(), locals(), ['*'])


def get_function(dotted_package_name):
    """
    Retrieve a function object from a full dotted-package name.
    :param dotted_package_name:
    :return:
    """

    # Parse out the path, module, and function
    last_dot = dotted_package_name.rfind(".")
    func_name = dotted_package_name[last_dot + 1:]
    if last_dot == -1:
        module_path = '__main__'
    else:
        module_path = dotted_package_name[:last_dot]

    module = get_module(module_path)
    function_obj = getattr(module, func_name)

    # Assert that the function is a *callable* attribute.
    assert isinstance(function_obj, collections.Callable), "%s is not callable." % dotted_package_name

    # Return a reference to the function itself,
    # not the results of the function.
    return function_obj


def __get_class(class_name, parent_class=None):
    """
    Load a module and retrieve a class (NOT an instance).

    If the parent_class is supplied, className must be of parent_class
    or a subclass of parent_class (or None is returned).

    :param class_name:
    :param parent_class:
    :return:
    """
    clazz = get_function(class_name)

    # Assert that the class is a subclass of parent_class.

    if parent_class is not None:
        if not issubclass(clazz, parent_class):
            raise TypeError("%s is not a subclass of %s" %
                            (class_name, parent_class))

    # Return a reference to the class itself, not an instantiated object.
    return clazz


def create_instance(implementation, logger=None, **kwargs):
    """
    :param implementation:
    :param logger:
    :param kwargs:
    :return:
    """
    logger = logger or logging.getLogger(__name__)
    logger.info("creating instance of %s" % implementation)
    logger.info("params for instance %s" % kwargs)

    if implementation is not None:
        clazz = __get_class(implementation)
        return clazz(**kwargs)
