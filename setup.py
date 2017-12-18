from distutils.core import setup

setup(
    name='nis-python-client',
    version='0.0.9',
    packages=['', 'test'],
    url='https://github.com/semolex/nis-python-client',
    license='MIT',
    author='semolex (Oleksii Semeshchuk)',
    author_email='semolex@live.com',
    description='Python client for NEM NIS API (https://nemproject.github.io)',
    install_requires=[
        "requests",
        "requests-mock"
    ],
)
