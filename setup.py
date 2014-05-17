from distutils.core import setup 
setup(name='pythonpinyin',
      version='0.13',
      description='a python project for getting pinyin for Chinese words or sentence',
      author='Small Qiao',
      author_email='dlutwy@qq.com',
      url='http://www.smallqiao.com',
      packages = ['pypinyin'],
      package_dir={'pypinyin':'pypinyin'},
      package_data={'pypinyin':['*.*']}
) 
