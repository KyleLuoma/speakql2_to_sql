
class SegmentFragment:

    def __init__(self, fragment_type, fragment_string):
        self.fragment_type = fragment_type
        self.fragment_string = fragment_string
        self.elements = []


    def get_fragment_string(self):
        return self.fragment_string
    

    def append_element(self, element):
        self.elements.append(element)


    def append_elements(self, element_list):
        self.elements = self.elements + element_list


    def to_string(self):
        return "Fragment type: " + self.fragment_type + ", Fragment: " + self.fragment_string