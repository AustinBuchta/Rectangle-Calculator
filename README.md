# Random Rectangle Calculator & ASCII Visualizer

A CLI utility that generates randomized dimensions, calculates fundamental geometric properties, and renders a dynamic ASCII grid representation of the generated rectangle.

## Key Features

* **Procedural Dimension Generation:** Leverages Python's `random.randint` to generate constrained rectangle height and width bounds.
* **Geometric Calculation Module:** Functional handler returning perimeter ($2 \times (H + W)$) and area ($H \times W$) tuple values.
* **ASCII Layout Engine:** Dynamic terminal string rendering that draws a scaled, hollow ASCII rectangle using formatted string padding.
* **Interactive Control Loop:** State-driven execution loop with input sanitization (`try/except` blocks) and prompt-driven continuation logic.

## Technical Requirements

* **Python Version:** Python 3.x (uses built-in `random` standard library—zero external dependencies required).

## Usage

```bash
python main.py
