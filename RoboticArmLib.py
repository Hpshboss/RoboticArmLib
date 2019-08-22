import serial
import sys
import os

class RoboticArm:
    def __init__(self, com_port, braudrate, AGV_arrive):
        self.comport = com_port
        self.braudrate = braudrate
        self.robotic_arm = serial.Serial(self.comport, self.braudrate, xonxoff=True, timeout=0.25)
        self.arm_jaw = True  # True means arm jaw is griping
        self.machine_jaw = True  # True means machine jaw is griping
        self.arm_move = False  # True means arm is moving
        self.arm_move_direction = False  # True means arm is moving into machine(arm_move=1)
                                         # or arm is in machine(arm_move=0)
        self.arm_taking_status = True  # True means arm is take workpiece in machine
        self.machine_running = False  # True means machine is running
        self.machine_door = True  # True machine means door is open
        self.AGV_arrive = AGV_arrive
        self.instructions1 = ("5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA")
        self.instructions2 = ("5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA")
        self.instructions3 = ("5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA")
        self.instructions4 = ("5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA",
                              "5MA")

    def G(self, machine_equipment):
        # AGV arrives at machine equipment 1
        if machine_equipment == 1:
            for instruction in self.instructions1:
                self.robotic_arm.write(instruction.encode() + os.linesep.encode())
                while True:
                    message = self.robotic_arm.readline(50)
                    print(message)
                    if message.find("Sync done".encode()) != -1:
                        break

        # AGV arrives at machine equipment 2
        if machine_equipment == 2:
            # wait door open
            while 1:
                if self.machine_door == 1:
                    for instruction in self.instructions1:
                        self.robotic_arm.write(instruction.encode() + os.linesep.encode())
                        while True:
                            message = self.robotic_arm.readline(50)
                            print(message)
                            if message.find("Sync done".encode()) != -1:
                                break
                    break

        # AGV arrives at machine equipment 3
        if machine_equipment == 3:
            # wait door open
            while 1:
                if self.machine_door == 1:
                    for instruction in self.instructions1:
                        self.robotic_arm.write(instruction.encode() + os.linesep.encode())
                        while True:
                            message = self.robotic_arm.readline(50)
                            print(message)
                            if message.find("Sync done".encode()) != -1:
                                break
                    break

        # AGV arrives at machine equipment 4
        if machine_equipment == 4:
            if self.machine_door == 1:
                for instruction in self.instructions1:
                    self.robotic_arm.write(instruction.encode() + os.linesep.encode())
                    while True:
                        message = self.robotic_arm.readline(50)
                        print(message)
                        if message.find("Sync done".encode()) != -1:
                            break