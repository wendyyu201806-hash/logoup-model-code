# Self-Contained LogoUp3D Core Guide

This reference is the built-in baseline for LogoUp3D code generation. Use it when no local manual, PDF, or examples are available.

## Program Shape

LogoUp code is a sequential turtle-style 3D modeling language.

Common structure:

```logoup
VAR t = INPUT_TIME(0, 0, 4, 18)
VAR phase = ABS(SIN(90 * t))

COLOR RGB(40, 120, 200)
MOVETO 0, 0, 10
RCUBE 100, 60, 20, 8, 8
```

Use `FUNC` for reusable modules:

```logoup
FUNC BOX @x, @y, @z, @l, @w, @h, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
  POP
END
```

Use `PUSH/POP` around anything that changes position, rotation, scale, drawing state, or local coordinate system.

## Coordinates And Orientation

- `MOVETO x, y, z`: move to absolute 3D position.
- `MOVE dx, dy, dz`: move relative to current orientation.
- `SHIFT dx, dy`: move in current sketch plane.
- `UP dz`: move along current normal/up direction.
- `TURN a`: rotate in the current sketch plane.
- `YAW/PITCH/ROLL a`: rotate the 3D turtle.
- `RESET`: reset coordinate orientation and drawing state.
- `CLEAR`: clear current sketch path.
- `CLEARSKETCH`: clear sketch only.

Use absolute helper functions for product parts, e.g. `BOX`, `CYL`, `CYLX`, `DOT`, so repeated modules stay stable.

## Variables, Math, Loops

```logoup
VAR i = 0
REPEAT 8
  BOX -40 + i * 12, 0, 8, 8, 4, 4, 1, cyan
  i = i + 1
END
```

Useful math:

- `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ATAN2`
- `ABS`, `SQRT`, `EXP`, `ROUND`, `FLOOR`, `CEIL`
- `RGB(r,g,b)`, `RGBA(r,g,b,a)`, `HSV(h,s,v)`

Avoid variable names that match function names even by case. Use `gear_spin`, not `gear`, if a function `GEAR` exists.

## Sketch-To-Solid

Use sketch commands when real silhouettes matter.

```logoup
COLOR white
WIDTH 2
DRAW
  GO 50
  ARC 10, 90
  GO 20
  ARC 10, 90
  GO 50
  CLOSE
DONE
FILL
EXTRUDE 2
CLEAR
```

Key sketch commands:

- `DRAW ... DONE`: create a path.
- `GO d`: move forward in sketch plane.
- `GOTO x, y`: absolute sketch-plane move.
- `ARC r, angle`: arc.
- `CIRC r`, `ELLIPSE a, b`, `RECT w, h`, `RRECT w, h, r`, `SQUARE s`, `NGON n, r`.
- `FILL`: fill sketch.
- `EXTRUDE h`: turn filled sketch into solid.
- `CAVE d`: make recessed surface/cavity.

## Boolean And Holes

2D holes in sketches:

```logoup
CIRC 32
FILL
ERASE ON
  CIRC 24
  FILL
ERASE OFF
EXTRUDE 2
CLEAR
```

3D subtraction:

```logoup
COLOR blue
RCUBE 100, 60, 30, 8, 8
SUBTRACT ON
  MOVE 0, 0, 4
  RCUBE 86, 46, 28, 6, 6
SUBTRACT OFF
```

Always turn `ERASE` and `SUBTRACT` off.

## BODY/LINK Lofting

Use `BODY/LINK` for curved shells, cups, bottles, handles, cables, springs, propeller blades, and organic parts.

```logoup
COLOR cyan
CIRC 16
FILL
BODY
  UP 12
  SCALE 0.85
  LINK
  UP 28
  SCALE 1.2
  LINK
  UP 42
  SCALE 0.7
  LINK
DONE
CLEAR
```

For a spring:

```logoup
FUNC SPRING_Z @x, @y, @z, @turns, @height, @compress, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    OFFSET 5
    CIRC 1.2
    FILL
    BODY
      REPEAT 36 * @turns
        YAW 10
        SHIFT 0, @height / (36 * @turns) * @compress
        LINK
      END
    DONE
  POP
  CLEAR
END
```

## Animation

Animation begins with `INPUT_TIME`.

```logoup
VAR t = INPUT_TIME(0, 0, 4, 18)
VAR phase = ABS(SIN(90 * t))
VAR spin = 720 * t
VAR scan = -60 + 120 * ABS(SIN(90 * t))
```

Use time variables directly in visible geometry:

- Rotation: `TURN spin`, `PITCH 70 * phase`, `ROLL -45 * phase`
- Translation: `BOX scan, 0, 20, ...`
- Length: `BOX 0, 0, 40 - drop / 2, 3, 3, drop, ...`

Readable animation speeds:

- lids/drawers/arms: `ABS(SIN(90 * t))`
- scanner: `-60 + 120 * ABS(SIN(90 * t))`
- gear/fan/rotor: `360*t` to `900*t` if a marker is visible
- avoid extremely fast symmetric shapes because they can look static

## Mechanism Requirements

Each animation needs fixed and moving parts:

- Hinge: fixed hinge pin + moving lid/panel.
- Drawer: fixed rails + moving drawer box.
- Gear: toothed wheel + axle + marker + meshing gear/rack.
- Fan/rotor: fixed motor pod + rotating blade group + hub.
- Spring: fixed guide rod + coil + moving cap/load.
- Winch: fixed drum + rotating cylinder + cable + payload.
- Scanner: fixed rail + moving sensor/light beam.
- Linkage: pivot points + crank + rod + driven slider.

## Common Static Helpers

```logoup
FUNC BOX @x, @y, @z, @l, @w, @h, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
  POP
END

FUNC DOT @x, @y, @z, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    BALL @r
  POP
END

FUNC CYL @x, @y, @z, @r, @h, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCYLINDER @r, @h, 1, 1
  POP
END

FUNC CYLX @x, @y, @z, @r, @h, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    PITCH 90
    RCYLINDER @r, @h, 1, 1
  POP
END

FUNC BAR @x1, @y1, @x2, @y2, @z, @w, @h, @c
  PUSH
    VAR dx = @x2 - @x1
    VAR dy = @y2 - @y1
    VAR len = SQRT(dx * dx + dy * dy)
    VAR ang = ATAN2(dy, dx)
    COLOR @c
    MOVETO (@x1 + @x2) / 2, (@y1 + @y2) / 2, @z
    TURN ang
    RCUBE len, @w, @h, 3, 3
  POP
END
```

## Product Integrity Rules

- Main body is the largest readable object.
- Every functional part has a visible connection: hinge, bracket, rail, cable, socket, arm, screw, or clamp.
- The whole model must be one assembled product. Build a continuous load path from base -> main body -> upper structure.
- Upper parts may not float above the base. Screens, lids, lamps, handles, rotors, signs, sensors, shelves, covers, and decorative panels need visible side walls, posts, brackets, hinge barrels, rails, sockets, screw bosses, struts, cables, or molded supports.
- A base may not be an unrelated transparent/display slab unless explicitly requested. If there is a base, attach it with feet, bolts, rails, sockets, or molded product walls.
- Avoid floating detail pieces and disconnected top/bottom layers.
- Keep accessories inside or attached to product.
- If the model becomes hard to read, remove decoration and enlarge the mechanism.

## Validation Checklist

Before final answer:

```text
PUSH count == POP count
DRAW count + BODY count <= DONE count
ERASE ON count == ERASE OFF count
SUBTRACT ON count == SUBTRACT OFF count
No full-width comma in executable code
INPUT_TIME present for animated models
.txt and .logoup hashes match
The model has one clear main object
Top, middle, and base are visibly connected
Moving parts are visible from outside
No major part is disconnected
```
