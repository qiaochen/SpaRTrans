# coding:utf-8

from distutils.core import setup
from transpa.version import __version__
setup(name='transpa',
      version=__version__,
      description='Translation-based imputation and cell type deconvolution',
      author='Chen Qiao',
      author_email='cqiao@connect.hku.hk',
      url='https://github.com/qiaochen/tranSpa',
      packages=['transpa'],
    #   entry_points = {
    #         "console_scripts": ['veloproj = veloproj.veloproj:main']
    #   },
      install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'tqdm',
        'torchmetrics',
        'anndata>=0.7.4',
        'scanpy>=1.5.1',
        'torch>=1.13.0',
        'umap-learn>=0.5.3',
        'torchvision>=0.14.0',
        'torchaudio',
        'scikit-learn',
        'squidpy',
      ]
    )