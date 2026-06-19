# Self-Contained LogoUp3D Example Library

Use these snippets as the built-in replacement for local examples. Adapt dimensions, colors, and placement to the user's object.

## 1. Real Pencil

Use for pencil cases, book stands, desk organizers, stationery drones.

```logoup
FUNC SIMPLE_PENCIL_X @x, @y, @z, @len, @c
  CYLX @x, @y, @z, 3.2, @len, @c
  CYLX @x - @len / 2 - 5, @y, @z, 3.6, 10, RGB(245,145,180)
  CYLX @x - @len / 2 + 3, @y, @z, 3.4, 4, RGB(220,228,235)
  CYLX @x + @len / 2 + 4, @y, @z, 3.4, 8, RGB(222,160,76)
  DOT @x + @len / 2 + 10, @y, @z, 2.2, RGB(18,22,30)
  BOX @x, @y, @z + 4, @len * 0.86, 1.2, 1.2, 0, RGB(248,244,224)
END
```

For more realism, replace the body with a triangular sketch/BODY pencil, but keep it static if animation is slow.

## 2. Eraser, Ruler, Note, Chip

```logoup
FUNC ERASER @x, @y, @z
  BOX @x, @y, @z, 30, 19, 11, 4, RGB(246,145,180)
  BOX @x - 2, @y, @z + 6, 24, 14, 2, 2, RGB(248,244,224)
  BOX @x + 10, @y, @z + 1, 5, 20, 13, 1, RGB(86,166,220)
END

FUNC RULER @x, @y, @z
  BOX @x, @y, @z, 82, 9, 3, 1, RGBA(120,230,245,150)
  VAR r_i = 0
  REPEAT 9
    BOX @x - 36 + r_i * 9, @y, @z + 3, 1, 10, 3, 0, RGB(18,22,30)
    r_i = r_i + 1
  END
END

FUNC NOTE_PAD @x, @y, @z
  BOX @x, @y, @z, 34, 24, 4, 2, RGB(248,244,224)
  BOX @x, @y, @z + 4, 30, 20, 2, 1, RGB(120,210,245)
  BOX @x - 2, @y + 3, @z + 7, 21, 2, 2, 0, RGB(235,114,50)
END

FUNC CHIP @x, @y, @z
  BOX @x, @y, @z, 27, 20, 4, 2, RGB(42,134,78)
  BOX @x, @y, @z + 4, 14, 10, 3, 1, RGB(18,22,30)
  VAR pin_i = 0
  REPEAT 5
    BOX @x - 16, @y - 8 + pin_i * 4, @z + 3, 4, 1, 2, 0, RGB(236,185,48)
    BOX @x + 16, @y - 8 + pin_i * 4, @z + 3, 4, 1, 2, 0, RGB(236,185,48)
    pin_i = pin_i + 1
  END
END
```

## 3. Real Drawer Assembly

Use for pencil cases, lunch boxes, shoe racks, garbage bins, key trays, plant organizers.

```logoup
FUNC DRAWER_ASSEMBLY @slide
  BOX -62, -55, 26, 5, 48, 5, 1, RGB(220,228,235)
  BOX 62, -55, 26, 5, 48, 5, 1, RGB(220,228,235)
  BOX 0, -40, 27, 136, 8, 16, 3, RGB(14,44,82)
  BOX 0, -58 - @slide, 20, 122, 34, 8, 5, RGB(248,244,224)
  BOX -62, -58 - @slide, 33, 6, 34, 20, 2, RGB(28,105,174)
  BOX 62, -58 - @slide, 33, 6, 34, 20, 2, RGB(28,105,174)
  BOX 0, -41 - @slide, 33, 122, 6, 20, 2, RGB(28,105,174)
  BOX 0, -77 - @slide, 37, 132, 7, 26, 3, RGB(28,105,174)
  CYLX 0, -83 - @slide, 38, 3, 24, RGB(236,185,48)
END
```

Rule: `@slide` should normally be smaller than half the drawer depth.

## 4. Hinge Lid

Use for pencil boxes, lunch boxes, toothbrush covers, garbage lids, cases.

```logoup
VAR open_phase = ABS(SIN(90 * t))
CYLX 0, 57, 66, 4, 120, RGB(220,228,235)
PUSH
  MOVETO 0, 57, 70
  PITCH -70 * open_phase
  COLOR RGB(28,105,174)
  MOVE 0, -45, 8
  RCUBE 190, 90, 12, 10, 10
POP
```

The pivot is at the real hinge edge. The lid body must be offset away from the hinge after rotation.

## 5. Toothed Gear

Use for visible gear trains. Keep gear static helper separate from animation call.

```logoup
FUNC SAMPLE_GEAR @n, @h, @c
  FUNC SAMPLE_GEAR_SKETCH @n
    VAR smlr = @n - 1.8
    VAR bigr = @n + 1.8
    VAR ang = 360 / @n
    VAR theta = ang * 0.125
    VAR edge = SQRT(bigr * bigr + smlr * smlr - 2 * bigr * smlr * COS(theta))
    VAR alpha = ASIN(smlr * SIN(theta) / edge)
    VAR beta = (ang - 2 * theta) / (1 + bigr / smlr) / 2
    VAR gammar = ang - 2 * (beta + theta)
    GO bigr
    TURN 90
    DRAW
      REPEAT @n
        ARC bigr, beta * 2
        TURN 90 - alpha
        GO edge
        TURN 180 - (180 - alpha - theta) - 90
        ARC smlr, gammar
        TURN 90 - (180 - alpha - theta)
        GO edge
        TURN 90 - alpha
      END
    DONE
  END
  WIDTH 1
  OFFSET 0.5
  CIRC 5
  SAMPLE_GEAR_SKETCH @n
  FILL
  COLOR @c
  BODY
    UP @h
  DONE
  COLOR RGB(235,68,62)
  PUSH
    GO @n * 0.55
    RCUBE @n * 0.9, 3, @h + 4, 1, 1
  POP
  CLEAR
  UP 0 - @h
END
```

Animated call:

```logoup
RESET
SHIFT -30, 0
UP 60
TURN 4 * 360 * t / 15
SAMPLE_GEAR 15, 8, RGB(236,185,48)
RESET
SHIFT 10, 0
UP 60
TURN -4 * 360 * t / 20
TURN 7.8
SAMPLE_GEAR 20, 8, RGB(72,205,112)
RESET
```

## 6. Slider / Scanner

```logoup
VAR scan = -60 + 120 * ABS(SIN(90 * t))
BOX 0, 30, 50, 130, 4, 4, 1, RGB(170,182,194)
BOX scan, 30, 55, 18, 8, 8, 2, RGB(75,220,245)
BOX scan, 20, 50, 5, 40, 2, 1, RGBA(75,220,245,80)
```

## 7. Fan / Rotor

Use for ventilators, toothbrush holders, drying racks, desk fans.

```logoup
FUNC FAN @x, @y, @z, @spin
  BOX @x, @y, @z, 34, 12, 28, 5, RGB(18,22,30)
  PUSH
    MOVETO @x, @y - 8, @z + 2
    TURN @spin
    COLOR RGB(75,220,245)
    ELLIPSE 18, 4
    FILL
    EXTRUDE 1
    CLEAR
    TURN 90
    ELLIPSE 18, 4
    FILL
    EXTRUDE 1
    CLEAR
    COLOR RGB(248,248,238)
    CIRC 4
    FILL
    EXTRUDE 2
    CLEAR
  POP
END
```

## 8. Drone Rotor Module

Use for drones. All parts must connect: arm to motor center, motor to hub, ring to pod.

```logoup
FUNC GUARD_RING @x, @y, @z
  PUSH
    MOVETO @x, @y, @z
    COLOR RGBA(80,220,255,90)
    CIRC 32
    FILL
    ERASE ON
      CIRC 26
      FILL
    ERASE OFF
    EXTRUDE 2
    CLEAR
  POP
END

FUNC DRONE_ROTOR @x, @y, @z, @dir, @spin
  GUARD_RING @x, @y, @z
  BOX @x, @y, @z - 1, 58, 5, 4, 1, RGB(170,182,194)
  BOX @x, @y, @z - 1, 5, 58, 4, 1, RGB(170,182,194)
  CYL @x, @y, @z - 14, 12, 28, RGB(16,46,82)
  CYL @x, @y, @z + 1, 5, 9, RGB(220,228,235)
  PUSH
    MOVETO @x, @y, @z + 8
    TURN @dir * @spin
    COLOR RGBA(120,225,255,22)
    CIRC 30
    FILL
    EXTRUDE 1
    CLEAR
    PUSH
      TURN 6
      MOVE 19, 0, 0
      COLOR RGBA(245,250,255,235)
      ELLIPSE 27, 4
      FILL
      EXTRUDE 1
      CLEAR
      MOVE 18, 0, 1
      COLOR RGB(236,64,58)
      ELLIPSE 6, 3
      FILL
      EXTRUDE 1
      CLEAR
    POP
    PUSH
      TURN 186
      MOVE 19, 0, 0
      COLOR RGBA(210,245,255,220)
      ELLIPSE 27, 4
      FILL
      EXTRUDE 1
      CLEAR
      MOVE 18, 0, 1
      COLOR RGB(75,220,245)
      ELLIPSE 6, 3
      FILL
      EXTRUDE 1
      CLEAR
    POP
    COLOR RGB(236,64,58)
    CIRC 6
    FILL
    EXTRUDE 4
    CLEAR
  POP
END
```

Drone arms should use `BAR body_x, body_y, rotor_x, rotor_y, rotor_z, ...` so they visibly reach the motor center.

## 9. Winch Delivery

Use for drones, cranes, prize boxes, rescue devices.

```logoup
VAR drop = 18 + 34 * ABS(SIN(90 * t))
VAR winch_spin = 540 * t

FUNC WINCH @x, @y, @z
  BOX @x, @y, @z, 46, 18, 14, 5, RGB(8,24,45)
  PUSH
    MOVETO @x, @y, @z + 10
    PITCH 90
    TURN winch_spin
    COLOR RGB(236,185,48)
    RCYLINDER 8, 34, 1, 1
    COLOR RGB(236,64,58)
    RCUBE 2, 30, 3, 1, 1
  POP
  BOX @x, @y, @z - drop / 2, 3, 3, drop, 1, RGB(88,74,56)
  DOT @x, @y, @z - drop - 2, 4, RGB(236,185,48)
END
```

## 10. Toothbrush Rack Objects

```logoup
FUNC TOOTHBRUSH @x, @y, @z, @c
  BOX @x, @y, @z + 30, 6, 5, 58, 3, @c
  BOX @x, @y, @z + 63, 10, 7, 14, 3, RGB(248,248,238)
  VAR br = 0
  REPEAT 4
    BOX @x - 4 + br * 3, @y - 5, @z + 69, 2, 5, 9, 1, RGB(75,220,245)
    br = br + 1
  END
END
```

## 11. Plant Pot And Leaves

```logoup
FUNC LEAF @x, @y, @z, @ang
  PUSH
    MOVETO @x, @y, @z
    TURN @ang
    COLOR RGB(52,150,75)
    ELLIPSE 18, 7
    FILL
    EXTRUDE 2
    CLEAR
  POP
END
```

Use with pot, soil, stem, water drops, pump, and sensor screen.

## 12. Product Recipes

### AI pencil case

Main parts:
- rounded rectangular shell
- raised rim
- rear hinge barrels
- lid rotating around rear edge
- inner dividers
- real pencils/eraser/ruler/notes/chip
- front drawer on rails
- small screen/LEDs
- exposed gear pair or scanner

Animations:
- lid open around hinge
- drawer slide within rails
- gear pair spin or scanner sweep
- optional mechanical arm pushes one pencil

### Study lamp

Main parts:
- stable base with buttons/screen
- rear hinge
- lower arm
- second hinge
- lamp head and LED strip
- eye-protection sensors

Animations:
- arm pitch
- lamp head pitch/roll
- scanner light or brightness pulse

### Toothbrush sterilizer

Main parts:
- sink-top base
- toothbrush cup slots
- three toothbrushes and toothpaste
- transparent hinged dust cover
- UV light strip
- small fan

Animations:
- cover opens
- toothbrush tray lifts
- fan spins
- UV light pulses

### Plant pen cup

Main parts:
- pen cup with pencils/pens
- plant pot with soil/leaves
- water tank
- pump and pipe
- sensor screen
- small drawer

Animations:
- pump fan spins
- water drops move
- drawer slides
- screen blinks

### Drone

Main parts:
- fuselage
- four arms reaching rotor centers
- motor pods
- rotor guards with struts
- thin marked propellers
- landing skids
- camera/gimbal
- winch cable and payload

Animations:
- propellers rotate with colored tip/marker
- camera scans
- winch drum rotates and payload moves

## 13. Error Prevention

- If LogoUp says a variable is undefined, define it before first use.
- If LogoUp says a function/procedure parameter type mismatch, check that a variable name does not collide with a `FUNC` name.
- If animation buffers forever, reduce dynamic `DRAW/BODY` complexity and use simpler moving geometry.
- If a rotor appears static, slow it down and add one colored blade tip.
- If a part looks detached, add a physical bar, bracket, socket, screw, rail, hinge, cable, or overlapping contact pad.
- If a drawer detaches, shorten slide distance and lengthen fixed rails.
