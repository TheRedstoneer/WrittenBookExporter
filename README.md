
# Written Book Exporter

Two really helpful python scripts to extract Written Books from the Game Files.

### Config
- WORLD_DIR is the Minecraft world-directory, located in the saves folder.
- OUTPUT_DIR is a folder, where every single book gets exported into.
- CHUNKS are two tuples (x, z), which define all the chunks that are exported.
If you want to export a whole world, just set it to (-1000, -1000), (1000, 1000)
- UUID is the player-uuid, needed for inventory-export

## Export from Player-Inventory:

