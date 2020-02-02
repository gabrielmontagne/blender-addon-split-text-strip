import bpy
from bpy.props import BoolProperty, PointerProperty, StringProperty
from bpy.types import Object, Text, Operator, Panel, PropertyGroup


class ConfigSplit(PropertyGroup):
    text_file: StringProperty(description="Textfile to show")

class SEQUENCER_OP_split_text_strips(Operator):
    """Split text strips"""
    bl_idname = "sequencer.split_text_strips"
    bl_label = "Split Text Strips"

    source_file: StringProperty(name='File')

    def draw(self, context):
        layout = self.layout
        layout.prop_search(self, "source_file", bpy.data, 'texts')

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        print(self.source_file)
        return {'FINISHED'}

class SEQUENCER_PT_split_text_strips(Panel):
    pass

def register():
    bpy.utils.register_class(ConfigSplit)
    bpy.utils.register_class(SEQUENCER_OP_split_text_strips)

def unregister():
    bpy.utils.unregister_class(SEQUENCER_OP_split_text_strips)
    bpy.utils.unregister_class(ConfigSplit)

if __name__ == "__main__":
    register()
