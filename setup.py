import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()





setup(
    name="openedx_event_listener",
    version="17.0.0",
    url="",
    project_urls={
        "Code": "",
        "Issue tracker": "",
    },
    license="AGPLv3",
    author="author",
    author_email="john.doe@example.com",
    description="simple app to listen to openedx events",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=17.0.0,<18.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=17.0.0,<18.0.0",
            "Django>=2.2",
            "openedx-events",
            "requests",
            "attrs==23.2.0",
        ]
    },
    entry_points={
        "lms.djangoapp": [
            "demoplugin = openedx_event_listener.apps:MyAppConfig",
        ],
        "cms.djangoapp": [
            "demoplugin = openedx_event_listener.apps:MyAppConfig",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
