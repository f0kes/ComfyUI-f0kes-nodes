import os

def count_files_in_directory(directory_path):
    try:
        items = os.listdir(directory_path)
        files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
        return len(files)
    except Exception as e:
        return str(e)


class FileCounter:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "directory_path": ("STRING", {
                    "multiline": False, 
                    "default": "/app/server/input/"
                }),
            },
        }
    RETURN_TYPES = ("INT",)
    FUNCTION = "count_files"
    CATEGORY = "File"
    def count_files(self, directory_path):
        return (count_files_in_directory(directory_path),)