import utils

class Dictionary:
    
    data = None

    def load_dict(self, file_name):
        with open('data/' + file_name, 'rb') as f:
            data = utils.pickle.load(f)

    def get_data(self):
        return data