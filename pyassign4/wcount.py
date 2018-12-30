#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Cuiruoyao"
__pkuid__  = "1800011755"
__email__  = "1800011755@pku.edu.cn"
"""

import sys
import re
import urllib
from urllib.request import Request,urlopen
from urllib.error import URLError

'''maxStr和printtable两个函数是为了把结果转化为表格输出'''
def maxStr(Str):
    maxLen = 0
    for i in range(len(Str)):
        if len(Str[i]) > maxLen:
           maxLen = len(Str[i])
        else:
           pass
    return maxLen

def printTable(dictionary_):
    tableData=[]
    tableData.append(list(dictionary_.keys()))
    a=[]
    for i in list(dictionary_.values()):
        a.append(str(i))
    tableData.append(a)
    for column in range(len(tableData[0])):
        for row in range(len(tableData)):
            print(tableData[row][column].rjust(maxStr(tableData[row])+5),end='')
        print()


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    l=re.split('[.,:-^(){}?"\n\r!;\' /&#*@_]',lines)#将lines里的单词分隔，放入列表l
    statistics={}
    for i in  l:
        if i not in statistics:
            statistics[i]=1
        else:
            statistics[i]+=1 #用字典统计单词出现的次数
    list1=sorted(statistics.items(),key = lambda x:x[1],reverse = True) #将单词出现的次数由大到小排序
    if topn>len(list1):#超出单词种类数，输出全部结果
        dict1=dict(list1[1:]) #列表中的第一个元素是‘’ 要去掉
    else:
        dict1=dict(list1[1:topn+1])
    printTable(dict1)



if __name__ == '__main__':
    if  len(sys.argv) == 1: #只输入了文件名，没有输入网址
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
    else:
        req =Request(sys.argv[1])
        try: #尝试是否能拿到文本数据
            response = urlopen(req)
        except URLError as e: #如果网址捕获异常则返回错误类型
            if hasattr(e,"code"):
                print (e.code)
            if hasattr(e,"reason"):
                print (e.reason)
        else:
            netaddress=sys.argv[1]   #提取网址
            doc=urlopen(netaddress).read()  #获取网页内容
            m=doc.decode('utf-8') #py3的urlopen返回的不是string是bytes 需用decode解码 将doc由bytes转化为str类型进行操作
            n=m.lower(). #将文章中大写字母转化为小写
            if len(sys.argv)==2:  #如果没有输入topn数的话则输出前10个频率最高的词
                wcount(n,10)
            else:
                wcount(n,sys.argv[2])

    sys.exit(1)



