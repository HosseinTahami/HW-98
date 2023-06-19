import sys 

def calculate_mark_average(marks) :
    total = sum(marks)
    average = total / len(marks)
    return average

if __name__ == "__main__":
    marks = sys.argv[1:]
    marks = [float(mark) for mark in marks]
    print("Average: ", calculate_mark_average(marks))