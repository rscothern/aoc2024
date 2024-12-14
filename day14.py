#!/usr/local/bin/python3

from map import Pos

from dataclasses import dataclass
from collections import defaultdict, namedtuple

Vel = Pos

@dataclass
class Robot():
    id: int
    pos: Pos
    vel: Vel

    def move(self):
        self.pos = Pos(self.pos.x + self.vel.x, self.pos.y + self.vel.y)


Quardrant = namedtuple("Pos", "top_left bottom_right")

def read_robots(filename):
    with open(filename, "r") as f:
        robot_data = []
        for i, line in enumerate(f.readlines()):
            pos, vel = line.strip().split()
            x, y = pos.split("=")[1].split(",")
            startpos = Pos(int(x), int(y))
            x, y = vel.split("=")[1].split(",")
            velocity = Vel(int(x), int(y))
            robot_data.append(Robot(i, startpos, velocity))
        return robot_data

def move_robots(robot_data, width, height):
    for robot in robot_data:
        robot.move()
        new_pos = robot.pos
        x = new_pos.x
        y = new_pos.y
        if new_pos.x < 0:
            x = new_pos.x + width
        if new_pos.x >= width:
            x = new_pos.x - width
        if new_pos.y < 0:
            y = new_pos.y + height
        if new_pos.y >= height:
            y = new_pos.y - height

        robot.pos = Pos(x,y)

def within_quadrant(quadrant, pos):
    return all(
        [quadrant.top_left.x <= pos.x <= quadrant.bottom_right.x,
         quadrant.top_left.y <= pos.y <= quadrant.bottom_right.y])


def calc_safety_factor(filename, width, height, seconds):
    robots = read_robots(filename)
    for _ in range(seconds):
        move_robots(robots, width, height)

    quadrant_counts = defaultdict(int)
    top_left = Quardrant(Pos(0,0), Pos(int(width/2) - 1, int(height/2-1)))
    top_right = Quardrant(Pos(int(width/2+1), 0), Pos(width, int(height/2-1)))
    bottom_left = Quardrant(Pos(0, int(height/2+1)), Pos(int(width/2-1), height))
    bottom_right = Quardrant(Pos(int(width/2)+1, int(height/2+1)), Pos(width, height))
    quadrants = [top_left, top_right, bottom_left, bottom_right]
    for robot in robots:
        for quadrant in quadrants:
            if within_quadrant(quadrant, robot.pos):
                quadrant_counts[repr(quadrant)] += 1

    safety_factor = 1
    for count in quadrant_counts.values():
        safety_factor *= count

    return safety_factor

assert calc_safety_factor("day14ex.txt", 11, 7, 100) == 12
assert calc_safety_factor("day14.txt", 101, 103, 100) == 217328832
