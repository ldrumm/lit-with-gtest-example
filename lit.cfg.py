# -*- Python -*-

import os

import lit.formats

# name: The name of this test suite.
config.name = "lit-gtest-example"

# the lit googletest runner uses file extensions. There might be a way round it,
# but not sure
gtest_bin_suffix = '.test'

config.test_exec_root = lit_config.params.get('CMAKE_BINARY_DIR', 'build')
config.test_source_root = os.path.dirname(__file__)

# annoyingly this is expected to be a semicolon-separated string a'la cmake but
# for our purposes we're just using a single directory so it should be fine.
# It's also required to be a relative path e.g. 'build' where the binaries are,
# relative to this config file
gtest_subdirs = os.path.dirname(config.test_exec_root)

# suffixes: A list of file extensions to treat as test files. gtest has its own
# somewhat confusing discovery so let's be explicit about that here
config.suffixes = []

# testFormat: The test format to use to interpret tests.
config.test_format = lit.formats.GoogleTest(
    'build', # This is a bit funny it's the name of 
    gtest_bin_suffix,
)
