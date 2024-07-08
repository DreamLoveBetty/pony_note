import logging
logger = logging.getLogger(__name__)

class PonyStringMergerNode:
    def __init__(self):
        pass

    CATEGORY = "pony_yes_node❤❤❤/pony_string_merger"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset_option": ( 
                    [
                        "null",
                        "score_9, score_8_up, score_7_up, score_6_up, score_5_up",
                        "score_9, score_8_up, score_7_up, score_6_up,",
                        "score_1, score_2, score_3, score_4",
                        "score_1, score_2, score_3, score_4，score_5",
                    ],
                ),
            },
            "optional": {
                "extra_text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "user_text": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "start_index": ("INT", {"default": 0, "min": 0, "max": 2048, "step": 1}),
                "end_index": ("INT", {"default": 2048, "min": 0, "max": 2048, "step": 1}), 
                "chars_to_remove_list": ("STRING", {"default": "", "multiline": False, "placeholder": "Enter substrings separated by commas"}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filtered_string",)  # 更新返回名称以匹配英文习惯

    FUNCTION = "merge_and_filter_strings"
    
    def remove_chars(self, string, chars_to_remove_list):
        """Helper function to remove multiple specified substrings from a string."""
        # 确保输入是一个列表，即使只有一个元素
        if not isinstance(chars_to_remove_list, list):
            chars_to_remove_list = [chars_to_remove_list]
    
        # 遍历列表中的每个子串，依次从原字符串中移除
        for chars in chars_to_remove_list:
            string = string.replace(chars, "")
    
        return string

    def merge_and_filter_strings(self,preset_option,extra_text,user_text,start_index,end_index,chars_to_remove_list):
        
        try:
        # 处理特殊预设选项 "null"
            if preset_option == "null":
               preset_option = ""  # 将 "null" 视为空字符串处理
        
        # 结合预设字符串、额外文本和输入文本
            combined_string = f"{preset_option} {extra_text} {user_text}"
        
        # 根据索引截取字符串
            cropped_string = combined_string[start_index:end_index] if end_index is not None else combined_string[start_index:]
            
            chars_to_remove_str = chars_to_remove_list
        # 使用逗号作为默认分隔符将输入字符串分割成列表
            chars_remove_list = chars_to_remove_str.split(",") if chars_to_remove_str else []
        # 调用remove_chars方法时传入解析后的列表
            filtered_string = self.remove_chars(cropped_string, chars_remove_list)
        
            return (filtered_string,)
        except Exception as e:
            # 记录错误信息到日志
            logger.error(f"An error occurred in PonyStringMergerNode: {e}")
            raise  # 再次抛出异常，以便ComfyUI框架能捕捉到并处理

WEB_DIRECTORY = "./web"