import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_fanstatic',
    'rebecca.fanstatic',
    'pyramid_debugtoolbar',
    'waitress',
    'js.bootstrap',
    'css.fontawesome',
    ]


setup(name='paulla.ldapmanager',
      version='0.0',
      description='paulla.ldapmanager',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Voileux',
      author_email='voileux@paulla.asso.fr',
      url='https://github.com/paulla/paulla.ldapmanager',
      keywords='web pyramid ldap manager',
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['paulla'], 
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="paulla.ldapmanager",
      entry_points="""\
      [paste.app_factory]
      main = paulla.ldapmanager:main
      """,
      )
