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
                    "default": "wolf"
                }),
                "sub_folder" : ("STRING", {
                    "multiline": False,
                    "default": "diffuse"
                }),
                "animation_name" : ("STRING", {
                    "multiline": False,
                    "default": "walk"
                }),
                "rotation" : ("STRING", {
                    "multiline": False,
                    "default": "0"
                }),
                "include_sub_folder": (["enable", "disable"],),
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "dojob"

    #OUTPUT_NODE = False

    CATEGORY = "String Constructor"

    def dojob(self, base_folder, model_folder, sub_folder, animation_name, rotation, include_sub_folder):
        print(f"""Your input contains:
            base_folder: {base_folder}
            model_folder: {model_folder}
            animation_name: {animation_name}
            rotation: {rotation}
        """)
        if include_sub_folder == "enable":
            return (base_folder + model_folder + "/" + sub_folder + "/" + animation_name+ "/" + rotation,)
        else:
            return (base_folder + model_folder + "/" +animation_name+ "/" + rotation,)

    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

