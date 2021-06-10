from nbt.nbt import NBTFile, TAG_Compound, TAG_List
import json
from re import sub as regex_replace
from WrittenBookExporter.config import *

PATH = WORLD_DIR + "/playerdata/" + UUID + ".dat"


def export_book(pages, title="???", author="anonym"):
    page_count = 0
    with open(f"{OUTPUT_DIR}/{title} by {author}", "w") as file:
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


def read_inventory(inv: TAG_List):
    export_count = 0
    for item in inv:
        ID = str(item.get("id"))
        print(ID)
        if ID == "minecraft:written_book":
            export_book(item.get("tag").get("pages"), item.get("tag").get("title").value, comp.get("tag").get("author").value)
            export_count -=- 1
        elif ID == "minecraft:writable_book":
            export_book(item.get("tag").get("pages"))
            export_count -=- 1

    print(f"successfully exported {export_count} books!")


#playerdata = NBTFile(PATH, 'r')
#inventory = playerdata.get("Inventory")
#read_inventory(inventory)
