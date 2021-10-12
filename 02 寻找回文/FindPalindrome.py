'''
    寻找回文单词
'''
from os import replace
import sys
import random
import re

# 读取文件，并对文件进行预处理
def load(file):
    words = []
    try:
        with open(file) as in_file:
            lines = in_file.read().strip()
            if lines is not None:
                tempList = [re.sub('\n', '', ele)
                            for ele in lines.split(' ') if len(ele) > 1]
                tempList = [re.sub('[^a-zA-Z]', '', ele)
                            for ele in tempList]  # 正则表达式去除无效字符
                tempList = [ele.lower() for ele in tempList]  # 全部转换成小写
                palindromeList = [ele for ele in tempList if isPalindrome(
                    ele) == True and len(ele) > 1]  # 寻找回文字符串
                words.extend(palindromeList)
        return words
    except IOError as e:
        print(e)
    finally:
        in_file.close()


# 判断是否是回文单词
def isPalindrome(word):
    if word[::] == word[::-1]:
        return True


if __name__ == '__main__':
    file = 'C:/Python/Python Programming Practice by Lee Vaughan/02 寻找回文/RobertLouisStevenson.txt'
    words = load(file)
    print(words)


'''
re 详解：
'''