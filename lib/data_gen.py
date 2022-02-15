# -*- coding: utf-8 -*-
import pandas as pd
import data_clean as dc
import re

def gene_raw_txt(content,raw_name,ind):
    ## deal with raw data
    with open('{}_{}.txt'.format(raw_name,ind), 'w') as f:
        raw_lines = re.split('[?!…。？！]',content)
        for line in raw_lines:
            f.write(line + '\n')

def gene_doc_txt(content, doc_name, ind):
    ## deal with input data, The sentenceid may change because of trimming
    with open('{}_{}.txt'.format(doc_name,ind), 'w') as f:
        text = dc.preclean_cut(content)
        lines = re.split('[?!…。？！]',text)
        for line in lines:
            line = dc.postclean(line)
            f.write(line + '\n')

# Function： 将原文预处理后使用jieba分词，在将分词后结果按照句号断句，断句后的list在此经过后处理，删除无用的字符与内容
# Return：以分词后句子为单元的list
def contcut(content):
    text = dc.preclean_cut(content)
    lines = re.split('[?!…。？！]', text)
    ret = []
    for line in lines:
        line = dc.postclean(line)
        if '文章 来源' and '责任编辑' not in line:  # 为了去除类似单独句：（责任编辑：XXX）
            ret.append(line)
    return ret


# Function：将原文按句号分割后，将每句句首的序号删除后放入list
# Return： 返回以句子为单元的list
def cont(content):
    text=dc.remove_tab_enter(content)
    out=[]
    for ele in  re.split('[?!…。？！]', text):
        if '文章来源' and '责任编辑' not in ele:  # 为了去除类似单独句：（责任编辑：XXX）
            out.append(dc.remove_index(ele))
    return out

# Function：将原始DataFrame 输入后，经过分词及过滤等操作后返回统一字段的DataFrame

def gene_df(df):
    out=pd.DataFrame()
    out['content_cut'] = df.content.apply(lambda x: contcut(str(x)))
    out['content_raw'] = df.content.apply(lambda x: cont(str(x)))
    out['abstract']=df.abstract
    out['title'] = df.title
    # out['label'] = df.label
    return out


if __name__=='__main__':

    df = pd.read_csv('portal.csv')
    raw_name = 'raw'
    doc_name = 'doc'
    # for ind, content in enumerate(df.content):
    #     gene_raw_txt(content,raw_name,ind)
    #     gene_doc_txt(content,doc_name,ind)
