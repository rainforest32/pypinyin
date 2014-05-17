pypinyin
========

a python project for getting pinyin for Chinese words or sentence

给汉字注音的一个python库，基本上能正确处理多音字的注音问题

dependency
========

python2.6+, test on python2.7

jieba: https://github.com/fxsjy/jieba

interface
========

getPy: give a Chinese sentence, return all possible pinyin with frequency

	给定一段中文，返回所有可能的拼音和相应频率
	
getMaxPy: give a Chinsse sentence, return the pinyin with maximum frequency

	给定一段中文，返回最有可能的拼音

example
========

please read the test.py file

algorithm
========

please read my blog page in Chinese: http://www.smallqiao.com/124804.html

pypi
========

https://pypi.python.org/pypi/pythonpinyin/0.13
