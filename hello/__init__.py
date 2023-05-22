def hello(uppercase: bool = False) -> str:
    if uppercase: # pragma: no cover
            return "HELLO"
    return "helloX"