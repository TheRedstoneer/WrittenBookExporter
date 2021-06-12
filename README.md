
# Written Book Exporter

A python module to extract Written Books from the Game Files.

This module has two modes: An **inventory-export** and a **chunk-export**.

### Inventory-Export
Specify the uuid from a player and all written books from his inventory get exported.

### Chunk-Export
Specify the chunks you want to export (or set to for example [-1000,-1000 1000,1000] if you want to export a whole map. **Warning: The more chunks, the slower D:**)


### Download & Installation
You will need **Python 3.8 or newer**.
Download or clone this repository, cd into it and run \
`pip3 install .` \
All dependencies should be installed automatically. \
\
You can now run the module from any folder with \
`python3 -m written_book_exporter <args>`


### command line arguments:
* `{INVENTORY,CHUNKS}`   Choose between inventory-export or chunk analysis and export
* `world_folder`         Minecraft world, located in the saves folder.
* `export_folder`        output folder, where every single book gets exported into as a seperate text-file.

**optional arguments:**
* `@h`           just show a help message.
* `@chunk CHUNK CHUNK`  chunks to export, [minX,minZ maxX,maxZ]
* `@uuid UUID`          the Player-UUID. it can be found on namemc.com
