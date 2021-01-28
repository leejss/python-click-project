from setuptools import setup

setup(
    name = "sum-and-max",
    version = "0.1",
    description = "Compute sum and find max number in given numbers",
    author = "leejss",
    author_email = "goldemshine@gmail.com",
    py_modules = ["sum-and-max"],
    install_requires ="Click",
    entry_points = '''
        [console_scripts]
        compute=compute:compute
    '''


)