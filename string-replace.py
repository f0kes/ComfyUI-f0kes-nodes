class InputStringConstructor:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "base_folder": ("STRING", {
                    "multiline": False, 
                    "default": "/app/server/input/"
                }),
                "model_folder": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "diffuseWOLK/"
                }),
                "rotation" : ("STRING", {
                    "multiline": False,
                    "default": "0"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "String Constructor"

    def dojob(self, base_folder, model_folder, rotation):
        return base_folder + model_folder + rotation

    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "InputStringConstructor": InputStringConstructor
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "InputStringConstructor": "Input String Constructor Node"
}