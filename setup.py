from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in land_purchase_demo/__init__.py
from land_purchase_demo import __version__ as version

setup(
	name='land_purchase_demo',
	version=version,
	description='Frappe based custom application to handle land purchase-related workflow',
	author='kaviya',
	author_email='kaviyaperiyasamy22@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
