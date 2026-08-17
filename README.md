# Blender Add-on Template
![Python version badge](https://img.shields.io/badge/Python%203.13+-3776AB?logo=python&logoColor=FFD43B)
![Blender version badge](https://img.shields.io/badge/Blender%205.2+-3776AB?logo=blender&logoColor=F5792A)

Structured starting point for developing **Blender** add-ons.

## Set Up Instructions
This guide shows how to set up a custom scripts folder so you can reload your add-on without restarting **Blender**.

1. **Open preferences**:
    Open **Blender** preferences by pressing `Ctrl + ,` or going to `Edit → Preferences` in the **Blender** topbar menu.

    ![Set Up Instruction Image][blender_addon_01]

2. **Add custom scripts directory**:
    In the File Paths section, add a custom scripts directory.
    Make sure there is a directory named `addons` (lowercase) inside the selected folder and place the addon inside it.

    ![Set Up Instruction Image][blender_addon_02]

3. **Save preferences**:
    Save your preferences so the settings persist between **Blender** sessions.

5. **Refresh local add-ons**:
    Refresh local add-ons. Your add-on should now appear in the list for enabling/disabling.
    Reload your add-on during development by refreshing local add-ons again with no need to restart Blender.

    ![Set Up Instruction Image][blender_addon_03]

6. **Activate the addon**:
    Search for your add-on and activate it.
    
    ![Set Up Instruction Image][blender_addon_04]

## Custom Scripts Directory Structure
Here’s an example of how your custom scripts directory might be organized when adding **Blender** add-ons.

> [!NOTE]
> **Blender** supports both single-file and folder-based add-ons.

```
custom scripts directory/
    └── addons/
        ├── addon.py              # Single-file add-on
        └── addon_folder/         # Folder-based add-on
            ├── __init__.py
            ├── other_module.py
            └── ...
```

[blender_addon_01]: https://res.cloudinary.com/vmfp1ov3/image/upload/v1786990972/blender_addon_01.webp
[blender_addon_02]: https://res.cloudinary.com/vmfp1ov3/image/upload/v1786990972/blender_addon_02.webp
[blender_addon_03]: https://res.cloudinary.com/vmfp1ov3/image/upload/v1786990972/blender_addon_03.webp
[blender_addon_04]: https://res.cloudinary.com/vmfp1ov3/image/upload/v1786990972/blender_addon_04.webp
