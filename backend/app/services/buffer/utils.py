import json
import os

buffer_path = "app/services/buffer/buffer.json"

def load_buffer():
    if os.path.exists(buffer_path) and os.path.getsize(buffer_path) > 0:
        with open(buffer_path, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def save_buffer(data):
    with open(buffer_path, "w") as file:
        json.dump(data, file, indent=4)

def write_prompt(query):
    data = load_buffer()
    if query not in data:
        data[query] = {'links': [], 'texts': []}
    save_buffer(data)

def write_link(prompt, link):
    data = load_buffer()
    if prompt not in data:
        write_prompt(prompt)
    data[prompt]['links'].append(link)
    save_buffer(data)

def write_text(prompt, text):
    data = load_buffer()
    if prompt not in data:
        write_prompt(prompt)
    data[prompt]['texts'].append(text)
    save_buffer(data)

def clear_buffer():
    save_buffer({})