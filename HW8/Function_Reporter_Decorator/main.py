from Decorator import FunctionReporter as fp



@fp("Report.txt")
def hello():
    return("Hello")



@fp("NewReport.txt")
def multi(n1,n2):
    return n1*n2


hello()
multi(5,9)

