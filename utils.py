import xlrd
import pickle
from soynlp.normalizer import *

def parse_dict():
    norm = dict()
    for a in range(1,16):
        workbook = xlrd.open_workbook('data/'+str(a)+'.xls')
        worksheet = workbook.sheet_by_index(0)
        rows = worksheet.nrows

        for i in range(rows):
            data = worksheet.row_values(i)
            text = data[0].replace('(','').replace(')','').replace('-','').replace('^','')
            text = only_hangle(text)
            if len(text) < 2:
                continue
            norm[text] = 1

    with open('/data/dict/parsed_dict.pkl','wb') as f:
        pickle.dump(norm,f)


def nomarlize(corpus_path):
    f = open(+'data/' + corpus_path, 'rt', encoding='utf-8')
    w = open('data/norm_' + corpus_path, encoding='utf-8')
    corpus = only_hangle(corpus)
    corpus = emoticon_normalize(corpus, num_repeats=2)
    return corpus


if __name__ == "__main__":
    nomarlize('natepann1.txt')
