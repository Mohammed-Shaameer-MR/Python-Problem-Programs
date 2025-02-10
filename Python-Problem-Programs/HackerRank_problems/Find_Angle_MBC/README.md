# Find Angle MBC

![Problem Diagram](https://github.com/Mohammed-Shaameer-MR/Python-Problem-Programs/blob/main/Python-Problem-Programs/HackerRank_problems/Find_Angle_MBC/problem_image.png?raw=true)

## Problem Statement

ABC is a right triangle, with a right angle at **B**. **M** is the midpoint of the hypotenuse **AC**. Given the lengths of **AB** and **BC**, find the angle **MBC** (θ) in degrees.

## Formula

To find **∠MBC**, we use the inverse tangent function:

**θ = arctan(AB / BC)**

The result should be **rounded to the nearest integer**.

## Input Format

1. The first line contains the length of side **AB**.
2. The second line contains the length of side **BC**.

## Output Format

- Output **MBC** in degrees **rounded to the nearest integer**.

## Constraints

- **0 < AB < 100**  
- **0 < BC < 100**  
- **AB and BC are natural numbers**.

## Example

### Input
10
10

### Processing
- Given **AB = 10** and **BC = 10**.
- Compute **θ = arctan(10 / 10)**.
- **θ = 45°**.

### Output
45°

