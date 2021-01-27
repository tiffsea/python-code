import json
import pypandoc

class Convert_Json():

    def __init__(self, json_fp, h1):
        self.fp = json_fp
        self.h1 = h1
        self.jdata = self.get_json()
        self.mddata = self.format_json_to_md()

    def get_json(self):
        with open(self.fp) as f:
            res = json.load(f)
        return res

    def convert_json_to_txt(self, output_fn):
        with open(output_fn, 'w') as f:
            json.dump(self.jdata, f)
        print('Json file successfully converted to txt')

    def format_json_to_md(self):
        text = f'# {self.h1}\n'
        dct = self.jdata
        for header, data in dct.items():
            if "link" not in header:
                text += f'## {header}\n'
                if len(data) >= 0:
                    for content in data:
                        if type(content) == dict:
                            for k, v in content.items():
                                text += f'**{k}**: {v}\n\n'
                            text += '\n'
                        elif type(content) != dict:  # case of object properties as single string, not list
                            text += f'{content}'
        return text

    def convert_dict_to_md(self, output_fn):
        with open(output_fn, 'w') as writer:
            writer.writelines(self.mddata)
        print('Dict successfully converted to md')

    def convert_md_to_docx(self, output_fn):
        output = pypandoc.convert_text(self.mddata, 'docx', format='md', outputfile=output_fn)
        print('Md successfully converted to docx')

# # driver code - uncomment and fill out
# fn = 'FILENAME.json'
# title = "TITLE"
# converter = Convert_Json(fn, title)

# converter.convert_json_to_txt(output_fn='json-to-txt.txt') # uncomment for text output
# converter.convert_dict_to_md(output_fn='dict-to-md.md') # uncomment for markdown output
# converter.convert_md_to_docx(output_fn='md-to-docx.docx') # uncomment for Word output
