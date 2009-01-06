from distutils.core import setup, Extension

setup(
    name = "ssdeep",
    version = "2.0-0.1",
    author = "Jose Nazario",
    author_email = "jose@monkey.org",
    license = "GPL2",
    long_description = " ",
    ext_modules = [Extension(
        "ssdeepmodule",
        sources = ["ssdeep.c", "ssdeep_util.c"],
        include_dirs = [".."],
        libraries = ["fuzzy"],
        library_dirs = ["../.libs"]
        ) ],
    url = "http://code.google.com/p/pyssdeep/",
)
    

