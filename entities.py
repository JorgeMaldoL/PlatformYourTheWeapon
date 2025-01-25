import pygame

class PhysicsEntity:
    """
    Represents a physical entity in the game with position, size, and velocity.
    """
    def __init__(self, game, e_type, pos, size):
        """
        Initialize the PhysicsEntity.
        
        Args:
            game (Game): Reference to the main game instance.
            e_type (str): Type of the entity.
            pos (tuple): Initial position (x, y).
            size (tuple): Size dimensions (width, height).
        """
        self.game = game  # Reference to the game instance
        self.type = e_type  # Type of the entity
        self.pos = list(pos)  # Current position of the entity
        self.size = size  # Size of the entity
        self.velocity = [0, 0]  # Current velocity in x and y directions

    def update(self, movement=(0, 0)):
        """
        Update the entity's position based on movement and velocity.
        
        Args:
            movement (tuple): Movement vector (dx, dy).
        """
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]  # Update x position
        self.pos[1] += frame_movement[1]  # Update y position

    def render(self, surf):
        """
        Render the entity on the given surface.
        
        Args:
            surf (pygame.Surface): The surface to draw the entity on.
        """
        surf.blit(self.game.assets['player'], self.pos)  # Draw the player image at the current position