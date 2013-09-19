from setuptools import setup, find_packages

version = '0.1.0'

setup(name='PyCanvas',
      version=version,
      description="Python wrapper for Canvas API",
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: Development",
          "Environment :: Console",
          "Intended Audience :: End Users/Desktop",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: Private",
          ],
      keywords='canvas learning management api',
      author='Garrett Pennington',
      author_email='garrettp@gmail.com',
      url='http://github.com/kstateome/PyCanvas/',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      )