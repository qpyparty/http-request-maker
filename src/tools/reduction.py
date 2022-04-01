def reduce(string: str) -> str:
    return string[:150] + "..." if len(string) > 150 else string
