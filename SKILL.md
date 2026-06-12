---
name: logoup-model-code
description: Generate LogoUp / LogoUp3D model code for polished 3D inventions, classroom objects, product concepts, and animated models. Use when the user asks to create, improve, debug, organize, or explain `.txt` LogoUp code, especially models using functions, `RCUBE`, `RCYLINDER`, sketch extrusion, color, `INPUT_TIME` animation, modular parts, or competition-ready science-and-technology themes.
---

# LogoUp Model Code

## Workflow

1. Clarify the model's story: object, problem solved, target user, and expected animation.
2. Inspect nearby examples when working in an existing project. Prefer established commands and local style.
3. Create standalone `.txt` code unless the user asks for snippets. Keep each model self-contained.
4. Build in modules: helper functions first, then main body, then animated parts, then decorative details.
5. Use `INPUT_TIME` for animation whenever the user wants movement or a competition showcase.
6. Run a static pass before finishing: no full-width commas in code, balanced `PUSH/POP`, no accidental unsupported operators, and no dangling sketch/body blocks.

## LogoUp Patterns

Prefer these reliable commands and combinations:

- Base solids: `RCUBE l, w, h, br, tr`, `RCYLINDER r, h, br, tr`, `BALL r`.
- Sketch solids: `CIRC`, `ELLIPSE`, `RECT`, `RRECT`, `DRAW ... DONE`, `FILL`, `EXTRUDE`, `BODY ... DONE`.
- Movement: `MOVETO x, y, z`, `MOVE x, y, z`, `UP h`, `YAW angle`, `PITCH angle`, `ROLL angle`, `TURN angle`.
- Modularity: `FUNC NAME @arg`, `PUSH/POP`, `CLEAR`, `RESET`.
- Materials: `COLOR RGB(r,g,b)`, `COLOR RGBA(r,g,b,a)`, `COLOR HSV(h,s,v)`.
- Animation: `VAR t = INPUT_TIME(0, 0, 4, 25)`, then drive position/angle with `SIN`, `ABS`, and multiplication.

Read `references/logoup-patterns.md` when you need fuller examples or a checklist.

## Quality Bar

Competition models should show:

- A recognizable main object from the first view.
- At least 6-10 visible detail groups, such as screens, sensors, handles, labels, lights, hinges, tools, panels, or texture strips.
- At least 2 meaningful animations, not only decorative spinning.
- A clear functional story: what problem it solves and how the moving parts demonstrate that solution.
- Code that a student can edit: named color variables, helper functions, and comments for major sections.

Avoid overusing pixel blocks unless the requested style is pixel art. For product concepts, prefer rounded solids, rings, transparent parts, panels, and layered assemblies.

## Static Check

Before delivering code:

- Search for full-width Chinese punctuation such as Chinese commas, semicolons, parentheses, and curly quotes.
- Avoid `%` modulo unless local examples prove the LogoUp parser supports it.
- Check `PUSH` count equals `POP` count.
- Ensure every `BODY` or `DRAW` has a matching `DONE`.
- Keep color expressions simple; define color variables before passing them into custom helper functions if parser stability matters.

## Scaffold Script

Use `scripts/scaffold_logoup_model.py` to print a starter animated model:

```bash
python scripts/scaffold_logoup_model.py "Smart School Invention"
```

The scaffold is only a starting point. Replace the placeholder details with the user's specific invention.
