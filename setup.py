from distutils.core import setup 
setup(name='pypinyin',
      version='0.14',
      description='a python project for getting pinyin for Chinese words or sentence',
      author='Small Qiao',
      author_email='dlutwy@qq.com',
      url='http://www.smallqiao.com',
      packages = ['pypinyin'],
      package_dir={'pypinyin':'pypinyin'},
      package_data={'pypinyin':['*.*']}
) 
