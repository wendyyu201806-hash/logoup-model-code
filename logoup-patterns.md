# LogoUp Code Patterns

## Animated Starter

```logoup
VAR t = INPUT_TIME(0, 0, 4, 25)
VAR open = ABS(SIN(90 * t))
VAR spin = 720 * t
VAR scan = -60 + 120 * ABS(SIN(180 * t))
```

Use `open` for lids, drawers, claws, and folding parts. Use `spin` for wheels, gears, propellers, and fans. Use `scan` for light bars and sensors.

## Helper Functions

```logoup
FUNC BOX @x, @y, @z, @l, @w, @h, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    RCUBE @l, @w, @h, @r, @r
  POP
  CLEAR
  RESET
END

FUNC DOT @x, @y, @z, @r, @c
  PUSH
    COLOR @c
    MOVETO @x, @y, @z
    BALL @r
  POP
  CLEAR
  RESET
END
```

## Common Showcase Motions

- Lid opening: `PITCH 0 - 70 * open`.
- Drawer sliding: `MOVETO x, y - 45 * open, z`.
- Scanning light: `BOX scan, y, z, 5, 100, 2, 1, cyan`.
- Gear or wheel: `TURN spin` before `RCYLINDER` or gear sketch.
- Hovering: `VAR hover = 10 * SIN(180 * t)` and add `hover` to z positions.
- Blinking: `RGB(255, 100 + 120 * ABS(SIN(360 * t)), 70)`.

## Model Structure

1. Comments naming the invention and animation.
2. `INPUT_TIME` and animation variables.
3. Color variables.
4. Helper functions.
5. Main object body.
6. Functional modules.
7. Animated parts.
8. Scene base or context objects.

## Design Ideas For School Inventions

- Smart desk organizer, pencil case, backpack cart, water cup, lunch box, reading stand, air purifier, safety bracelet, plant monitor, sleep alarm.
- Add technology signs: screen, camera, radar ring, sensor dots, LED strip, wireless charging ring, solar panel, mechanical arm.
- Add life context: book, pencil, homework page, classroom desk, school road, name tag, storage bin.
