#  (?<=(?<!\\)(?:\\{2})*)\*\*[^\\*]*(?:\\.[^\\*]*)*\*\*
import re
def markup(string_to_parse):
    """
    Returns parsed text with <html>
    :param string_to_parse: String to parse into HTML
    :return: returns html
    """
    bold_re=re.compile(r".*?(\*\*(.*?)\*\*).*?") # **bold**
    italic_re=re.compile(r".*?(''(.*?)'').*?")  # ''italics**
    image_re=re.compile(r".*?(![-(.*?)-]).*?")  # ![-image_id-]

    found_matches=re.findall(italic_re,string_to_parse)
    for match in found_matches:
        string_to_parse=string_to_parse.replace(match[0],"<i>"+match[1]+"</i>")
    found_matches=re.findall(bold_re,string_to_parse)
    for match in found_matches:
        string_to_parse=string_to_parse.replace(match[0],"<b>"+match[1]+"</b>")
    return string_to_parse.replace("\n","<br>")
def markup_list_descriptions(items_list):
    return_items=[]
    for item in items_list:
        item.description=markup(item.description)
        return_items.append(item)
    return return_items