class StringCombinations:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "first_zipped": ("ZIPPED_STRING",), 
                "second_zipped": ("ZIPPED_STRING",), 
            },
        }

    RETURN_TYPES = ("ZIPPED_STRING","ZIPPED_STRING",)
    RETURN_NAMES = ("first string", "second string",)
    OUTPUT_IS_LIST = (True,True,)
    FUNCTION = "dojob"

    #OUTPUT_NODE = False

    CATEGORY = "String Constructor"

    def dojob(self, first_zipped, second_zipped):
         # Create all combinations of pairs from the two lists
        combinations = [(a, b) for a in first_zipped for b in second_zipped]
        first_elements = [a for a, b in combinations]
        second_elements = [b for a, b in combinations]
        return (first_elements, second_elements)

    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

