# Copyright 2022 mockcube
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file

from setuptools import find_packages, setup

with open("README.md", "r") as file:
    long_description = file.read()

with open("VERSION", "r") as file:
    version = file.read()

package_data = {"": ["*"]}

install_requires = [
    "gym==0.17.2",
    "imageio-ffmpeg==0.4.2",
    "imageio==2.8.0",
    "matplotlib==3.2.1",
    "tensorflow-probability==0.12.2",
    "tensorflow==2.5.0",
    "tf-agents==0.8.0",
]

extras_require = {"mujoco-py": ["mujoco-py>=2.0,<2.1"]}

setup_kwargs = {
    "name": "bellman",
    "version": version,
    "description": "An Introduction to Machine Learning Algorithms in Python",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "license": "Apache License 2.0",
    "author": "mockcube",
    "author_email": "jorgehaniel1@gmail.com",
    "classifiers": [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    "keywords": "machine-learning reinforcement-learning deep-learning tensorflow",
    "maintainer": "mockcube",
    "maintainer_email": "jorgehaniel1@gmail.com",
    "url": "https://mockcube",
    "project_urls": {
        "Source on GitHub": "https://github.com/mockcube/Intro-to-ML-Algorithms",
        "Issue tracker": "https://github.com/mockcube/Intro-to-ML-Algorithms/issues",
        "Documentation": "https://mockcube/docs/latest",
    },
    "packages": find_packages(include=("*",)),
    "package_data": package_data,
    "install_requires": install_requires,
    "extras_require": extras_require,
    "python_requires": ">=3.7,<4.0",
}


setup(**setup_kwargs)
