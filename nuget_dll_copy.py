import os
import sys
from os import system
import shutil

nuget_folder = "/Users/cloudlin/Downloads/v2"
dll_export_folder = "/Users/cloudlin/Downloads/v2_dlls"
compatible_dotnet_version = "netstandard2.0"


def step_into_and_search(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            step_into_and_search(entry.path)
        if entry.path.endswith(".dll") and entry.is_file() and compatible_dotnet_version in entry.path:
            print(entry.path)
            shutil.copy(entry.path, f"{dll_export_folder}/{entry.name}")
            global count
            count += 1


nuget_result = os.system(
    f"nuget install Google.Apis.Translate.v2 -OutputDirectory {nuget_folder}")

if(nuget_result != 0):
    print("nuget install package failed. exit code is %d" % nuget_result)
    sys.exit()

# find and copy dlls to export folder
if not os.path.exists(dll_export_folder):
    try:
        os.mkdir(dll_export_folder)
    except OSError:
        print("Creation of the directory %s failed" % dll_export_folder)
        sys.exit()
    else:
        print("Successfully created the directory %s " % dll_export_folder)

count = 0
step_into_and_search(nuget_folder)
print(f"==========Script finished, copied [{count}] dlls!==========")
