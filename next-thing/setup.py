from distutils.core import setup

from setuptools import find_packages

setup(
    name="next_thing",
    use_scm_version={
        "root": "..",
        "local_scheme": "node-and-timestamp",
        "relative_to": __file__,
    },
    description="Python custom thingy",
    author="John Weispfenning",
    install_requires=[],
    author_email="yourmom@blackhole.com",
    packages=find_packages(),
)
