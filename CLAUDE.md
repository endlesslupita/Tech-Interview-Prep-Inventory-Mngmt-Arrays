# Tech Interview Prep: Inventory Management System Update | Array

## Assignment Context
- Course: AD311 Intermediate Application Development 1
- Task: Duplicate zeros in-place in an inventory array to represent restock orders
- Scenario: Retail company needs to flag out-of-stock products by duplicating each zero entry, shifting remaining entries right

## Problem Summary
Given an array `inventory` of stock counts, duplicate each zero in-place:
- Each `0` (out-of-stock product) must be duplicated
- Subsequent elements shift right
- Elements beyond the original array length are not modified
- No separate output array — modification is in-place

**Example 1:** `[4,0,1,3,0,2,5,0]` → `[4,0,0,1,3,0,0,2]`
**Example 2:** `[3,2,1]` → `[3,2,1]` (no zeros, unchanged)

## Deliverables Required
- Solution in `solution.py`
- ASCII diagrams/flowcharts of the approach
- Clarifying questions documented
- Pytest unit tests: 3+ normal cases, 3+ edge cases
- Time and space complexity analysis
- Optimized solution with trade-off explanation

## Workflow (from parent CLAUDE.md)
- Generate naive solution first, then optimize
- Analyze time/space complexity for both versions
- Create pytest unit tests (3+ normal, 3+ edge cases)
- Create simple ASCII diagrams for whiteboard explanation

## Style (from parent CLAUDE.md)
- Use Pythonic idioms
- Include docstrings with complexity analysis

## Constraints
- Must be presentable as a live coding interview (talk through decisions)
- Communicate clearly throughout - explain why you make each decision