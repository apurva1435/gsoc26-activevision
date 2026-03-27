# GSoC 2026 — ActiveVision Contributions

Preparation work for GSoC 2026 Project #19 — ActiveVision: 
A Data and Model Portal for the Study of Goal-Directed Vision
Organization: INCF

## About

This repository documents my exploration of the 
[ActiveVisionPortal](https://github.com/m2b3/ActiveVisionPortal) 
codebase and contributions I've been working on as part of 
my GSoC 2026 proposal.

## Contributions

### 1. Lazy Loading Fix for Model Registry
**Problem identified:** `model_registry.py` eagerly imports 
all models at startup. This causes dependency errors even for 
simple operations like `--list_models` when optional 
dependencies like Detectron2 are not installed.

**Fix:** Models are now imported only when explicitly 
requested — not at startup.

### 2. YAML Experiment Config Design
A proposed config format for reproducible multi-model 
experiments — the foundation of the Experiment Engine 
described in my proposal.

### 3. Task-Conditioned Evaluation Design
Design for evaluating models separately by task type 
(free-viewing vs visual search) and feeding task prompts 
to vision-language models during evaluation.

## Related
- ActiveVisionPortal: github.com/m2b3/ActiveVisionPortal
- INCF GSoC 2026: neurostars.org
