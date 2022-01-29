from setuptools import setup

__project__ = "XMS-SMS"
__version__ = "0.0.1"
__description__ = "A Python module to read SMS binary files https://www.xmswiki.com/wiki/SMS:Binary_Dataset_Files_*.dat"
__packages__ = ["sms"]
__author__ = "A. Liakatas"
__author_email__ = "aristotelis.liakatas@gmail.com"
__url__ = "https://github.com/aliakatas/SMS_Binary"
__classifiers__ = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: MIT License",
    "Topic :: Scientific/Engineering",

]
__keywords__ = [
    "sms",
    "xms",
    "2D results",
    "floodmodeller",
]
__requires__ = [
    "pathlib",
    "pandas",
    "numpy",
]

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author= __author__,
    author_email= __author_email__,
    url=__url__,
    classifiers = __classifiers__,
    keywords=__keywords__,
    requires=__requires__,
    
)