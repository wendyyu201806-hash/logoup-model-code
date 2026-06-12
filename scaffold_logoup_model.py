#!/usr/bin/env python3
"""Print a compact animated LogoUp starter model."""

import argparse


TEMPLATE = """// {name}
// Starter LogoUp model: animated lid, scanner, lights, and product body.

VAR t = INPUT_TIME(0, 0, 4, 25)
VAR open = ABS(SIN(90 * t))
VAR spin = 720 * t
VAR scan = -60 + 120 * ABS(SIN(180 * t))

VAR dark = RGB(35, 45, 60)
VAR blue = RGB(45, 130, 200)
VAR cyan = RGBA(80, 230, 255, 120)
VAR yellow = HSV(45, 85, 100)
VAR green = RGB(90, 245, 150)

FUNC BOX @x, @y, @z, @l, @w, @h, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
  POP
  CLEAR
  RESET
END

// Main rounded product body
BOX 0, 0, 0, 140, 86, 24, 12, blue
BOX 0, -46, 26, 88, 6, 28, 3, dark
BOX 0, -50, 36, 66, 2, 12, 2, cyan

// Animated lid or panel
PUSH
  MOVETO 0, 44, 28
  PITCH 0 - 65 * open
  MOVE 0, 34, 0
  COLOR RGB(240, 248, 255)
  RCUBE 130, 62, 6, 8, 8
  COLOR cyan
  MOVE 0, 0, 6
  RCUBE 88, 34, 2, 4, 4
POP
CLEAR
RESET

// Scanner
BOX scan, 0, 42, 5, 90, 2, 1, cyan

// Rotating technology ring
PUSH
  MOVETO 48, 0, 32
  PITCH 90
  TURN spin
  COLOR yellow
  CIRC 20
  CIRC 15
  FILL
  EXTRUDE 3
POP
CLEAR
RESET

// Status lights
BOX -36, -52, 54, 10, 2, 6, 1, yellow
BOX 0, -52, 54, 10, 2, 6, 1, green
BOX 36, -52, 54, 10, 2, 6, 1, yellow
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="?", default="智能校园发明")
    args = parser.parse_args()
    print(TEMPLATE.format(name=args.name))


if __name__ == "__main__":
    main()
