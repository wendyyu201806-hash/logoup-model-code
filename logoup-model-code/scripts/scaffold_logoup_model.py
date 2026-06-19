#!/usr/bin/env python3
"""Print a high-detail LogoUp starter for competition-style invention models."""

import argparse


TEMPLATE = r"""// __NAME__
// High-detail scaffold: connected base, hollow shell, cutouts, cave recess,
// body/link curved part, Xiamen motifs, gears, spring, scanner, slider and gripper.

VAR t = INPUT_TIME(0, 0, 4, 25)
VAR phase = ABS(SIN(90 * t))
VAR pulse = ABS(SIN(360 * t))
VAR scan = -70 + 140 * ABS(SIN(180 * t))
VAR spin = 1080 * t
VAR slow = 240 * t
VAR open = ABS(SIN(90 * t))

VAR tech_blue = RGB(28, 98, 168)
VAR deep_blue = RGB(16, 48, 92)
VAR sea_teal = RGB(38, 178, 184)
VAR glass = RGBA(110, 230, 255, 115)
VAR scan_light = RGBA(0, 210, 255, 70)
VAR graphite = RGB(34, 39, 48)
VAR rubber = RGB(26, 30, 36)
VAR metal = RGB(155, 166, 178)
VAR light_metal = RGB(216, 224, 232)
VAR ivory = RGB(248, 244, 226)
VAR jade = RGB(52, 174, 122)
VAR gold = RGB(236, 176, 60)
VAR brick = RGB(174, 74, 50)
VAR porcelain = RGB(42, 96, 170)
VAR egret = RGB(246, 250, 250)
VAR warning = RGB(255, 92, 66)
VAR paper = RGB(250, 248, 232)
VAR ink = RGB(18, 24, 36)
VAR wood = RGB(205, 150, 86)

FUNC BOX @x, @y, @z, @l, @w, @h, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
  POP
END

FUNC CYL @x, @y, @z, @r, @h, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCYLINDER @r, @h, 1, 1
  POP
END

FUNC CYL_X @x, @y, @z, @r, @h, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    PITCH 90
    RCYLINDER @r, @h, 1, 1
  POP
END

FUNC DOT @x, @y, @z, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    BALL @r
  POP
END

FUNC SCREW @x, @y, @z
  PUSH
    COLOR metal
    MOVETO @x, @y, @z
    RCYLINDER 3.2, 1.2, 1, 1
    COLOR graphite
    RCUBE 5.5, 0.8, 0.9, 0, 0
    TURN 90
    RCUBE 5.5, 0.8, 0.9, 0, 0
  POP
END

FUNC HOLLOW_BOX @x, @y, @z, @l, @w, @h, @wall, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
    SUBTRACT ON
      MOVETO @x, @y, @z + @wall
      RCUBE @l - @wall * 2, @w - @wall * 2, @h, @r, @r
    SUBTRACT OFF
  POP
END

FUNC CAVE_SLOT @x, @y, @z, @l, @w, @d, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RRECT @l, @w, 3
    FILL
    CAVE @d
  POP
  CLEAR
END

FUNC CLOUD_CUT_PANEL @x, @y, @z, @w, @h, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RRECT @w, @h, 6
    FILL
    ERASE ON
      GOTO 0 - @w / 3, 0
      CIRC @h / 5
      FILL
      GOTO 0, 0
      CIRC @h / 4
      FILL
      GOTO @w / 3, 0
      CIRC @h / 5
      FILL
    ERASE OFF
    EXTRUDE 2
  POP
  CLEAR
END

FUNC LATTICE_PANEL @x, @y, @z, @w, @h, @c
  BOX @x, @y, @z, @w, 2.5, 3, 1, @c
  BOX @x, @y + @h, @z, @w, 2.5, 3, 1, @c
  BOX @x - @w / 2, @y + @h / 2, @z, 2.5, @h, 3, 1, @c
  BOX @x + @w / 2, @y + @h / 2, @z, 2.5, @h, 3, 1, @c
  VAR li = 1
  REPEAT 5
    BOX @x - @w / 2 + li * @w / 6, @y + @h / 2, @z + 1, 2.2, @h - 4, 2.2, 1, @c
    li = li + 1
  END
  VAR lj = 1
  REPEAT 3
    BOX @x, @y + lj * @h / 4, @z + 2, @w - 4, 2.2, 2.2, 1, @c
    lj = lj + 1
  END
END

FUNC PIANO_KEYS @x, @y, @z, @count
  VAR pk = 0
  REPEAT @count
    BOX @x + pk * 8, @y, @z, 7, 18, 3, 1, ivory
    IF pk - 3 * FLOOR(pk / 3) < 2 THEN
      BOX @x + pk * 8 + 2, @y + 5, @z + 3, 3.5, 10, 3, 1, ink
    END
    pk = pk + 1
  END
END

FUNC WAVE_STRIP @x, @y, @z, @seg, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    WIDTH 2
    DRAW
      VAR wi = 0
      REPEAT @seg
        ARC 8, 80
        ARC -8, 80
        wi = wi + 1
      END
    DONE
    EXTRUDE 1.5
  POP
  CLEAR
END

FUNC EGRET_BADGE @x, @y, @z, @s, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    SCALE @s
    WIDTH 2
    DRAW
      TURN -12
      GO 16
      TURN 64
      GO 26
      TURN -112
      GO 34
      TURN 140
      GO 26
      TURN -72
      GO 20
      TURN -116
      GO 18
      TURN -64
      GO 16
    DONE
    FILL
    EXTRUDE 1.6
  POP
  CLEAR
END

FUNC GEAR_DISC @x, @y, @z, @r, @teeth, @ang, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    TURN @ang
    RCYLINDER @r, 4, 1, 1
    VAR gt = 0
    REPEAT @teeth
      PUSH
        TURN gt * 360 / @teeth
        GO @r + 2
        RCUBE 5, 8, 4, 1, 1
      POP
      gt = gt + 1
    END
    COLOR graphite
    RCYLINDER @r / 3, 5, 1, 1
  POP
END

FUNC SPRING_Z @x, @y, @z, @turns, @height, @compress, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    OFFSET 5
    CIRC 1.2
    FILL
    BODY
      VAR si = 0
      REPEAT 36 * @turns
        YAW 10
        SHIFT 0, @height / (36 * @turns) * @compress
        LINK
        si = si + 1
      END
    DONE
  POP
  CLEAR
END

FUNC PROP_BLADES @x, @y, @z, @ang, @dir
  PUSH
    MOVETO @x, @y, @z
    TURN @ang * @dir
    VAR pb = 0
    REPEAT 4
      COLOR RGBA(232, 248, 255, 150)
      WIDTH 1.5
      DRAW
        GO 13
        TURN -25
        GO 42
        TURN 64
        GO 12
        TURN 55
        GO 40
        TURN 56
        GO 14
      DONE
      FILL
      EXTRUDE 1.8
      CLEAR
      TURN 90
      pb = pb + 1
    END
  POP
END

FUNC PENCIL @x, @y, @z, @len, @c
  BOX @x, @y, @z, @len, 5, 5, 2, @c
  BOX @x + @len / 2 + 5, @y, @z, 10, 5, 5, 1, wood
  DOT @x + @len / 2 + 11, @y, @z, 2.2, ink
  BOX @x - @len / 2 - 4, @y, @z, 8, 5, 5, 1, light_metal
END

FUNC BOOK @x, @y, @z, @w, @h, @c
  BOX @x, @y, @z, @w, @h, 6, 2, @c
  BOX @x, @y - @h / 2 + 2, @z + 4, @w - 6, 2, 2, 0, paper
  BOX @x, @y + @h / 2 - 2, @z + 4, @w - 6, 2, 2, 0, paper
  BOX @x - @w / 2 + 4, @y, @z + 4, 3, @h - 8, 2, 0, porcelain
END

FUNC SCREEN @x, @y, @z, @w, @h
  BOX @x, @y, @z, @w, @h, 3, 4, glass
  VAR sx = 0
  REPEAT 4
    BOX @x - @w / 2 + 12 + sx * 14, @y, @z + 3, 7, 2, 2, 1, sea_teal
    sx = sx + 1
  END
  DOT @x + @w / 2 - 10, @y, @z + 4, 3, RGB(50 + 180 * pulse, 220, 120)
END

// Connected Xiamen-style display base.
BOX 0, 0, -8, 260, 160, 8, 12, graphite
BOX 0, 0, -3, 238, 138, 4, 10, deep_blue
WAVE_STRIP -108, -72, 4, 11, sea_teal
WAVE_STRIP -108, 72, 4, 11, sea_teal
PIANO_KEYS -80, -86, 7, 20
BOX -98, 58, 8, 14, 8, 4, 1, brick
BOX -82, 58, 8, 14, 8, 4, 1, RGB(195, 92, 64)
BOX -66, 58, 8, 14, 8, 4, 1, brick
LATTICE_PANEL -95, -28, 18, 46, 34, gold
LATTICE_PANEL 48, -28, 18, 46, 34, gold
EGRET_BADGE 0, 58, 12, 0.75, egret

// Main object shell: hollow, recessed, and visibly bolted.
HOLLOW_BOX 0, 0, 30, 170, 88, 42, 5, 14, tech_blue
CAVE_SLOT 0, -46, 53, 112, 14, 4, glass
CLOUD_CUT_PANEL -52, 42, 55, 38, 16, gold
CLOUD_CUT_PANEL 52, 42, 55, 38, 16, gold
SCREEN 0, -48, 66, 64, 15
SCREW -72, -34, 58
SCREW 72, -34, 58
SCREW -72, 34, 58
SCREW 72, 34, 58

// Curved side pod made with BODY/LINK so the model is not box-only.
PUSH
  COLOR ivory
  MOVETO 0, 0, 70
  CIRC 24
  FILL
  BODY
    UP 14
    SCALE 0.88
    LINK
    UP 30
    SCALE 1.1
    LINK
    UP 44
    SCALE 0.7
    LINK
  DONE
POP
CLEAR

// Sliding rail, payload and scanner animation.
BOX -72, -24, 24, 5, 84, 5, 1, metal
BOX 72, -24, 24, 5, 84, 5, 1, metal
BOX 0, -76 - 48 * open, 27, 130, 48, 10, 6, ivory
PENCIL -34, -76 - 48 * open, 37, 62, gold
PENCIL 28, -76 - 48 * open, 37, 58, jade
BOOK 0, -48 - 48 * open, 39, 72, 34, porcelain
BOX scan, -80, 66, 5, 82, 2, 1, scan_light

// Exposed mechanism: gear pair, spring and prop/fan module.
GEAR_DISC -42, 20, 58, 18, 16, slow, sea_teal
GEAR_DISC -2, 20, 58, 13, 12, 0 - slow * 18 / 13, gold
SPRING_Z 55, 18, 42, 5, 44, 0.75 + 0.25 * open, gold
CYL 0, 0, 94, 13, 9, gold
PROP_BLADES 0, 0, 102, spin, 1

// Cable gripper that opens and closes around the payload.
BOX 0, 0, 88 - 42 * open / 2, 2.5, 2.5, 42 * open, 1, graphite
PUSH
  MOVETO -28 - 16 * open, 0, 62 - 42 * open
  YAW 18 * open
  COLOR gold
  RCUBE 8, 42, 8, 3, 3
  MOVE 0, 24, 0
  RCUBE 20, 6, 8, 3, 3
POP
PUSH
  MOVETO 28 + 16 * open, 0, 62 - 42 * open
  YAW 0 - 18 * open
  COLOR gold
  RCUBE 8, 42, 8, 3, 3
  MOVE 0, 24, 0
  RCUBE 20, 6, 8, 3, 3
POP
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs="?", default="Smart School Invention")
    args = parser.parse_args()
    print(TEMPLATE.replace("__NAME__", args.name))


if __name__ == "__main__":
    main()
