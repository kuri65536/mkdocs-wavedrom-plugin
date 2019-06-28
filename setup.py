# Copyright (c) 2019, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from setuptools import setup, find_packages  # type: ignore


def readme():
    # type: () -> str
    with open('README.md') as f:
        return f.read()


long_description = (
    "This is a mkdocs plugin, "
    "this could enable the wavedrom charts in the markdown file."
    "Please follow the 'how to' section in reame to enable this plugin"
)

setup(name='mkdocs-wavedrom-plugin',
      version='0.1.0',
      description='A MkDocs plugin for support '
                  'wavedrom charts in markdown file',
      long_description=long_description + "\n\n" + readme(),
      long_description_content_type='text/markdown',
      keywords='mkdocs python markdown wavedrom',
      url='https://github.com/kuri65536/mkdocs-wavedrom-plugin',
      author='Shimoda',
      author_email='kuri65536@hotmail.com',
      license='MPL2',
      python_requires='>=2.7',
      install_requires=['setuptools>=18.5',
                        'beautifulsoup4>=4.6.3',
                        'mkdocs>=1.0.4'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Information Technology',
                   'License :: OSI Approved :: '
                   'Mozilla Public License 2.0 (MPL 2.0)',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7'],
      packages=find_packages(exclude=['*.tests']),
      entry_points={'mkdocs.plugins': [
            'markdownwavedrom = markdownwavedrom.plugin:MarkdownWavedromPlugin'
      ]})
