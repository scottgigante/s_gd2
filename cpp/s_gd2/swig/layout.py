# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info

if _swig_python_version_info >= (2, 7, 0):

    def swig_import_helper():
        import importlib

        pkg = __name__.rpartition(".")[0]
        mname = ".".join((pkg, "_layout")).lstrip(".")
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module("_layout")

    _layout = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):

    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module("_layout", [dirname(__file__)])
        except ImportError:
            import _layout

            return _layout
        try:
            _mod = imp.load_module("_layout", fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod

    _layout = swig_import_helper()
    del swig_import_helper
else:
    import _layout
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == "SwigPyObject":
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(
        "'%s' object has no attribute '%s'" % (class_type.__name__, name)
    )


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (
        self.__class__.__module__,
        self.__class__.__name__,
        strthis,
    )


try:
    _object = object
    _newclass = 1
except __builtin__.Exception:

    class _object:
        pass

    _newclass = 0


def dimension_check(kd):
    return _layout.dimension_check(kd)


dimension_check = _layout.dimension_check


def unweighted_edge_check(len_I, len_J):
    return _layout.unweighted_edge_check(len_I, len_J)


unweighted_edge_check = _layout.unweighted_edge_check


def weighted_edge_check(len_I, len_J, len_V):
    return _layout.weighted_edge_check(len_I, len_J, len_V)


weighted_edge_check = _layout.weighted_edge_check


def layout_unweighted(X, I, J, t_max, eps, rseed):
    return _layout.layout_unweighted(X, I, J, t_max, eps, rseed)


layout_unweighted = _layout.layout_unweighted


def layout_weighted(X, I, J, V, t_max, eps, rseed):
    return _layout.layout_weighted(X, I, J, V, t_max, eps, rseed)


layout_weighted = _layout.layout_weighted


def layout_unweighted_convergent(X, I, J, t_max, eps, delta, t_maxmax, rseed):
    return _layout.layout_unweighted_convergent(
        X, I, J, t_max, eps, delta, t_maxmax, rseed
    )


layout_unweighted_convergent = _layout.layout_unweighted_convergent


def layout_weighted_convergent(X, I, J, V, t_max, eps, delta, t_maxmax, rseed):
    return _layout.layout_weighted_convergent(
        X, I, J, V, t_max, eps, delta, t_maxmax, rseed
    )


layout_weighted_convergent = _layout.layout_weighted_convergent


def layout_sparse_unweighted(X, I, J, p, t_max, eps, rseed):
    return _layout.layout_sparse_unweighted(X, I, J, p, t_max, eps, rseed)


layout_sparse_unweighted = _layout.layout_sparse_unweighted


def layout_sparse_weighted(X, I, J, V, p, t_max, eps, rseed):
    return _layout.layout_sparse_weighted(X, I, J, V, p, t_max, eps, rseed)


layout_sparse_weighted = _layout.layout_sparse_weighted


def mds_direct(X, d, w, eta, rseed):
    return _layout.mds_direct(X, d, w, eta, rseed)


mds_direct = _layout.mds_direct
# This file is compatible with both classic and new-style classes.
