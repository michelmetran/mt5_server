"""
Summary

"""

from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

requirements = []
for line in open('requirements.txt', encoding='utf-8'):
    li = line.strip()
    if not li.startswith('#'):
        requirements.append(line.rstrip())


VERSION = (0, 0, 2)
__version__ = '.'.join(map(str, VERSION))


setup(
    name='mt5-server',
    version=__version__,
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Servidor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/michelmetran/mt5_server',
    keywords='python, metatrader',
    # Python and Packages
    python_requires='>=3',
    install_requires=requirements,
    # Entry
    # Our packages live under src but src is not a package itself
    # package_dir={'': 'sp_ff_apa_corumbatai'},
    # Quando são diversos módulos...
    packages=find_packages('.', exclude=['tests']),
    #packages=find_packages(),
    # Dados
    # include_package_data=True,
    # package_data={'': ['data/output/geo/*.7z']},
    # Classificação
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
)
