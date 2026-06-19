# LogoUp Patterns From Local Examples

Use these idioms when writing detailed models.

## Contour First

For realistic objects, draw the side/top silhouette first, then make it solid:

```logoup
WIDTH 2
DRAW
  GO 80
  ARC 20, 90
  GO 40
  CLOSE
DONE
FILL
EXTRUDE 8
```

Examples:
- Airplane example 1: aircraft fuselage, wings, tail, wheel supports are all contour driven.
- Root drone example: rotor blade contours use `DRAW`, many `GO/TURN` segments, then `FILL` and `EXTRUDE`.
- Stationery example: pencil, book, set square, eraser, and pen use accurate profiles rather than box stacks.

## Hollow, Cut, And Recess

Use `ERASE ON/OFF` inside sketch construction for 2D holes. Use `SUBTRACT ON/OFF` to remove 3D volumes. Use `CAVE` for recessed cuts.

```logoup
CIRC 40
FILL
ERASE ON
CIRC 28
FILL
ERASE OFF
EXTRUDE 4
```

```logoup
COLOR light_green
CUBE 110, 110, 60
SUBTRACT ON
UP 2
CUBE 105, 105, 55
SUBTRACT OFF
```

Examples:
- Carved fan example: decorative fan holes are erased from the fan rib.
- Comb example: eyes and face are cut using `ERASE` and `SUBTRACT`.
- Root drone example: base shell is hollowed with `SUBTRACT`; center top uses `CAVE`.

## Curved Bodies And Lofting

Use `BODY ... LINK ... DONE` to connect sections. Change scale, yaw, pitch, roll, or position between links to make curved surfaces.

```logoup
CIRC 20
FILL
BODY
  SCALE 0.5
  JUMP 3
  LINK
DONE
```

Examples:
- Transparent cup example: a cup wall is built by rotating a profile with repeated `YAW` and `LINK`.
- Porcelain vase example: non-round decorative surfaces use `SCALEX` while yawing.
- Gourd example: stem and tendrils use repeated `PITCH/YAW/ROLL/UP`.
- Airplane example 2: fuselage is a lofted body with scale changes over height.

## Parametric Decorative Curves

Use `TO XFUNC/YFUNC` and `CURVE` for ornamental lines:

```logoup
TO ROSE @a, @n, @d
  VAR k = @n / @d
  FUNC XFUNC @theta
    RETURN @a * COS(k * @theta) * COS(@theta)
  END
  FUNC YFUNC @theta
    RETURN @a * COS(k * @theta) * SIN(@theta)
  END
  CURVE 0, 360 * @d, 720, XFUNC, YFUNC
END
```

Examples:
- Carved fan example: leaf, rose, heart, astroid, bicorn patterns.

## Arrays And Fine Details

Use loops for vents, grilles, keyboard keys, board lines, screw patterns, lattice windows, LED beads, and sensor arrays.

```logoup
VAR i = 0
REPEAT 12
  MOVETO -55 + i * 10, 0, 6
  RECT 5, 20
  FILL
  EXTRUDE 2
  i = i + 1
END
```

Examples:
- Electronic keyboard example: piano keys, speakers, buttons, screen.
- Go board example: board grid and hundreds of pieces.
- University gate example: repeated columns and layered architectural boards.

## Function Blocks

Write reusable `FUNC` helpers for meaningful parts, not just generic boxes: `ROTOR`, `HINGE`, `GEAR`, `LATTICE_PANEL`, `MOTOR_POD`, `BOOK`, `PENCIL`, `CABLE_DRUM`, `EGRET_CUTOUT`.

Use `PUSH/POP` around helpers that move the cursor or orientation.

## Static Checks

- Check `PUSH` equals `POP`.
- Check every `DRAW` and `BODY` has `DONE`.
- Check every `ERASE ON` has `ERASE OFF`.
- Check every `SUBTRACT ON` has `SUBTRACT OFF`.
- Avoid full-width punctuation in executable lines.
- Do not copy known corrupted example typos such as the bad comma in one gear example line.
