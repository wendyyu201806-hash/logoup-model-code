# LogoUp Speedrun Study Notes

This reference condenses the full local LogoUp speedrun PDF and appendix command table.

## Full Book Structure

1. Sketch movement and plane drawing: cursor movement, `GO`, `TURN`, `DRAW`, `DONE`, `FILL`, `WIDTH`.
2. Freehand contour writing: `GOTO`, arcs, `CLOSE`, inner/outer rings, fill order.
3. Extrusion: move sketch plane, make solids with `EXTRUDE` and `CAVE`.
4. Aircraft model: adjust spatial pose and make different extruded parts.
5. Rotation bodies: axis-symmetric modeling with `BODY`, `YAW`, `LINK`.
6. Precision shapes: color, extrusion, rotation, accurate object profiles.
7. Pipe joints and geometry connection: spatial jumps and connected shapes.
8. Loops: repeated geometry, arrays, grids, vents.
9. Variables: parameterized repeated forms.
10. Functions: named reusable parts.
11. Conditions: branch control.
12. Element composition: absolute placement and drawing components.
13. Boolean/crop: `ERASE`, `SUBTRACT`, cutouts, shape interaction.
14. Artistic works: extend boolean ideas from 2D to 3D solids.
15. Polyhedra/cutting: create facets by cutting larger solids.
16. Multi-direction boolean design.
17. Grayscale/image-inspired modeling.
18. Recursive structures and fine geometry.
19. Moving joints: fitted parts and activity mechanisms.
20. Real-world scanning and scan-to-model workflow.
21. Product rendering and scene output.
22. Parameter lists for manageable design values.
23. Time-driven animation.
24. Appendix command reference.

## Important Commands

Flow and functions:
- `REPEAT`, `REPEAT WHEN`, `REPEAT UNTIL`, `IF/ELSE`, `FUNC`, `RETURN`, `VAR`, assignment.

Sketch:
- `GO`, `TURN`, `DRAW`, `DONE`, `FILL`, `WIDTH`, `CLEAR`, `CLEARSKETCH`, `HOME`, `OFFSET`, `CLOSE`, `GOTO`, `TURNTO`, `ERASE`, `SCALE`, `SCALEX`, `SCALEY`.

3D:
- `UP`, `YAW`, `PITCH`, `ROLL`, `BODY`, `LINK`, `JUMP`, `YAWTO`, `PITCHTO`, `ROLLTO`, `NORMAL`, `NORMALTO`, `ROTATEX`, `ROTATEY`, `ROTATEZ`, `MOVE`, `MOVETO`, `SHIFT`, `RESET`, `SUBTRACT`, `WARPX`, `WARPY`.

Standard shapes:
- `NGON`, `CIRC`, `ARC`, `STAR`, `STAR5`, `STAR6`, `RECT`, `SQUARE`, `RRECT`, `RSQUARE`, `SPIRO`, `ASTROID`, `EXTRUDE`, `CAVE`, `CUBE`, `BALL`, `ELLIPSOID`, `CYLINDER`, `PYRAMID`, `NPYRAMID`, `CONE`.

Images and state:
- `INGLOAD`, `INGSCALE`, `INGSTAMP`, `INGUNLOAD`, `GETX`, `GETY`, `GETH`, `GETOX`, `GETOY`, `GETOZ`, `GETYAW`, `GETPITCH`, `GETROLL`, `GETWIDTH`, `ISDRAWING`, `GETSCALEX`, `GETSCALEY`, `GETWARPX`, `GETWARPY`.

Math and color:
- `RGB`, `RGBA`, `HSV`, `SIN`, `COS`, `TAN`, `ASIN`, `ACOS`, `ATAN`, `ATAN2`, `ABS`, `SQRT`, `EXP`, `LOG`, `ROUND`, `FLOOR`, `CEIL`, `RAND`, `SRAND`.

## Modeling Lessons To Apply

- Use sketches to define accurate silhouettes before making solids.
- Use holes and boolean cuts for realism: vents, handles, grooves, slots, screw recesses, transparent windows, hollow shells.
- Use `BODY/LINK` to make curved shells, bottles, cups, propeller blades, rubber grips, cables, and organic decorative forms.
- Use loops for repeated detail. A competition object should have arrays: vents, lattice, buttons, keys, rivets, LEDs, screws, guide holes.
- Use named functions for repeated meaningful modules.
- Use time only after geometry is clear. Function animation should show the real mechanism.

## Supplied Root Drone Minimum

If a root drone reference `.txt` exists, treat it as the minimum standard:
- Hollow shell with `SUBTRACT`.
- Custom rotor body using `BODY`, `PITCH`, `JUMP`, `LINK`.
- Hand-drawn propeller blades with `DRAW`, `GO`, `TURN`, `FILL`, `EXTRUDE`.
- Multiple nozzle/sensor modules.
- Top ring/cave details and tower/antenna assembly.

New drone or product models must be more complex than this baseline, not simpler.
