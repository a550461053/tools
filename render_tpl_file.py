# coding="utf-8"

from jinja2 import Template, Environment, FileSystemLoader

import os 
import sys

class RenderFile(object):
    def save_to_file(self, data, path):
        data_list = data.split('\n')
        with open(path, 'w') as file:
            for i in data_list:
                file.write(i + '\n')

    def render_to_file(self, file_path, input_file, output_file, json_data):
        env = Environment(loader=FileSystemLoader(file_path),
                            trim_blocks=True, 
                            lstrip_blocks=True)
        template = env.get_template(input_file)
        data = template.render(json_data)
        self.save_to_file(data, output_file)

# test

file_path = "./data"
input_file = "a.tpl"  # input_file tpl is just file_name.
output_file = "./data/b.yaml"  # output_file yaml is file_path.
json_data = {"a": 123, "b": True, "c": "666"}
RenderFile().render_to_file(file_path, input_file, output_file, json_data)

