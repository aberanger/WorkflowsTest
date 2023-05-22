from hello import hello

def test_hello():
        assert hello() == "hello"
        
def test_hello_uppercase():
    assert hello(True) == "HELLO"