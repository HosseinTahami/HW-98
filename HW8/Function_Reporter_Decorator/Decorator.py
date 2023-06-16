import datetime


class FunctionReporter:
    
    def __init__(self, fname:str = "Report.txt"):
        self.file = fname

        
    def __call__(self,function):
        def wrapper(*args,**kwargs):
            value = function(*args,**kwargs)
            run_date = datetime.datetime.now()
            f = open(self.file, "a")
            f.write(f"Function({function.__name__}) was called at {run_date} and returend {value} !\n")
            f.close()
            return value
        return wrapper
