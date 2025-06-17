import turtle as tr

def create_screen():
    wind = tr.Screen()
    wind.title("Ping Pong")
    wind.bgcolor("black")
    wind.setup(width=800, height=600)
    wind.tracer(0)
    return wind