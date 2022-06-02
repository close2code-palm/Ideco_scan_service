from setuptools import setup, find_packages

setup(
    name='sswa',
    version='1.0',
    description='simple scanner web app',
    author='Julian Kolesnikov',
    author_email='julyfortune101@gmail.com',
    packages=['sswa'],
    url='https://github.com/close2code-palm/ideco_scan_service',
    install_requires=[
        'aiohttp',
        'python_version == 3.10',
    ],
)
