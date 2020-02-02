import bpy

def main(context):
    for ob in context.scene.objects:
        print(ob)

class SEQUENCER_OP_split_text_strips(bpy.types.Operator):
    """Split text strips"""
    bl_idname = "sequencer.split_text_strips"
    bl_label = "Split Text Strips"

    so: bpy.props.BoolProperty(name='Algo Boolérico', default=True)

    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SEQUENCER_OP_split_text_strips)

def unregister():
    bpy.utils.unregister_class(SEQUENCER_OP_split_text_strips)

if __name__ == "__main__":
    register()
