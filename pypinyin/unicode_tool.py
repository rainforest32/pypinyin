#/usr/bin/env python3

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= '\u4e00' and uchar <= '\u9fa5':
        return True
    else:
        return False
 
def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= '\u0030' and uchar <= '\u0039':
        return True
    else:
        return False
 
def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= '\u0041' and uchar <= '\u005a') \
            or (uchar >= '\u0061' and uchar <= '\u007a'):
        return True
    else:
        return False
 
def is_other(uchar):
    """判断是否非汉字，数字和英文字符"""
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False
 
def B2Q(uchar):
    """半角转全角"""
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:
        # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
        return unichr(inside_code)
 
def Q2B(uchar):
    """全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:
        # 转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)
 
def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])
 
def uniform(ustring):
    """格式化字符串，完成全角转半角，大写转小写的工作"""
    return stringQ2B(ustring).lower()
