from setuptools import setup, find_packages

setup(
    name='sswa',
    version='1.0',
    description='simple scanner web app',
    author='Julian Kolesnikov',
    author_email='julyfortune101@gmail.com',
    packages=['sswa'],
    install_requires=[
        'aiohttp',
    ],
    entry_points={
        'console_scripts': [
            'serve_scanner=sswa.run_server:main'
        ],
    },
    python_requires=">=3.7",
)
