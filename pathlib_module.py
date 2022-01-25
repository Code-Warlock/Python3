from pathlib import Path
import os

# home_dir = Path.home()
# current_dir = Path.cwd()
# current_file = Path(__file__)
# # print(current_file)
# new_folder = current_dir / 'des.txt' # C:\\Users\Felz\Desktop\Desmond\Python3
# new_folder.mkdir(mode=511, parents=False, exist_ok=False)
# print(new_folder.name)
# print(new_folder.is_file())
# print(home_dir)


current_folder = Path.cwd()
# for doc in current_folder.iterdir():
#     if doc.suffix == '.txt':
#         print(doc)

for doc in current_folder.rglob("*"):
    if doc.suffix == '.txt':
        print(doc)
