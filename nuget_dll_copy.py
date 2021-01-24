import os
import sys
from os import system
import shutil
import argparse
import platform

# CLI argument settings
parser = argparse.ArgumentParser()
parser.add_argument("nuget_package_name",
                    help="the nuget package to export from, e.g. Newtonsoft.Json")
parser.add_argument(
    "--nuget-path", help="The path to NuGet will download to, default is xxx")
parser.add_argument(
    "--output-path", help="The path to export dll, default is xxx")
parser.add_argument("--dotnet-version",
                    help="Must match the [Api Compatibility Level] in your Unity build settings, default is [netstandard2.0]")
args = parser.parse_args()

# default path
platform = platform.system()
if platform == "Linux" or platform == "Darwin":
    nuget_path = f"/Users/cloudlin/Downloads/{args.nuget_package_name}"
    dll_output_path = "/Users/cloudlin/Downloads/v2_dlls"
    compatible_dotnet_version = "netstandard2.0"
elif platform == "Windows":
    nuget_path = f"{args.nuget_package_name}"
    dll_output_path = "exported_dlls"
    compatible_dotnet_version = "netstandard2.0"

# if argument is specified, override the default path
if args.nuget_path:
    nuget_path = args.nuget_path
if args.output_path:
    dll_output_path = args.output_path
if args.dotnet_version:
    compatible_dotnet_version = args.dotnet_version

# download nuget package
nuget_result = os.system(
    f"nuget install {args.nuget_package_name} -OutputDirectory {nuget_path}")

if nuget_result != 0:
    print("NuGet install package failed. exit code is %d" % nuget_result)
    sys.exit()

# find and copy dlls to export folder
if not os.path.exists(dll_output_path):
    try:
        os.mkdir(dll_output_path)
    except OSError:
        print("Creation of the directory %s failed" % dll_output_path)
        sys.exit()
    else:
        print("Successfully created the directory %s " % dll_output_path)


def step_into_and_search(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            step_into_and_search(entry.path)
        if entry.path.endswith(".dll") and entry.is_file() and compatible_dotnet_version in entry.path:
            print(entry.path)
            shutil.copy(entry.path, f"{dll_output_path}/{entry.name}")
            global count
            count += 1


count = 0
step_into_and_search(nuget_path)
print(f"==========Script finished, copied [{count}] dlls!==========")
