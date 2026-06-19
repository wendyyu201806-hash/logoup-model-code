# Mechanical Animation Reference For LogoUp

Use this before generating animated models.

## Lessons From Local Animation Examples

- Crank linkage example: computes the second link angle with `ASIN(GETY() / h2)`, so motion is constrained by link length.
- Gear train example: rotates meshing gears in opposite directions with radius/tooth-count ratios.
- Spring example: uses `BODY`, repeated `YAW`, `SHIFT`, and `LINK`; compression changes the step length over time.
- Damped swing example: uses `COS(360 * t) * angle * EXP(-t * damping)`.
- Deforming ring example: animates a body with repeated `ROLL`, `YAW`, and `LINK`.

## Animation Variables

```logoup
VAR t = INPUT_TIME(0, 0, 4, 25)
VAR phase = ABS(SIN(90 * t))
VAR spin = 720 * t
VAR scan = -60 + 120 * ABS(SIN(180 * t))
VAR pulse = ABS(SIN(360 * t))
```

## Mechanism Requirements

Every moving module needs both moving and fixed geometry:

- Rotor: motor pod, axle, guard ring or bracket, blades.
- Winch: drum, axle caps, cable, hook or gripper, payload.
- Hinge: pin barrels, side brackets, moving lid, gasket or latch.
- Slider: drawer, twin rails, stop blocks, handle.
- Gear: toothed profiles or visible teeth, axle hubs, meshing pair, housing.
- Spring: guide rod, end caps, coil body, compression target.
- Linkage: pivots, arms, rods, constrained end point.
- Wheel: tire, hub, axle, fork or suspension.
- Belt: rollers, belt slab, carried object, scanner or sorter.

## Recipes

### Cable winch

```logoup
VAR drop = 20 + 50 * phase
PUSH
  MOVETO 0, 0, 80
  YAW 90
  TURN 0 - spin * 0.25
  RCYLINDER 12, 30, 1, 1
POP
BOX 0, 0, 55 - drop / 2, 3, 3, drop, 1, cable_color
```

### Constrained linkage

Use geometry from the crank example when possible:

```logoup
VAR crank = 360 * t
TURN crank
GO h1
VAR driven = 90 + ASIN(GETY() / h2)
TURN -crank + driven
GO h2
```

### Spring compression

```logoup
VAR compress = 1 + 0.35 * SIN(360 * t)
BODY
  REPEAT 36 * turns
    YAW 10
    SHIFT 0, step / 36 * compress
    LINK
  END
DONE
```

### Sliding scanner

```logoup
VAR scan = -60 + 120 * ABS(SIN(180 * t))
BOX scan, 0, 20, 18, 8, 8, 2, sensor_color
BOX 0, -10, 18, 140, 3, 3, 1, rail_color
BOX 0, 10, 18, 140, 3, 3, 1, rail_color
```

## Avoid

- Moving a whole object without a visible mechanism.
- Independent animations that should be mechanically linked.
- Fast chaotic motion. Use smooth `SIN/COS` cycles and ratios.
- Cultural motifs that spin randomly. Let motifs be vents, guards, grilles, trims, or light masks.
