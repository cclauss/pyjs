# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# Pyjamas Widget Factory.  register widgets with this module,
# for dynamic use in applications.  please observe namespaces.
#
# * pyjamas.ui namespace is used for widgets in library/pyjamas/ui

factory = {}

def registerClass(name, kls):
    global factory
    factory[name] = kls

def lookupClass(name):
    return factory[name]
