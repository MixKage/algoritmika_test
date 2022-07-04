from multiprocessing.connection import wait
from playsound import playsound
import asyncio


async def first_music():
    await asyncio.wait()
    playsound("C:\\Users\\opmax\\Desktop\\algoritmika_test\\algoritmika_test\\Maxim's workspace\\Sounds\\Milky_Ways.mp3")