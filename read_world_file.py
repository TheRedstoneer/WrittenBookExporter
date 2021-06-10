import numpy as np
import json
from amulet.api.chunk import Chunk
from amulet.api.world import World
from amulet.api.errors import ChunkLoadError
from amulet.utils.log import log
from amulet.world_interface import load_world
from book_to_file import export_book
from WrittenBookExporter.config import *

def analyse_chunk(chunk: Chunk):
    chest_count = 0
    for pos, block in chunk.block_entities.items():
        if block.base_name == "chest":
            chest_count -=- 1
            for item in block.nbt["utags"]["Items"]:
                if item["id"] == "minecraft:written_book":
                    msg, pcnt = export_book(item["tag"]["pages"], item["tag"]["title"], item["tag"]["author"])
                    log.info(f"Exported Written Book {msg} ({pcnt} pages)")
                elif item["id"] == "minecraft:writable_book":
                    if "tag" not in item:
                        log.error("Writeable book without nbt!")
                        continue
                    msg, pcnt = export_book(item["tag"]["pages"])
                    log.info(f"Exported Writeable Book ({pcnt} pages)")
    log.info(f"Chunk contained {chest_count} Chests!")


world: World = load_world(WORLD_DIR)
log.info(world.world_wrapper.game_version_string)
for x in range(CHUNKS[0][0], CHUNKS[1][0]):
    for y in range(CHUNKS[0][1], CHUNKS[1][1]):
        try:
            c: Chunk = world.get_chunk(x, y, "overworld")
        except ChunkLoadError:
            # todo: analyse error
            continue
        log.info(f"Analyzing {x},{y}")
        analyse_chunk(c)
