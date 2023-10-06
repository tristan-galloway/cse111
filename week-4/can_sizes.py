"""

Student: Tristan Galloway
Teacher: Brother Clements
File: can_sizes.py
Purpose: Strengthen your understanding of user-defined functions,
parameters, arguments, and local variable scope by writing a program
that has three or more functions.

"""
# Import math so we can use the math.pi function
import math

def main():
    # Create a matching list of names, radius, heights, costs per can.
    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost_per_can = [.28, .42, .45, .61, .86, .83, .22, .26, 1.53, .34, .38, .42]
    
    # iterate through the names and compute each of their respective volumes, surface areas, and storage efficiencies then display the storage efficiency
    for i, name in enumerate(names):
        volume = compute_volume(radius[i], heights[i])
        surface_area = compute_surface_area(radius[i], heights[i])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        print(f"{name} {storage_efficiency:.2f}.")
    
import math
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi*radius**2*height
    return volume

compute_volume(2, 4)

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.

    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surface_area = 2*math.pi*radius*(radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """Compute and return the storage efficiency of a cylinder

    Parameters
        volume: the volume of the cylinder
        surface_area: the surface area of the cylinder
    Rutern: the storage effiency of the cylinder
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()