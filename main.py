import dictionary
import filter
import utils
from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2


def main():

    Dict = dictionary.Dictionary()
    Dict.load_dict('parsed_dict.pkl')

    Filter = filter.Filter()
    Filter.load_noun_data('garbage_noun_list.txt')
    Filter.load_not_noun_data('garbage_not_noun_list.txt')

    word_list = []
    filter_noun_list = Filter.get_noun_data()
    filter_not_noun_list = Filter.get_not_noun_data()
    word_dict = Dict.get_data()

    corpus_path = 'data/norm_theqoo5.txt'
    sents = DoublespaceLineCorpus(corpus_path, iter_sent=True)
    noun_extractor = LRNounExtractor_v2(verbose=True)
    nouns = noun_extractor.train_extract(sents)

    nouns = {key: value for key, value in nouns.items() if  len(key) > 1}

    sorted_dict = sorted(nouns.items(), key=lambda item: item[1].frequency * item[1].score, reverse = True)

    cnt = 200
    for k,v in sorted_dict:
        #print(k + " " + str(int(v.frequency * v.score )), end = ' ')
        word_list.append(k)
        if cnt == 0:
            break
        cnt -= 1


    for word in word_list[:]:
        if word in word_dict :
            word_list.remove(word)
    
    for word in word_list[:]:
        if word in filter_noun_list: 
            word_list.remove(word)

    for word in word_list[:]:
        if word in filter_not_noun_list:
            word_list.remove(word)

    for word in word_list:    
        print(word,end=' ')


if __name__ == "__main__":
	main()