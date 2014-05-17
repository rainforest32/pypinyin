#coding:gbk

import sys, os, jieba, unicode_tool

class PyInfo:
    def __init__(self):
        self.py = ''
        self.freq = 0

class GetPinyin:
    def __init__(self):
        self.is_load = False
        self.dict_path = os.path.split(os.path.realpath(__file__))[0] + '/py.txt'
        self.jieba_dict_path = os.path.split(os.path.realpath(__file__))[0] + '/dict.txt'
    
    def getMaxPy(self, sentence):
        if not self.is_load:
            self.load()
        sentence = unicode_tool.uniform(sentence)
        segs = jieba.cut(sentence)
        py_str = ''
        for seg in segs:
            if unicode_tool.is_chinese(seg[0]):
                if seg in self.pydict:
                    py = self.pydict[seg][0].py
                else:
                    py = seg
            else:
                py = seg
                
            if py_str == '':
                py_str = py
            else:
                py_str += ' ' + py
        return py_str
        
        
    def getPy(self, sentence):
        if not self.is_load:
            self.load()
        sentence = unicode_tool.uniform(sentence)
        segs = jieba.cut(sentence)
        pyInfoList = []
        for seg in segs:
            if unicode_tool.is_chinese(seg[0]):
                if seg in self.pydict:
                    pyInfos = self.pydict[seg]
                    pyInfoList.append(pyInfos)
                    continue
            pyInfo = PyInfo()
            pyInfo.py = seg
            pyInfo.freq = 1
            pyInfoList.append([ pyInfo ])
            
        results = []
        pyInfoListLen = len(pyInfoList)
        pos = [ 0 for i in range(pyInfoListLen)]
        max_pos = [ len(pyInfoList[i]) - 1 for i in range(pyInfoListLen)]
        
        while True:
            complete = True
            ri = PyInfo()
            ri.freq = 1
            for i in range(pyInfoListLen):
                if ri.py == '':
                    ri.py = pyInfoList[i][pos[i]].py
                else:
                    ri.py += ' ' + pyInfoList[i][pos[i]].py
                ri.freq *= pyInfoList[i][pos[i]].freq
            results.append(ri)
            
            for i in range(pyInfoListLen - 1, -1, -1):
                if pos[i] < max_pos[i]:
                    pos[i] += 1
                    complete = False
                    break
                else:
                    pos[i] = 0
            if complete:
                break
        return results
        
    
    def load(self):
        # load jieba first
        if not jieba.initialized:
            jieba.set_dictionary(self.jieba_dict_path)
            jieba.initialize()
        self.pydict = {}
        f = None
        try:
            f = open(self.dict_path)
            for line in f:
                try:
                    line = line.strip().decode('gbk')
                except:
                    continue
                sps = line.split('\t')
                if len(sps) != 3:
                    print >>sys.stderr, 'bad format line [%s]' % line
                    continue
                word = sps[0]
                py = sps[1]
                freq = float(sps[2])
                if word in self.pydict:
                    wordInfoLen = len(self.pydict[word])
                    i = 0
                    dup = False
                    while i < wordInfoLen:
                        if self.pydict[word][i].py == py:
                            if self.pydict[word][i].freq < freq:
                                self.pydict[word][i].freq = freq
                            dup = True
                            break
                        if self.pydict[word][i].freq < freq:
                            break
                        i += 1
                    if not dup:
                        pyInfo = PyInfo()
                        pyInfo.py = py
                        pyInfo.freq = freq
                        self.pydict[word].insert(i, pyInfo)
                        wordInfoLen += 1
                        for j in range(i + 1, wordInfoLen):
                            if self.pydict[word][j].py == py:
                                del self.pydict[word][j]
                                break
                else:
                    pyInfo = PyInfo()
                    pyInfo.py = py
                    pyInfo.freq = freq
                    self.pydict[word] = [ pyInfo ]
        except Exception, e:
            try:
                f.close()
            except:
                pass
            return False
        self.is_load = True
        return True