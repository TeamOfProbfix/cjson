import re
import sys
import json

class CJSONParser:
    def __init__(self, cjson_text):
        # Tách token: ký tự cấu trúc hoặc các từ/số
        self.tokens = re.findall(r'[{}\[\],:]|\w+|[0-9.-]+', cjson_text)
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        return self._parse_value()

    def _parse_value(self):
        token = self._peek()
        
        if token == '{':
            return self._parse_object()
        elif token == '[':
            return self._parse_array()
        else:
            token = self._consume()
            # Logic Tag-free detection
            if token == 'true': return True
            if token == 'false': return False
            if token == 'null': return None
            
            # Xử lý Number
            try:
                if '.' in token: return float(token)
                return int(token)
            except ValueError:
                return token # String mặc định

    def _parse_object(self):
        self._consume() # Consume '{'
        obj = {}
        while self._peek() != '}':
            key = self._consume()
            self._consume() # Consume ':'
            obj[key] = self._parse_value()
            if self._peek() == ',':
                self._consume() # Consume ','
        self._consume() # Consume '}'
        return obj

    def _parse_array(self):
        self._consume() # Consume '['
        arr = []
        while self._peek() != ']':
            arr.append(self._parse_value())
            if self._peek() == ',':
                self._consume() # Consume ','
        self._consume() # Consume ']'
        return arr

def load_cjson(file_path):
    with open(file_path, 'r') as f:
        return CJSONParser(f.read()).parse()

# --- Phần CLI: Dùng để chạy trực tiếp trên Terminal ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cjson_parser.py <file.cjson>")
        sys.exit(1)
        
    try:
        data = load_cjson(sys.argv[1])
        # In ra JSON chuẩn để kiểm chứng
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error parsing .cjson: {e}")
        
