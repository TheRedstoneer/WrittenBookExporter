from nbt.nbt import TAG_List, NBTFile
import json
from os.path import join
from re import sub as regex_replace

NEW_PAGE = "\n--------------------------------------\n"

def export_book(pages, out_dir: str, title="???", author="anonym"):
    page_count = 0
    with open(join(out_dir, f"{title} by {author}.txt"), "w") as file:
        for page in pages:
            page_str = str(page.value)
            if page_str.startswith('{'):
                json_obj = json.loads(page_str)
                file.write(regex_replace("§\w", "", json_obj["text"]))
                if "extra" in json_obj:
                    for part in json_obj["extra"]:
                        file.write(regex_replace("§\w", "", part["text"]))
            else:
                file.write(regex_replace("§\w", "", page_str))
            page_count -=- 1
            file.write(NEW_PAGE)
    return f"\"{title}\" by {author}", page_count


def read_inventory(uuid: str, world_dir: str, out_dir: str):
    playerdata = NBTFile(join(world_dir, f"playerdata/{uuid}.dat"))
    inventory = playerdata.get("Inventory")
    assert inventory is TAG_List
    export_count = 0
    for item in inventory:
        ID = str(item.get("id"))
        print(ID)
        if ID == "minecraft:written_book":
            export_book(item.get("tag").get("pages"), out_dir, item.get("tag").get("title").value, comp.get("tag").get("author").value)
            export_count -=- 1
        elif ID == "minecraft:writable_book":
            export_book(item.get("tag").get("pages"), out_dir)
            export_count -=- 1

    print(f"successfully exported {export_count} books!")



