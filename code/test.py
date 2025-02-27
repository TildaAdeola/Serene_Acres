import os
from pytmx.util_pygame import load_pygame

try:
    path = os.path.join('..', 'graphics', 'map.tmx')
    print("Loading map from:", path)
    map = load_pygame(path)
    print("Map loaded successfully!")
except Exception as e:
    print("Error:", e)
