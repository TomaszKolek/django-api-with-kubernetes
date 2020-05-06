from random import randint

class ImageClassifier:
    def __init__(self, image_path):
        self.image_path = image_path

    def get_attributes(self):
        return {
            "score": randint(1, 100),
            "other score": randint(100, 300),
        }
