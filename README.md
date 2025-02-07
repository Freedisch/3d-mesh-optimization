# 3D Mesh Optimization Algorithm

## Overview
This project implements a 3D mesh optimization algorithm that leverages concepts from differential geometry and numerical optimization to improve rendering efficiency. The algorithm aims to reduce the number of vertices and faces in a 3D mesh while preserving its geometric features and visual quality.

## Features
- **Differential Geometry**: Utilizes vertex normals, face normals, and curvature information to understand the mesh's geometric properties.
- **Numerical Optimization**: Employs gradient descent to minimize an objective function that quantifies the mesh's quality.
- **Preprocessing and Postprocessing**: Ensures the mesh is in a suitable state before and after optimization.
- **Rendering Efficiency**: Optimizes the mesh to reduce rendering time without sacrificing visual fidelity.

## Installation
To run the 3D mesh optimization algorithm, you need to install the following Python libraries:

```bash
pip install numpy trimesh
```

## Usage
1. **Prepare Your Mesh**: Ensure you have a 3D mesh file in `.obj` format.
2. **Update the Script**: Replace `'./mesh.obj'` with the path to your mesh file and `'path/to/save/optimized_mesh.obj'` with the desired output path in the script.
3. **Run the Script**: Save the script to a file, e.g., `optimize_mesh.py`, and run it using Python:
   ```bash
   python optimize_mesh.py
   ```
4. **View the Results**: The optimized mesh will be saved to the specified path and displayed using the `trimesh` viewer.

## Video Presentation:

https://youtu.be/2r8zQKOlzO0 

## Image Result

<img width="1677" alt="Screenshot 2025-02-07 at 17 01 06" src="https://github.com/user-attachments/assets/d6e9b0c3-52fc-43b6-bd70-6229de5ea086" />


## Conclusion
This project provides a basic implementation of a 3D mesh optimization algorithm. The algorithm can be further refined and optimized based on specific requirements and use cases. The goal is to improve rendering efficiency while preserving the mesh's geometric features and visual quality.
