# Copyright 2018, Alan Zaffetti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
"""testcase setup module.

See: https://github.com/ajzaff/testcase
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='testcase',
    version='0.1.0',
    description='Run tabular unit tests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ajzaff/testcase',
    author='Alan Zaffetti',
    author_email='ajzaff@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Unit',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tabular test development utility',
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ajzaff/testcase/issues',
        'Source': 'https://github.com/ajzaff/testcase/',
    },
)
