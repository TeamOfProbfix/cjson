import re

class CJSONParser:
    def __init__(self, cjson_text):
        # Tách token: Phân tách các phần tử cấu trúc {}[],: và các từ/số
        # Regex này đảm bảo không nhận diện các ký tự lạ, giữ tính thuần khiết
        self.tokens = re.findall(r'[{}\[\],:]|\w+|[0-9.-]+', cjson_text)
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        """Hàm duy nhất người dùng cần gọi để xử lý mọi dữ liệu"""
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
            
            # Xử lý số (Integer/Float)
            try:
                if '.' in token: return float(token)
                return int(token)
            except ValueError:
                return token # Trả về như một chuỗi nếu không phải các dạng trên

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

# --- CÁCH SỬ DỤNG CHO BẤT KỲ FILE NÀO ---
def load_cjson(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        return CJSONParser(content).parse()
          
