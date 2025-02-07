import numpy as np
import trimesh

def preprocess_mesh(mesh):
    if isinstance(mesh, trimesh.Scene):
        mesh = mesh.geometry[list(mesh.geometry.keys())[0]]

    mesh.vertex_normals
    mesh.face_normals

    mesh.curvature = np.linalg.norm(mesh.vertex_normals, axis=1)

    return mesh

def compute_geometric_error(mesh):
    original_vertices = mesh.vertices.copy()
    error = np.linalg.norm(mesh.vertices - original_vertices, axis=1).mean()
    return error

def compute_curvature_error(mesh):
    original_curvature = mesh.curvature.copy()
    error = np.abs(mesh.curvature - original_curvature).mean()
    return error

def objective_function(mesh):
    geometric_error = compute_geometric_error(mesh)
    curvature_error = compute_curvature_error(mesh)
    return geometric_error + curvature_error

def compute_geometric_gradients(mesh):
    original_vertices = mesh.vertices.copy()
    gradients = mesh.vertices - original_vertices
    return gradients

def compute_curvature_gradients(mesh):
    original_curvature = mesh.curvature.copy()
    gradients = (mesh.curvature - original_curvature)[:, np.newaxis] * mesh.vertex_normals
    return gradients

def compute_gradients(mesh):
    geometric_gradients = compute_geometric_gradients(mesh)
    curvature_gradients = compute_curvature_gradients(mesh)
    return geometric_gradients + curvature_gradients

def gradient_descent(mesh, learning_rate=0.01, num_iterations=100):
    for i in range(num_iterations):
        gradients = compute_gradients(mesh)
        mesh.vertices -= learning_rate * gradients
        if i % 10 == 0:
            print(f"Iteration {i}, Objective: {objective_function(mesh)}")
    return mesh

def postprocess_mesh(mesh):
    mesh.remove_unreferenced_vertices()
    mesh.remove_degenerate_faces()

    mesh.fix_normals()

    return mesh

def optimize_mesh(mesh, learning_rate=0.01, num_iterations=100):
    mesh = preprocess_mesh(mesh)
    mesh = gradient_descent(mesh, learning_rate, num_iterations)
    mesh = postprocess_mesh(mesh)
    return mesh

mesh = trimesh.load('./22-trees_9_obj/trees9.obj')

optimized_mesh = optimize_mesh(mesh)

optimized_mesh.export('./22-trees_9_obj/optimized_mesh.obj')

optimized_mesh.show()
