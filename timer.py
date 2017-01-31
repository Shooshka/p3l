from threading import Timer
from appJar import gui

app = gui('Timers')

def timer(arg):
    t = Timer(float(app.getEntry(arg)), play, args=[arg])
    print('Таймер поставлен на {0} секунд'.format(int(app.getEntry(arg))))
    t.start()


def show_msg(desc):
    app.infoBox('Таймер сработал!', app.getEntry(desc))

def play(arg):
    desc = arg[0:5] + 'desc' + arg[9]
    app.playSound('FluteNotification.wav')
    show_msg(desc)


app.addLabel('timername1', 'Таймер1:', 0, 0)
app.addEntry('timername1', 0, 1)
app.addLabel('timerdesc1', 'Описание1:', 1, 0)
app.addEntry('timerdesc1', 1, 1)
app.addNamedButton('Start', 'timername1', timer)
app.addLabel('timername2', 'Таймер2:', 3, 0)
app.addEntry('timername2', 3, 1)
app.addLabel('timerdesc2', 'Описание2:', 4, 0)
app.addEntry('timerdesc2', 4, 1)
app.addNamedButton('Start', 'timername2', timer)
app.addLabel('timername3', 'Таймер3:', 6, 0)
app.addEntry('timername3', 6, 1)
app.addLabel('timerdesc3', 'Описание3:', 7, 0)
app.addEntry('timerdesc3', 7, 1)
app.addNamedButton('Start', 'timername3', timer)
app.go()
