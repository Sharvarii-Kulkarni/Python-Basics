from datetime import datetime
def currentdatetime():
    n = datetime.now()
    formatted_datetime = n.strftime("%y-%m-%d %H:%M:%S")
    return formatted_datetime

print(currentdatetime())
