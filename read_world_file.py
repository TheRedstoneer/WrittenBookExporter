import numpy as np
import json
from amulet.api.chunk import Chunk
from amulet.api.world import World
from amulet.api.block_entity import BlockEntity
from amulet.world_interface import load_world
from .book_to_file import export_book
from .config import *

def analyse_chunk(chunk: Chunk):
    for pos, block in chunk.block_entities.items():
        if block.base_name == "chest":
            print(f"Chest @[{pos[0]},{pos[1]},{pos[2]}] contains:")
            for item in block.nbt["utags"]["Items"]:
                if item["id"] == "minecraft:written_book":
                    export_book(item["tag"]["pages"], item["tag"]["title"], item["tag"]["author"])
                elif item["id"] == "minecraft:writable_book":
                    export_book(item["tag"]["pages"])


world: World = load_world(WORLD_FOLDER)
print(world.world_wrapper.game_version_string)
analyse_chunk(world.get_chunk(15, -22, "overworld"))
