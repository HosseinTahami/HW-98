from contextlib import contextmanager

class FileManager:
    def __init__(self, filename : str, mode : str):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_value, trace):
        self.file.close()
    
    def import_to_list(self) -> list :
        lines = []
        for line in self.file :
            lines.append(line)
        return lines
    
    def import_to_file(self, lines : list) :
        for line in lines :
            self.file.write(line)
    
        
input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file path: ")


with FileManager(input_file_path,"r") as file :
    lines = file.import_to_list()

with FileManager(output_file_path,"w") as file :
    file.import_to_file(lines)


#/home/hossein/Maktab98/Homeworks/HW10/Q6/first.txt
#/home/hossein/Maktab98/Homeworks/HW10/Q6/second.txt