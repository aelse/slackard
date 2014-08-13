from setuptools import setup
import os.path
__dir__ = os.path.dirname(os.path.abspath(__file__))

setup(
    name='slackard',
    license='BSD',
    py_modules=['slackard'],
    version='1.0.1',
    install_requires=['PyYAML', 'requests', 'slacker'],

    description='A pluggable bot for slack.com',
    long_description='See https://github.com/aelse/slackard',

    author='Alexander Else',
    author_email='aelse@else.id.au',
    url='https://github.com/aelse/slackard',

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Communications :: Chat",
        "Topic :: Office/Business :: Groupware",
    ],

    entry_points={
        'console_scripts': ['slackard=slackard:main'],
    }
)
