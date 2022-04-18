
class FragmentElement:

    def __init__(self, element_text):
        self.element_text = element_text



    def to_string(self):
        return "Element: " + self.element_text



    def as_dict(self):
        return {
            'element_string' : self.element_text
        }