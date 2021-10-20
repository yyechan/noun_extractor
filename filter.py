import utils

class Filter:

    noun_data = []
    not_noun_data = []

    def load_noun_data(self, file_name):
        f = open('data/garbage/' + file_name, mode='r', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            self.noun_data.append(line.replace('\n',''))
        f.close()

    def load_not_noun_data(self, file_name):
        f = open('data/garbage/' + file_name, mode='r', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            self.not_noun_data.append(line.replace('\n',''))
        f.close()

    def get_noun_data(self):
        return self.noun_data
    
    def get_not_noun_data(self):
        return self.not_noun_data