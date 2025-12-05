import os
import shutil

File_Count = {"Video":0, "Image":0, "Audio":0, "Document":0, "Archive":0}
Skipped = 0
Images = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
Videos = {".mp4", ".mov", ".mkv", ".mpg", ".mpeg" ".webm", ".wmv"}
Audios = {".mp3", ".wav", ".ogg", ".flac", ".wma", ".opus", ".aac"}
Documents = {".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".md", ".wps"}
Archives = {".tar", ".rar", ".zip", ".7zip", ".gz"}
Folders = set()
FilesThatNeedSorting = []

while True:
    AddressBar = input("Please enter the FULL address of the folder you want to handle \n").strip()

    if os.path.exists(AddressBar) and os.path.isdir(AddressBar):
        print("File Address found! Loading...")
        break
        
    else:
        print("File Address does not exist. Please try again. \n")

for item in os.listdir(AddressBar):
    Everyitem = os.path.join(AddressBar, item)

    if os.path.isdir(Everyitem):
        continue

    elif "." not in item:
        print(f"Skipped due to lack of an extension:{item}.")
        Skipped += 1
        continue

    else:
        FilesThatNeedSorting.append(item)

print("\nFiles to sort:", FilesThatNeedSorting)

def category(filename):
    cat = os.path.splitext(filename)[1].lower()

    if cat in Images:
        return "Image"
    elif cat in Videos:
        return "Video"
    elif cat in Audios:
        return "Audio"
    elif cat in Documents:
        return "Document"
    elif cat in Archives:
        return "Archive"
    else:
        return "Other"

for f in FilesThatNeedSorting:
    Categories = category(f)
    Folders.add(Categories)
    print(f"{f}) = {category(f)}")
    File_Count[Categories] += 1

for categories in Folders:
    FolderAddress = os.path.join(AddressBar, categories)
    os.makedirs(FolderAddress, exist_ok=True)
    print(f"Folder created or already exists: {FolderAddress}")

for f in FilesThatNeedSorting:
    Folder = category(f)
    CurrentLocation = os.path.join(AddressBar, f)
    Destination = os.path.join(AddressBar, Folder, f)
    counter = 1
    dupliname, ext = os.path.splitext(f)
    while os.path.exists(Destination):
        newdupliname = f"{dupliname} ({counter}){ext}"
        Destination = os.path.join(AddressBar, Folder, newdupliname)
        counter += 1

    shutil.move(CurrentLocation, Destination)
    print(f"Moved {f} to {Destination}")


print("File Organizer complete!")
for category, count in File_Count.items():
    print(f"\n{category}: {count} files moved")
print(f"Skipped {Skipped} files")

input("\nPress ENTER to exit.")