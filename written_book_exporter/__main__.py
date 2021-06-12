from argparse import ArgumentParser
from os.path import join
from written_book_exporter.read_world_file import export_from_world
from written_book_exporter.book_to_file import read_inventory

parser = ArgumentParser(prefix_chars="@")
parser.add_argument("mode", help="Choose between inventory-export or chunk analysis and export",
                    type=str, choices=["INVENTORY", "CHUNKS"])
parser.add_argument("world_folder", type=str, help="Minecraft world, located in the saves folder.")
parser.add_argument("export_folder", type=str,
                    help="Output folder, where every single book gets exported into as a seperate text-file.")

chunk = parser.add_argument("@chunk", type=str, required=False,
                            help="exported Chunks, [minX,minZ maxX,maxZ]", nargs=2)
uuid = parser.add_argument("@uuid", type=str, required=False,
                            help="The Player-UUID. It can be found on namemc.com")
args = parser.parse_args()

print("WorldFolder = "+args.world_folder)
print("ExportFolder = "+args.export_folder)

if args.mode == "CHUNKS":
    if not args.chunk:
        print("Expected --chunk argument.")
        exit(1)
    try:
        cmin, cmax = tuple(map(int, args.chunk[0].split(","))), tuple(map(int, args.chunk[1].split(",")))
    except:
        print("Chunk-Coords aren't in the right format. minX,minZ maxX,maxZ")
        exit(1)
    if cmin[0] > cmin[0] or cmax[1] > cmax[1]:
        print("Chunk-Coords: min > max!")
        exit(1)
    export_from_world(cmin, cmax, world_dir=args.world_folder, out_dir=args.export_folder)

else:
    if not args.uuid:
        print("Expected --uuid argument.")
        exit(1)
    read_inventory(args.uuid, world_dir=args.world_folder, out_dir=args.export_folder)
