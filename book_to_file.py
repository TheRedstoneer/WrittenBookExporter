from nbt.nbt import NBTFile, TAG_Compound, TAG_List
import json
from re import sub as regex_replace
from .config import *

PATH = PATH + "/playerdata/" + UUID + ".dat"


def export_book(pages, title="???", author="anonym"):
    page_count = 0
    with open(f"{OUTPUT_DIR}/{title} by {author}", "w") as file:
        for page in pages:
            pageS = str(page.value)
            if pageS.startswith('{'):
                jsonObj = json.loads(pageS)
                file.write(regex_replace("§\w", "", jsonObj["text"]))
                if "extra" in jsonObj:
                    for part in jsonObj["extra"]:
                        file.write(regex_replace("§\w", "", part["text"]))
            else:
                file.write(regex_replace("§\w", "", pageS))
            page_count -=- 1
            file.write(NEW_PAGE)
    print(f"exported {page_count} pages!")


def read_inventory(invList):
    export_count = 0
    if type(invList) is not TAG_List: return
    for item in invList:
        ID = str(item.get("id"))
        print(ID)
        if ID == "minecraft:written_book":
            export_book(item.get("tag").get("pages"), comp.get("tag").get("title").value, comp.get("tag").get("author").value)
            export_count -=- 1
        elif ID == "minecraft:writable_book":
            export_book(item.get("tag").get("pages"))
            export_count -=- 1

    print(f"successfully exported {export_count} books!")

playerdata = NBTFile(PATH, 'r')
inventory = playerdata.get("Inventory")
read_inventory(inventory)
