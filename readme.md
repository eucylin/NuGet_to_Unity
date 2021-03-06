A simple script that download NuGet package and exported dll which Unity can directly use.

# Prerequisites

- [Python3](https://www.python.org/downloads/)
- [Nuget CLI](https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-nuget-cli)

# Usages

Download or Clone the [nuget_dll_copy.py](https://github.com/eucylin/NuGet_to_Unity/blob/main/nuget_dll_copy.py "nuget_dll_copy.py")

For macOS/Linux user, run following command in terminal:

```bash
$ python3 ./nuget_dll_copy.py [nuget_package_name]

# for example, exported Google Translate package
$ python3 ./nuget_dll_copy.py Google.Cloud.Translation.V2
```

For Windows10, use commad below in Powershell:

```bash
$ py ./nuget_dll_copy.py [nuget_package_name]
```

After script executed finish, A folder named [nuget_package_name] will show up in the path you executed script.

There will be two folder inside it, copy the "exported_dlls" folder and place it in under your Unity project folder _Assets/Plugins_. That's it!

If you wish to specified path and .Net version, use these arguments

```bash
# use custom path and .Net4.x version
$ python3 ./nuget_dll_copy.py Google.Cloud.Translation.V2 --nuget-path ~/Downloads/G_Source --output-path ~/Downloads/G_Output --dotnet-version net4
```

optional:

If you use IL2CPP as scripting backend and the nuget package make use of C# reflections. You probably need to create a `link.xml` file to avoid compile error in builds. Follow the document below to create your own xml file.

# Reference

You could also follow the link below to do these works manually. Result is the same, but may takes more time to copy the dll from each dependent package.

[Microsoft Doc](https://docs.microsoft.com/en-us/visualstudio/gamedev/unity/unity-scripting-upgrade#add-packages-from-nuget-to-a-unity-project)
