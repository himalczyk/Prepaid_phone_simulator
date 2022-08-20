from setuptools import setup

setup(
    name='prepaid_phone_simulator',
    version='0.1',
    description='Oldschool prepaid phone simulator CLI app',
    url='https://github.com/himalczyk/Prepaid_phone_simulator',
    author='himalczyk',
    author_email='himalczyk1@gmail.com',
    license='unlicense',
    packages=['prepaid_phone_simulator'],
    install_requires=[
        'atomicwrites',
        'attrs',
        'certifi',
        'charset-normalizer',
        'colorama',
        'idna',
        'iniconfig',
        'packaging',
        'pluggy',
        'py',
        'PyJWT',
        'pyparsing',
        'pytest',
        'python-dotenv',
        'python-http-client',
        'pytz',
        'requests',
        'sendgrid',
        'starkbank-ecdsa',
        'tomli',
        'twilio',
        'urllib3',
    ],
    zip_safe=False
)