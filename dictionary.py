import utils

class Dictionary:
    
    data = None

    def load_dict(self, file_name):
        with open('data/dict/' + file_name, 'rb') as f:
            self.data = utils.pickle.load(f)

    def get_data(self):
        return self.data