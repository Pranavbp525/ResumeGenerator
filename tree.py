import os

def generate_tree(directory, prefix=""):
    """Generate a tree-like structure of the directory."""
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(f"{prefix}├── {item}/")
            generate_tree(path, prefix + "│   ")
        else:
            print(f"{prefix}└── {item}")

# Example usage
project_root = "."  # Replace with your project directory
generate_tree(project_root)