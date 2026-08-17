
"""
Blender Add-on Template

Structured starting point for developing Blender add-ons.
"""

# Blender-Python API imports
from bpy.utils import register_class, unregister_class

# Add-on imports
from .views import panels
from .controllers import operators


bl_info = {
    "name": "Blender Add-on Template",
    "description": "Structured starting point for developing Blender add-ons.",
    "author": "Doramas García Jorge (gajodoramas)",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "location": "View3D > Sidebar > Blender Add-on tab",
    "warning": "Experimental under-development add-on.",
    "tracker_url": "https://github.com/gajodoramas/blender-addon-template/issues",
    "category": "3D View"
}
_registrable_classes = \
    operators.registrable \
        + panels.registrable


def register():
    """Register all add-on classes in Blender."""
    for cls in _registrable_classes:
        register_class(cls)


def unregister():
    """Unregister all add-on classes in Blender."""
    for cls in reversed(_registrable_classes):
        unregister_class(cls)
