class StringSplitter:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING", {
                    "multiline": True, 
                    "default": "/app/server/input/"
                }),
            },
        }

    RETURN_TYPES = ("ZIPPED_STRING",)
    RETURN_NAMES = ("zipped_string",)
    OUTPUT_IS_LIST = (True,)


    FUNCTION = "dojob"

    #OUTPUT_NODE = False

    CATEGORY = "String Constructor/Splitter"

    def dojob(self, strings):
        print(f"""Your input contains:
            strings: {strings}
        """)
        return (strings.split(),)

    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""


class UnzipStrings:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"zipped_string": ("ZIPPED_STRING",), }}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "dojob"
    CATEGORY = "String Constructor/Splitter"
    def dojob(self, zipped_string):
        return zipped_string