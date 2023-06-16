class Indenter:
    def __init__(self):
        self.indent_number = -1

    def __enter__(self):
        self.indent_number += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_number -= 1

    def print(self, text):
        print("    " * self.indent_number + text)


with Indenter() as indent:
    indent.print("<A>")
    with indent:
        indent.print("<B>")
        with indent:
            indent.print("<C>")
    indent.print("<D>")
    
