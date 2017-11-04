import datetime

def HelloWorldNow(speaker):
    today = datetime.date.today()
    info = speaker + ' says "Hello World" on ' + today.strftime('%d, %b %Y')
    return info

if __name__ == '__main__':
    print HelloWorldNow('Ming')
