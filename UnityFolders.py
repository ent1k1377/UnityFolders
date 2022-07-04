import os


def createFolders():
    path = input("Enter the path to create folders: ")
    pathResources = f"{path}\\Resources"
    listFolders = ["Animations", "Fonts", "Materials", "Music", "Prefabs", "Scripts", "Shaders",
                   "Sprites", "Tilemaps", "UI"]

    if os.path.exists(pathResources):
        return "Resources folder already exists"

    os.mkdir(pathResources)
    for folder in listFolders:
        os.mkdir(f"{path}\\Resources\\{folder}")
    return "Success"


if __name__ == '__main__':
    print(createFolders())
