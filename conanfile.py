#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostFunction_TypesConan(base.BoostBaseConan):
    name = "boost_function_types"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_function_types"
    lib_short_names = ["function_types"]
    header_only_libs = ["function_types"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_mpl",
        "boost_preprocessor",
        "boost_type_traits"
    ]


