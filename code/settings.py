import pygame
from os.path import join

screen_width = 800 #screen values
screen_height = 800

tile_size = 16



# Animation frame settings (all frames in a sprite sheet)
FRAME_WIDTH = 32
FRAME_HEIGHT = 32
NUM_FRAMES = 8
SCALE_FACTOR = 2
SCALED_FRAME_WIDTH = FRAME_WIDTH * SCALE_FACTOR
SCALED_FRAME_HEIGHT = FRAME_HEIGHT * SCALE_FACTOR

# Customization options:
NUM_SKINTONES = 8
NUM_CLOTHING_OPTIONS = 10
NUM_HAIRSTYLE_OPTIONS = 15

DIRECTIONS = ['forward', 'backward', 'left', 'right']

#import images

def import_image(*path, alpha=True, file_format='png'):
    """
    Loads an image from the given file path.
    :param path: Components of the file path which will be joined.
    :param alpha: If True, the image is converted with per-pixel alpha (transparency).
    """
    full_path = join(*path) + f'.{file_format}'
    if alpha:
        image = pygame.image.load(full_path).convert_alpha()
    else:
        image = pygame.image.load(full_path).convert()
    return image

#import frames

def import_animation_frames(path, num_frames=NUM_FRAMES,
                            frame_width=FRAME_WIDTH, frame_height=FRAME_HEIGHT,
                            scale_factor=SCALE_FACTOR, file_format='png'):
    """
    Loads a sprite sheet and slices it into individual frames.
    It assumes the sprite sheet contains the frames arranged horizontally.
    After cutting each frame (which is frame_width x frame_height),
    the frame is scaled up by the given scale_factor.
    :param path: The file path to the sprite sheet (without extension).
    :param num_frames: Number of frames in the sprite sheet.
    :param frame_width: The width of one frame (unscaled).
    :param frame_height: The height of one frame (unscaled).
    :param scale_factor: The factor by which to scale each frame.
    :param file_format: The file extension (default 'png').
    :return: A list of pygame.Surface objects, one for each frame.
    """
    # Load the entire sprite sheet image
    sheet = import_image(path, file_format=file_format)

    frames = []
    for i in range(num_frames):

        frame_surface = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA)


        frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)

        # Blit (copy) the current frame from the sheet onto the frame_surface.
        frame_surface.blit(sheet, (0, 0), frame_rect)

        # Scale the frame to the desired size.
        scaled_frame = pygame.transform.scale(
            frame_surface,
            (frame_width * scale_factor, frame_height * scale_factor)
        )
        frames.append(scaled_frame)

    return frames

#dictionaries
def load_player_animations(base_folder):

    animations = {
        'skintones': {},
        'clothes': {},
        'hairstyles': {}
    }

