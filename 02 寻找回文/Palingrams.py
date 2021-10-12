
"""寻找给定字典文件中的所有回文短语"""
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
                words.extend(tempList)
        return words
    except IOError as e:
        print(e)
    finally:
        in_file.close()

# 寻找回文短语
def find_palingrams(words):
    """寻找字典中的回文短语。"""
    pali_list = []
    for word in words:
        length = len(word)
        rev_word = word[::-1]
        if length > 1:
            for i in range(length):
                if word[i:] == rev_word[:length-i] and rev_word[length-i:] in words:
                    pali_list.append((word, rev_word[length-i:]))
                if word[:i] == rev_word[length-i:] and rev_word[:length-i] in words:
                    pali_list.append((rev_word[:length-i], word))
    return pali_list


if __name__ == '__main__':
    file = 'C:/Python/Python Programming Practice by Lee Vaughan/02 寻找回文/RobertLouisStevenson.txt'
    words = load(file)
    # print(words)

    palingrams = find_palingrams(words)

    # 根据短语的第一个单词，对回文短语进行排序
    palingrams_sorted = sorted(palingrams)

    # 输出回文短语列表
    print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
    for first, second in palingrams_sorted:
        print("{} {}".format(first, second))