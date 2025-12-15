import urllib.request
import re


class MyFile:
    def __init__(self, path, mode="read"):
        self.path = path
        self.mode = mode
        
        if mode not in ["read", "write", "append", "url"]:
            raise ValueError(f"Недопустимый режим: {mode}")
    
    def read(self):
        if self.mode != "read":
            raise ValueError("Режим не поддерживает чтение")
        
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {self.path}")
        except Exception as e:
            raise Exception(f"Ошибка чтения: {e}")
    
    def write(self, text):
        if self.mode not in ["write", "append"]:
            raise ValueError("Режим не поддерживает запись")
        
        mode = 'w' if self.mode == 'write' else 'a'
        
        try:
            with open(self.path, mode, encoding='utf-8') as f:
                return f.write(text)
        except Exception as e:
            raise Exception(f"Ошибка записи: {e}")
    
    def read_url(self):
        if self.mode != "url":
            raise ValueError("Режим не поддерживает URL")
        
        try:
            with urllib.request.urlopen(self.path, timeout=5) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            raise Exception(f"Ошибка чтения URL: {e}")
    
    def count_urls(self):
        content = self.read_url()
        urls = re.findall(r'https?://[^\s"\'<>]+', content)
        return len(urls)
    
    def write_url(self, filepath):
        content = self.read_url()
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                return f.write(content)
        except Exception as e:
            raise Exception(f"Ошибка записи в файл: {e}")



file = MyFile("test.txt", "write")
file.write("Привет, мир!")
    
file = MyFile("test.txt", "read")
print(file.read())
    

file = MyFile("test.txt", "append")
file.write("привет!")
    

file = MyFile("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat", "url")
text = file.read_url()
print(text[:200])
print(f"Найдено URL: {file.count_urls()}")
file.write_url("text.txt")