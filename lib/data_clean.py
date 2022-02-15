# -*- coding: utf-8 -*-
import re,jieba
'''
输入：content 长文本
输出：分词后文本 空格隔开 'key1 key2 key3'
'''

def clean_cut(content):
    cleaned = preclean(content)
    cleaned = postclean(cleaned)
    out= jieba.cut(cleaned, cut_all=False)
    return ' '.join(out)

def preclean_cut(content):
    precleaned = preclean(content)
    out= jieba.cut(precleaned, cut_all=False)
    return ' '.join(out)

def preclean(text):
    text=strQ2B(text)
    text=text.replace(u'\u3000', u'')
    text=re.sub(r'\t+','',text)
    text=re.sub(r'\n+','',text)
    # text=re.sub('[【](.*?)[】]|_网易订阅|责任编辑|编辑','',text)
    text = re.sub('[【](.*?)[】]|_网易订阅', '', text)
    text=re.sub(r'[―・�=_|@━■▲^M〔〕〇●□↓◆③⊙╱★〉〈▼○E△ⅱ∶÷é④ⅲ±° ]','',text)
    text=re.sub('(www\.(.*?))|(http://(.*?))','',text.lower()) #去URL
    return text

def postclean(text):
    text=re.sub('[,，:「」￥…;"”“+/—!-%\[\]*◎《》、~`"\'‘’!?#$%^*()&\[\]{}:;\/\\><+-]','',text)   #去特殊字符
    text=re.sub('[\d]*[a-zA-Z]+[\d]*','',text)    #去英文
    text=re.sub('([\d]*年*[\d]*月*[\d]+日+)|([\d]+年+)|([\d]*年*[\d]+月+)','',text)    #去日期
    text=re.sub(r'\s+',' ',text)
    return text.strip()

def remove_tab_enter(text):
    text=text.strip()
    text=re.sub(r'\t+','',text)
    text=re.sub(r'\n+','',text)
    text=text.replace(u'\u3000', u'')
    return text

def remove_index(text):
    text = re.sub('^([\d|一|二|三|四|五|六|七|八|九|十]*)[)）、]', '', text)  # 删除句首的序号，如：2） 2、等
    text = re.sub('^[「(（【](.*?)[)）】」]','',text)
    text = re.sub('^[，、；！%#？\\\“”"\']+','',text)
    text = re.sub('^(其中|不过|而且|但是|此外|但|另外|另一方面|他表示|她表示)[,，、]*','',text)
    return text

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in str(ustring):
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring

'''
传入参数：
text = '我们 是 社会主义 接班人'
stopwords 为停用词表位置，文件中每行为一个停用词

输出参数：
经过停用词表过滤后的语句
return '社会主义 接班人'
'''
def scan_stopwords(text, stopwords):
    output = []
    stopw = [line.strip() for line in open(stopwords, 'r', encoding='utf-8').readlines()]
    for i in text.split(' '):
        if i not in stopw:
            output.append(i)
    return (' '.join(output)).strip()
