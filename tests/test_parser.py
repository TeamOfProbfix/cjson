from src.cjson_parser import CJSONParser

def test_parser():
    # File test chứa đủ các trường hợp: Object, Array, Boolean, Number, Null
    test_data = """
    {
      check_bool: true,
      check_num: 12345,
      check_null: null,
      nested: {
        list: [1, 2, 3],
        inner: { key: value }
      }
    }
    """
    
    parser = CJSONParser(test_data)
    result = parser.parse()
    
    # Kiểm tra các giá trị sau khi parse
    assert result["check_bool"] is True
    assert result["check_num"] == 12345
    assert result["check_null"] is None
    assert result["nested"]["list"] == [1, 2, 3]
    assert result["nested"]["inner"]["key"] == "value"
    
    print("Test passed successfully! .cjson is working as expected.")

if __name__ == "__main__":
    test_parser()
  
