# Task-Conditioned Evaluation — Design Document

## What This Is
A novel evaluation approach for scanpath models that measures 
performance separately by task type — free-viewing vs visual search.

## The Problem with Current Evaluation
Current evaluation treats all scanpaths identically regardless 
of what task the human was performing. A model may perform well 
on free-viewing sequences but poorly on visual-search sequences 
— but current tools cannot reveal this distinction.

## Proposed Approach

### Step 1 — Tag sequences by task condition
COCO-Search18 already contains task-condition labels. 
We filter sequences by condition during evaluation.

### Step 2 — Per-condition metric breakdown
Instead of one aggregate score, results are broken down:

| Model       | Free Viewing | Visual Search |
|-------------|-------------|---------------|
| IRL         | 0.71        | 0.63          |
| HAT         | 0.68        | 0.61          |
| LLaVA-1.5   | 0.61        | 0.84          |

### Step 3 — Text prompt injection for VLMs
For models like LLaVA-1.5 that accept text input:
- Without prompt: image only → baseline
- With prompt: image + "Find the {target}" → task-conditioned

This directly answers: does language context improve 
goal-directed scanpath prediction?

## Why This Matters
This connects VLM evaluation to the actual scientific 
question of the project — goal-directed vision — rather 
than treating all models identically regardless of 
their capabilities.
```

Commit this file.

---

## Step 7 — Your Repo Now Looks Like This
```
gsoc2026-activevision/
├── README.md
├── lazy_loading_fix.py
├── experiment_config_example.yaml
└── task_conditioned_eval_design.md
