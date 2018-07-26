#/usr/bin/env python3

import sys, pypinyin

def main():
    getPy = pypinyin.GetPinyin()
    getPy.load()
    print 'text getPy: '
    results = getPy.getPy("wo今天要抢红米，重庆是个好地方")
    for result in results:
        print result.py
    
    print 'test getMaxPy: '
    print getPy.getMaxPy('wo今天要抢红米，重庆是个好地方，我热爱江西')
    print getPy.getMaxPy('我是中国人，我热爱我的祖国，遇到重大事情，请报告组织')
    return 0
    

if __name__ == '__main__':
    sys.exit(main())
