---
name: logoup-model-code
description: Generate, improve, debug, and organize competition-grade LogoUp / LogoUp3D `.txt` and `.logoup` model code. Use for LogoUp3D inventions, school-life products, realistic daily objects with technology functions, connected mechanical models, Chinese/Xiamen decorative models, hollow/lattice/cutaway techniques, and visible animations using INPUT_TIME, DRAW/FILL/EXTRUDE, BODY/LINK, ERASE, SUBTRACT, CAVE, gears, sliders, hinges, fans, rotors, springs, linkages, winches, drawers, and moving sensors.
---

# LogoUp Model Code

This skill is self-contained. It must work even on a computer with no `logoup速成.pdf`, no `例子` folder, and no previous LogoUp models. Local project files are useful extras, not required sources.

## Offline Guarantee

Use the bundled references as the source of truth. They contain the distilled LogoUp3D command grammar, modeling rules, animation patterns, mechanical structures, validation rules, and reusable example-derived parts needed to generate new models without external files.

When local PDFs, screenshots, examples, or old portfolio code are absent:

- do not stop or ask the user to provide them;
- do not claim LogoUp rules are unavailable;
- generate from `offline-core.md` and `offline-example-library.md`;
- keep the model simpler if needed, but still make it recognizable, connected, animated, and runnable.

When local examples are available, treat them as optional refinement material only. Never make generated code depend on paths, assets, screenshots, or helper files that will not exist on another computer.

## Required Reading

For every non-trivial LogoUp generation or repair task:

1. Read `references/offline-core.md`. It is the bundled command guide, modeling grammar, animation rules, and validation checklist.
2. Read `references/offline-example-library.md`. It is the bundled example library with reusable snippets for common shapes, stationery, drawers, gears, fans, rotors, drones, holders, lamps, toothbrush racks, plant pots, and other daily inventions.
3. If the local workspace contains `logoup速成.pdf`, `tmp_pdf_preview/all_pages_2x`, `例子`, a root drone, or an existing AI study pencil case, read only the relevant local files as extra evidence. Do not depend on them being present.
4. For cultural/Xiamen/Chinese classical styling, also read `references/classical-xiamen-style.md`.

## Generation Workflow

1. Convert the user's short idea into a complete modeling prompt before coding. Include:
   - real-life object prototype
   - exact life problem solved
   - visible parts and their positions
   - source patterns from `offline-example-library.md`
   - animation mechanisms and variables
   - connection points and acceptance checks
2. Start from a common real object, then add technology. The viewer must first recognize the product as a lamp, pencil case, cup, toothbrush holder, drone, lunch box, book stand, umbrella rack, plant pot, etc.
3. Build object anatomy before decoration: shell, rim, lid, hinge, rails, screws, motors, sensors, cables, slots, held objects, and contact points.
4. Use bundled example-derived parts. Do not invent vague symbols when the library has a usable pattern.
5. Preserve integrity. The whole model must read as one assembled product, not a set of loose parts. Every major part must visibly connect to the product. The upper structure and the base must be joined by walls, posts, hinges, rails, brackets, screws, sockets, or other believable supports; never leave the top floating above or detached from the base. Do not scatter accessories as separate islands.
6. Add visible functional animation. Decorative motion alone is insufficient.
7. Keep animation readable:
   - slow: lids, hinges, arms, sliding drawers
   - medium: springs, linkages, trays, floats
   - fast but marked: fans, gears, rotors, wheels
8. Write one folder per portfolio work under `作品集/<作品名>/`. Include both `<作品名>.txt` and `<作品名>.logoup` with identical code.
9. Run static checks before reporting completion:
   - no full-width commas in executable code
   - `PUSH` equals `POP`
   - every `DRAW` and `BODY` has `DONE`
   - every `ERASE ON` has `ERASE OFF`
   - every `SUBTRACT ON` has `SUBTRACT OFF`
   - `.txt` and `.logoup` hashes match

## Modeling Prompt Template

Use this internally before code. Show it to the user only when they ask to review the design before coding.

```text
LogoUp3D modeling prompt

User idea:
{user idea}

1. Product identity
- Work name:
- Real-life prototype:
- Problem solved:
- Use scene:
- First-view story:

2. Object anatomy
- Main silhouette and proportions:
- Fixed body parts:
- Moving parts:
- Held real-world objects:
- Connection points:
- Parts to avoid because they would look scattered:

3. Example migration
- Main shell pattern from offline library:
- Small-object pattern from offline library:
- Mechanical animation pattern from offline library:
- Decoration/detail pattern from offline library:
- How each pattern is scaled, rotated, recolored, or simplified:

4. Animation plan
- Total time and frame rate:
- Animation 1: moving part, fixed guide, variable, range, visible effect.
- Animation 2: moving part, fixed guide, variable, range, visible effect.
- Animation 3: moving part, fixed guide, variable, range, visible effect.

5. LogoUp implementation constraints
- Use INPUT_TIME directly in visible coordinates or TURN/PITCH/ROLL/MOVE/SHIFT.
- Use PUSH/POP around moving coordinate systems.
- Avoid variable/FUNC name collisions.
- Make `.txt` and `.logoup` identical.

6. Acceptance checks
- It is recognizable as:
- Its life problem is visible:
- The moving mechanism is visible from outside:
- No floating parts, disconnected supports, derailed drawers, wrong hinge axes, toothless gears, static-looking rotors, or unrecognizable real objects.
```

## Non-Negotiable Quality Rules

- A pencil case needs tub, raised rim, lid, hinge barrels, latch, inner dividers, tray/drawer, stationery, and optional exposed mechanism.
- Overall product integrity is mandatory. Before adding details or animation, define a continuous load path from base -> main body -> upper parts. Top pieces, covers, screens, handles, lamps, rotors, holders, signs, sensors, and decorative panels must be physically attached with visible supports, hinge barrels, brackets, columns, side walls, rails, cables, or screw bosses.
- The base is not a separate display platform unless the user explicitly asks for a display stand. If a base exists, it must either be part of the product shell or attach to the product through feet, bolts, rails, sockets, or molded supports.
- A drone needs fuselage, arms physically connected to motor pods, motor pods supporting spinning propeller axles, guard rings connected by struts, landing gear attached to fuselage, gimbal/winch/payload connected to body.
- Drone propellers must be thin airfoil-like blades, not thick rectangular slabs. Use 2 or 3 slender rounded/tapered blades, thickness 1-2, central hub, one colored tip or marker, and moderate speed so rotation is visible.
- A gear must have visible teeth, axle/hub, and a colored radial marker. It should drive or mesh with another visible part whenever possible.
- Draw sliding drawers as assemblies: fixed rails, cavity, drawer floor, side walls, front board, handle/knob if appropriate, and visible contents. The drawer may not slide out farther than its rails can support.
- Draw hinges around the real hinge edge. A lid must close over the product, not rotate around its center.
- Holders must contain the held object: umbrella racks contain umbrellas, slipper racks contain slippers, toothbrush racks contain toothbrushes and toothpaste, book stands contain books/pages, key trays contain keys, dish racks contain utensils.
- Transparent parts are allowed only as small windows, covers, and cutaways. Do not make the entire product transparent if it stops reading as a real object.
- Prefer compact, readable models over overloaded showcases. If animation fails or feels invisible, reduce detail and enlarge the exposed moving mechanism.

## Reference Map

- `references/offline-core.md`: self-contained LogoUp3D command guide, syntax rules, coordinate and animation rules, validation checklist.
- `references/offline-example-library.md`: reusable model snippets and product recipes.
- `references/mechanical-animation.md`: additional animation recipes.
- `references/logoup-patterns.md`: older pattern summary from local examples.
- `references/logoup-speedrun-study.md`: older speedrun summary.
- `references/classical-xiamen-style.md`: cultural styling guidance.

## Avoid

- Requiring a local PDF or example folder to know how to write code.
- Refusing a generation task just because `logoup速成.pdf`, `all_pages_2x`, or `例子` is missing.
- Copying broken local example typos.
- Using one generic base/layout for every model.
- Scattering parts around the scene.
- Moving the whole object instead of showing the mechanism.
- Overusing `RCUBE` when contour, `BODY`, `CAVE`, `ERASE`, `SUBTRACT`, or arrays would make the model clearer.
