"""
KarmaParse
=========

* `development version
  <http://github.com/dcolish/Parser/zipball/master#egg=Parser-dev>`_
"""
from setuptools import setup, find_packages

setup(name="karmaparse",
      version="dev",
      packages=find_packages(),
      namespace_packages=['karmaparse'],
      include_package_data=True,
      author='',
      author_email='',
      description='',
      long_description=__doc__,
      zip_safe=False,
      platforms='any',
      license='',
      url='',

      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Unix',
        ],

      install_requires=[
        'ply',
        ],

      test_suite="nose.collector",
      tests_require=[
        'nose',
        ],
      )
