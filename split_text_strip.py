import bpy
from bpy.props import BoolProperty, PointerProperty, StringProperty
from bpy.types import Object, Text, Operator, Panel, PropertyGroup

bl_info = {
    'name': 'Split Sequencer Text Strip',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Split a VSE text strip from the contents of a text file',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-split-text-strip/issues'
}

def split_from_text(text):
    lines = [l.body.strip() for l in bpy.data.texts[text].lines if l.body.strip()]
    split_sequence(lines)

def split_sequence(lines=['aaa', 'bbb', 'cccc']):
    parts = len(lines)
    seq = bpy.context.selected_sequences[0]
    end = seq.frame_final_end
    start = seq.frame_final_start
    duration = seq.frame_final_duration

    assert duration > parts, 'sequence too short to be split'
    part_duration = duration / parts

    for (cut, line) in zip(range(start, end, int(part_duration)), lines):
        if cut > start:
            bpy.ops.sequencer.cut(frame=cut, type='SOFT', side='RIGHT')
        seq = bpy.context.selected_sequences[0]
        seq.text = line

class SEQUENCER_OP_split_text_strip(Operator):
    """Split Text Strip"""
    bl_idname = "sequencer.split_text_strip"
    bl_label = "Split Text Strip"

    source_file: StringProperty(name='File')

    def draw(self, context):
        layout = self.layout
        layout.prop_search(self, "source_file", bpy.data, 'texts')

    @classmethod
    def poll(cls, context):
        return len(context.selected_sequences) == 1

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        split_from_text(self.source_file)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SEQUENCER_OP_split_text_strip)

def unregister():
    bpy.utils.unregister_class(SEQUENCER_OP_split_text_strip)

if __name__ == "__main__":
    register()
