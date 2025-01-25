import pygame

# Base path for image assets
BASE_IMG_PATH = 'data/images/'

def load_image(path):
    """
    Load an image from the specified path, convert it for optimal display,
    and set the transparent color key.
    
    Args:
        path (str): Relative path to the image file.
        
    Returns:
        pygame.Surface: The loaded and processed image.
    """
    img = pygame.image.load(BASE_IMG_PATH + path).convert()  # Load and convert the image
    img.set_colorkey((0, 0, 0))  # Set black as the transparent color
    return img