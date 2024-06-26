#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Variáveis/objetos

# EV3
ev3 = EV3Brick()

# antih = motor C gira em anti-horário para subir a garra
mc = Motor(Port.C)
# Funções
def sobeGarra(mc):
    # parâmetro 1: 1000 = 100% de velocidade = 1000°/s, parâmetro 2: posição desejada em graus
    # faz o movimento anti-horário para subir a garra
    mc.run_target(500, -1000)
def desceGarra(mc):
    # faz o movimento horário para descer a garra
    mc.run_target(500, 0)
# teste
sobeGarra(mc)
desceGarra(mc)
