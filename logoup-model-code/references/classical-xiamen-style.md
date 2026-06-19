# Chinese Classical And Xiamen Style Guide

Use when a model needs Chinese classical beauty, local identity, or competition visual polish.

## Xiamen Elements

Integrate these as geometry, not just comments:

- Egret: white bird silhouette as cutout, badge, light mask, fin, or drone wing guard.
- Gulangyu piano: black/white key motif as side trim, scanner rail, base steps, or signal grille.
- Sea and island: wave curves, coastline edge, ripple rings, harbor bollards, boat-like base.
- Shapowei harbor: dock planks, mooring rings, fishing-net lattice, small buoy lights.
- Xiamen bridge arcs: curved support ribs, cable-stayed lines, arch handles.
- Minnan red-brick architecture: brick-red panels, swallow-tail roof curve, stone base blocks, carved window grilles.

## Chinese Classical Motifs

Good motif placements:
- Cloud pattern as vents or sensor grille.
- Lattice window as transparent panel or heat exhaust.
- Folding fan ribs as propeller guard, lamp shade, cup sleeve, or book stand support.
- Ruyi curve as handle or latch.
- Wave pattern as base border or airflow path.
- Seal stamp frame as name plate or control panel.
- Porcelain blue-white linework as cup, lunch box, or lamp shade trim.

## Implementation Patterns

### Lattice grille

Use repeated thin bars or erased rounded rectangles:

```logoup
VAR i = 0
REPEAT 7
  BOX -30 + i * 10, 0, 0, 3, 40, 2, 1, trim_color
  i = i + 1
END
VAR j = 0
REPEAT 4
  BOX 0, -18 + j * 12, 1, 70, 3, 2, 1, trim_color
  j = j + 1
END
```

### Cloud or wave contour

Use `DRAW` and `ARC`, then `FILL` and `EXTRUDE` as a relief or cutout.

### Fan pattern

Use the carved folding fan example idiom:
- Define a rib contour.
- Use `ERASE ON` to cut flower/leaf/heart/rose patterns.
- Repeat ribs with `YAW`.

## Color Direction

Use a balanced palette:
- Technology base: deep blue, graphite, silver, translucent cyan.
- Classical accents: brick red, ivory, jade green, warm gold, porcelain blue.
- Xiamen accent: sea teal, egret white, piano black, stone gray.

Avoid making everything one color family. Accents should clarify function and culture.
