import matplotlib.pyplot as plt

def plot_number_line(points, title="Number Line"):
    """
    Plots given points on a horizontal number line.
    
    Args:
        points (list): List of numbers to plot.
        title (str): Title of the plot.
    """
    if not points or not all(isinstance(p, (int, float)) for p in points):
        raise ValueError("Points must be a non-empty list of numbers.")

    # Determine range with padding
    min_val = min(points) - 1
    max_val = max(points) + 1

    fig, ax = plt.subplots(figsize=(8, 2))
    
    # Draw horizontal line
    ax.hlines(y=0, xmin=min_val, xmax=max_val, color='black')
    
    # Plot points
    ax.scatter(points, [0] * len(points), color='red', zorder=5)
    
    # Annotate each point
    for p in points:
        ax.annotate(str(p), (p, 0.1), ha='center', fontsize=10)
    
    # Remove y-axis and set limits
    ax.get_yaxis().set_visible(False)
    ax.set_xlim(min_val, max_val)
    ax.set_title(title)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        numbers = [0, 2, 4.5, -3, 7]
        plot_number_line(numbers, "Example Number Line")
    except Exception as e:
        print(f"Error: {e}")
