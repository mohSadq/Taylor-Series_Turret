# 🛡️ Taylor-Series-Turret

A Python/Pygame project where I implemented a turret that tracks the mouse cursor without using standard math libraries like `math.atan2()`. 

## 🎯 Introduction
The goal of this project was to move away from "black box" functions and learn exactly how computers calculate angles. By building my own trigonometry engine from scratch, I gained a deep understanding of **numerical approximation** and **coordinate geometry**.

### 📚 Resources
* **Video Tutorial:** [Pygame Turret Logic](https://youtu.be/WnIycS9Gf_c)
* **Assets:** [Ground Shaker - Itch.io](https://zintoki.itch.io/ground-shaker)

---

## 🧮 How the Math Works

The project calculates the turret's rotation angle using the **Gregory-Leibniz Series** for $\arctan(z)$.

### 1. The Power Series
I implemented the arctangent function using 11 terms of the following Taylor series:
$$\arctan(z) = z - \frac{z^3}{3} + \frac{z^5}{5} - \frac{z^7}{7} + \dots$$


### 2. The Challenge: Domain Reduction
A major hurdle with the Taylor series for $\arctan$ is that it only works (converges) when the input $|z| \leq 1$. If the mouse is at a steep angle where the slope is greater than 1, the series "explodes" and provides incorrect values.

To solve this, I used **Domain Reduction**:
* If $|z| > 1$, I calculate the angle using the reciprocal: $90^\circ - \arctan(1/z)$

### 3. Quadrant Mapping
Since the series only returns values for the right side of the circle, I added logic to map the results to all 4 quadrants (0° to 360°) by checking the signs of $x$ and $y$ (the mouse's relative position).



---

## 🛠️ Implementation Details
* **Language:** Python 3
* **Library:** Pygame (for rendering and input)

---
## 🤝 Feedback & Improvements
This project was a deep dive into the math behind game engines. I am aware that this implementation is a numerical approximation and may not be 100% "production-ready" compared to optimized C libraries.

If you have suggestions for:
* More efficient power series iterations
* Better ways to handle the quadrant logic
* General Python clean-code tips

**I would be very grateful for your feedback!** Please feel free to open an issue or reach out. I am always looking to learn and improve.
