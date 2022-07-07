from playsound import playsound


def first_music(bool):
    playsound("Maxim's workspace\Sounds\Milky_Ways.mp3", bool)
def failure_sound(bool):
    playsound("Sounds\\failure.wav", bool)
def success_sound(bool):
    playsound("Sounds\\success.wav", bool)