bl_info = {
    "name" : "Variants Switch",
    "author" : "Circle_Coder",
    "description" : "变体集切换",
    "blender" : (4, 5, 0),
    "version" : (1, 0, 0),
    "location" : "N-Panel",
    "waring" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Designer Tools"
}


import bpy
import bpy.utils.previews



def string_to_int(value):
    if value.isdigit():
        return int(value)
    return 0

def string_to_icon(value):
    if value in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys():
        return bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items[value].value
    return string_to_int(value)
    
def icon_to_string(value):
    for icon in bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items:
        if icon.value == value:
            return icon.name
    return "NONE"
    
def enum_set_to_string(value):
    if type(value) == set:
        if len(value) > 0:
            return "[" + (", ").join(list(value)) + "]"
        return "[]"
    return value
    
def string_to_type(value, to_type, default):
    try:
        value = to_type(value)
    except:
        value = default
    return value

addon_keymaps = {}
_icons = None
nodetree = {'sna_vairiantcollections_list': [], }
nodetree001 = {}
operators_collection_switch = {'sna_visible_collection_multi': [], 'sna_visible_collection_single': [], }


def sna_update_gpr_variantcollections_3A3C6(self, context):
    sna_updated_prop = self.gpr_variantcollections
    sna_function_execute_49671()
def sna_update_sna_index_variantcollections_185DE(self, context):
    sna_updated_prop = self.sna_index_variantcollections
    sna_function_execute_49671()
_item_map = dict()
def make_enum_item(_id, name, descr, preview_id, uid):
    lookup = str(_id)+"\0"+str(name)+"\0"+str(descr)+"\0"+str(preview_id)+"\0"+str(uid)
    if not lookup in _item_map:
        _item_map[lookup] = (_id, name, descr, preview_id, uid)
    return _item_map[lookup]
class SNA_UL_display_collection_list_E8F8F(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index_E8F8F):
        row = layout
        row_173A1 = layout.row(heading='', align=True)
        row_173A1.alert = False
        row_173A1.enabled = True
        row_173A1.use_property_split = False
        row_173A1.use_property_decorate = False
        row_173A1.scale_x = 1.0
        row_173A1.scale_y = 1.0
        row_173A1.alignment = 'Expand'.upper()
        row_173A1.label(text='', icon="CHECKMARK")
        row_173A1.prop(bpy.context.scene.sna_collection_variantcollections[index_E8F8F], 'gpr_variantcollections', text='', icon_value=0, emboss=True)
        
def sna_update_sna_tooglemode_DD2FD(self, context):
    sna_updated_prop = self.sna_tooglemode
    if sna_updated_prop:
        for i_7C9A2 in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            if bpy.data.collections[bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_7C9A2].name].hide_viewport:
                pass
            else:
                operators_collection_switch['sna_visible_collection_single'].append(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_7C9A2].name)
        for i_53B97 in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            if bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_53B97].name in operators_collection_switch['sna_visible_collection_multi']:
                sna_set_visible_D1E9C(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_53B97].name)
            else:
                sna_set_hidden_D7349(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_53B97].name)
        operators_collection_switch['sna_visible_collection_multi'] = []
    else:
        for i_073A9 in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            if bpy.data.collections[bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_073A9].name].hide_viewport:
                pass
            else:
                operators_collection_switch['sna_visible_collection_multi'].append(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_073A9].name)
        for i_57C2F in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            if bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_57C2F].name in operators_collection_switch['sna_visible_collection_single']:
                sna_set_visible_D1E9C(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_57C2F].name)
            else:
                sna_set_hidden_D7349(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_57C2F].name)
        operators_collection_switch['sna_visible_collection_single'] = []

class SNA_OT_Update_Variant_Collections_2Aacb(bpy.types.Operator):
    bl_idname = "sna.update_variant_collections_2aacb"
    bl_label = "更新变体集"
    bl_description = "如果没有任何显示，点这个按钮更新一下"
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        sna_function_execute_49671()
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
def sna_function_execute_49671():
    nodetree['sna_vairiantcollections_list'] = []
    for i_4FDEB in range(len(bpy.context.scene.sna_collection_variantcollections)):
        nodetree['sna_vairiantcollections_list'].append([bpy.context.scene.sna_collection_variantcollections[i_4FDEB].gpr_variantcollections.name, bpy.context.scene.sna_collection_variantcollections[i_4FDEB].gpr_variantcollections.name, '', 250])
class SNA_OT_Down_A4Bd3(bpy.types.Operator):
    bl_idname = "sna.down_a4bd3"
    bl_label = "Down"
    bl_description = "Move current variant collection down"
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        bpy.context.scene.sna_collection_variantcollections.move(bpy.context.scene.sna_index_variantcollections, int(bpy.context.scene.sna_index_variantcollections + 1.0))
        item_C4394 = bpy.context.scene.sna_collection_variantcollections[int(bpy.context.scene.sna_index_variantcollections + 1.0)]
        bpy.context.scene.sna_index_variantcollections = int(bpy.context.scene.sna_index_variantcollections + 1.0)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_OT_Remove_55F23(bpy.types.Operator):
    bl_idname = "sna.remove_55f23"
    bl_label = "Remove"
    bl_description = "Remove current variant collection"
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        if len(bpy.context.scene.sna_collection_variantcollections) > bpy.context.scene.sna_index_variantcollections:
            bpy.context.scene.sna_collection_variantcollections.remove(bpy.context.scene.sna_index_variantcollections)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_OT_Up_258D5(bpy.types.Operator):
    bl_idname = "sna.up_258d5"
    bl_label = "Up"
    bl_description = "Move current variant collection up"
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        bpy.context.scene.sna_collection_variantcollections.move(bpy.context.scene.sna_index_variantcollections, int(bpy.context.scene.sna_index_variantcollections - 1.0))
        item_3F866 = bpy.context.scene.sna_collection_variantcollections[int(bpy.context.scene.sna_index_variantcollections - 1.0)]
        bpy.context.scene.sna_index_variantcollections = int(bpy.context.scene.sna_index_variantcollections - 1.0)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_OT_Add_Ef6F0(bpy.types.Operator):
    bl_idname = "sna.add_ef6f0"
    bl_label = "Add"
    bl_description = "Add a new Variant Collection"
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        item_A8FC1 = bpy.context.scene.sna_collection_variantcollections.add()
        item_A8FC1.gpr_variantcollections = bpy.context.collection
        sna_function_execute_49671()
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
def sna_selected_variantcollection_enum_items(self, context):
    enum_items = nodetree['sna_vairiantcollections_list']
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]
class SNA_PT_COLLECTION_VARIANTS_51FDF(bpy.types.Panel):
    bl_label = '变体集切换'
    bl_idname = 'SNA_PT_COLLECTION_VARIANTS_51FDF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = '变体集切换'
    bl_order = 1
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    @classmethod
    def poll(cls, context):
        return not (False)
    
    def draw_header(self, context):
        layout = self.layout
        
    def draw(self, context):
        layout = self.layout
        col_6DCB6 = layout.column(heading='', align=True)
        col_6DCB6.alert = False
        col_6DCB6.enabled = True
        col_6DCB6.use_property_split = False
        col_6DCB6.use_property_decorate = False
        col_6DCB6.scale_x = 1.0
        col_6DCB6.scale_y = 1.0
        col_6DCB6.alignment = 'Expand'.upper()
        col_6DCB6.prop(bpy.context.scene, 'sna_toggle_variantcollectionssetup',
                       text='关闭变体集设置' if bpy.context.scene.sna_toggle_variantcollectionssetup else '打开变体集设置',
                       icon_value=0, emboss=True, toggle=True,
                       invert_checkbox=bpy.context.scene.sna_toggle_variantcollectionssetup)
        if bpy.context.scene.sna_toggle_variantcollectionssetup:
            row_8AF32 = col_6DCB6.row(heading='', align=True)
            row_8AF32.alert = False
            row_8AF32.enabled = True
            row_8AF32.use_property_split = False
            row_8AF32.use_property_decorate = False
            row_8AF32.scale_x = 1.0
            row_8AF32.scale_y = 1.0
            row_8AF32.alignment = 'Expand'.upper()
            row_8AF32.template_list('SNA_UL_display_collection_list_E8F8F', 'Display Collection List',
                                    bpy.context.scene, 'sna_collection_variantcollections', bpy.context.scene,
                                    'sna_index_variantcollections', rows=3)
            col_AF001 = row_8AF32.column(heading='', align=True)
            col_AF001.alert = False
            col_AF001.enabled = True
            col_AF001.use_property_split = False
            col_AF001.use_property_decorate = False
            col_AF001.scale_x = 1.0
            col_AF001.scale_y = 1.0
            col_AF001.alignment = 'Expand'.upper()
            op = col_AF001.operator('sna.add_ef6f0', text='', icon="ADD", emboss=True, depress=False)
            op = col_AF001.operator('sna.remove_55f23', text='', icon="TRASH", emboss=True, depress=False)
            # op = col_AF001.operator('sna.up_258d5', text='', icon="TRIA_UP", emboss=True, depress=False)
            # op = col_AF001.operator('sna.down_a4bd3', text='', icon="TRIA_DOWN", emboss=True, depress=False)
        else:
            pass

        
class SNA_OT_Op_All_On_Fe88D(bpy.types.Operator):
    bl_idname = "sna.op_all_on_fe88d"
    bl_label = "OP_All_ON"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        for i_AF11A in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            sna_set_visible_D1E9C(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_AF11A].name)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_OT_Op_All_Off_7Be70(bpy.types.Operator):
    bl_idname = "sna.op_all_off_7be70"
    bl_label = "OP_All_OFF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        for i_549CB in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            sna_set_hidden_D7349(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_549CB].name)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_OT_Op_Invert_Visible_Dede2(bpy.types.Operator):
    bl_idname = "sna.op_invert_visible_dede2"
    bl_label = "OP_INVERT VISIBLE"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        for i_D5101 in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            if bpy.data.collections[bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_D5101].name].hide_viewport:
                sna_set_visible_D1E9C(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_D5101].name)
            else:
                sna_set_hidden_D7349(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_D5101].name)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
def sna_set_visible_D1E9C(input):
    bpy.data.collections[input].hide_viewport = False
    bpy.data.collections[input].hide_render = False
def sna_set_hidden_D7349(input):
    bpy.data.collections[input].hide_viewport = True
    bpy.data.collections[input].hide_render = True
class SNA_OT_Toggle_Collections_53977(bpy.types.Operator):
    bl_idname = "sna.toggle_collections_53977"
    bl_label = "Toggle Collections"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    
    
    sna_selected_collection: bpy.props.StringProperty(name='Selected Collection', description='', default='', subtype='NONE', maxlen=0)
    
    @classmethod
    def poll(cls, context):
        return not False
    def execute(self, context):
        if bpy.context.scene.sna_tooglemode:
            bpy.data.collections[self.sna_selected_collection].hide_viewport = not bpy.data.collections[self.sna_selected_collection].hide_viewport
        else:
            for i_2FE2E in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
                if bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2FE2E].name == self.sna_selected_collection:
                    sna_set_visible_D1E9C(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2FE2E].name)
                else:
                    sna_set_hidden_D7349(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2FE2E].name)
        return {"FINISHED"}
    
    def invoke(self, context, event):
        
        
        return self.execute(context)
class SNA_PT_NEW_PANEL_C3C1F(bpy.types.Panel):
    bl_label = 'New Panel'
    bl_idname = 'SNA_PT_NEW_PANEL_C3C1F'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    
    bl_order = 0
    bl_options = {'HIDE_HEADER'}
    bl_parent_id = 'SNA_PT_COLLECTION_VARIANTS_51FDF'
    @classmethod
    def poll(cls, context):
        return not (False)
    
    def draw_header(self, context):
        layout = self.layout
        
    def draw(self, context):
        layout = self.layout
        col_E8B33 = layout.column(heading='', align=True)
        col_E8B33.alert = False
        col_E8B33.enabled = True
        col_E8B33.use_property_split = False
        col_E8B33.use_property_decorate = False
        col_E8B33.scale_x = 1.0
        col_E8B33.scale_y = 1.0
        col_E8B33.alignment = 'Expand'.upper()
        row_926CB = col_E8B33.row(heading='', align=True)
        row_926CB.alert = False
        row_926CB.enabled = True
        row_926CB.use_property_split = False
        row_926CB.use_property_decorate = False
        row_926CB.scale_x = 1.0
        row_926CB.scale_y = 1.0
        row_926CB.alignment = 'Expand'.upper()
        op = row_926CB.operator('sna.update_variant_collections_2aacb', text='', icon="FILE_REFRESH", emboss=True, depress=False)
        row_926CB.prop(bpy.context.scene, 'sna_selected_variantcollection', text='', icon_value=0, emboss=True)
        # row_926CB.prop(bpy.context.scene, 'sna_tooglemode', text='Toggle Single' if bpy.context.scene.sna_tooglemode else 'Toggle Multi', icon_value=0, emboss=True, toggle=True, invert_checkbox=bpy.context.scene.sna_tooglemode)
        row_3F71D = col_E8B33.row(heading='', align=True)
        row_3F71D.alert = False
        row_3F71D.enabled = True
        row_3F71D.use_property_split = False
        row_3F71D.use_property_decorate = False
        row_3F71D.scale_x = 1.0
        row_3F71D.scale_y = 1.0
        row_3F71D.alignment = 'Expand'.upper()

        for i_2BB19 in range(len(bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children)):
            op = col_E8B33.operator('sna.toggle_collections_53977', text=bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2BB19].name, icon_value=0, emboss=True, depress=not bpy.data.collections[bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2BB19].name].hide_viewport)
            op.sna_selected_collection = bpy.data.collections[bpy.context.scene.sna_selected_variantcollection].children[i_2BB19].name
class SNA_GROUP_sna_group_variantcollections(bpy.types.PropertyGroup):

    gpr_variantcollections: bpy.props.PointerProperty(name='GPR_VariantCollections', description='', type=bpy.types.Collection, update=sna_update_gpr_variantcollections_3A3C6)







def sna_selectionvsallobjects_enum_items(self, context):
    return [("No Items", "No Items", "No generate enum items node found to create items!", "ERROR", 0)]




def register():
    
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_GROUP_sna_group_variantcollections)
    bpy.types.Scene.sna_toggle_variantcollectionssetup = bpy.props.BoolProperty(name='Toggle_VariantCollectionsSetup', description='', default=False)
    bpy.types.Scene.sna_index_variantcollections = bpy.props.IntProperty(name='Index_VariantCollections', description='Select Variant Collection to move or remove', default=0, subtype='NONE', min=0, update=sna_update_sna_index_variantcollections_185DE)
    bpy.types.Scene.sna_collection_variantcollections = bpy.props.CollectionProperty(name='Collection_VariantCollections', description='', type=SNA_GROUP_sna_group_variantcollections)
    bpy.types.Scene.sna_selected_variantcollection = bpy.props.EnumProperty(name='选择变体集', description='', items=sna_selected_variantcollection_enum_items)
    bpy.types.Scene.sna_tooglemode = bpy.props.BoolProperty(name='ToogleMode', description='', default=False, update=sna_update_sna_tooglemode_DD2FD)
    bpy.types.Scene.sna_selectionvsallobjects = bpy.props.EnumProperty(name='SelectionVSallobjects', description='', items=[('Selection only', 'Selection only', 'Sections will only be visible on the selected object(s)', 0, 0), ('All objects', 'All objects', 'Sections will be visible on all objects', 0, 1)])
    
    
    bpy.utils.register_class(SNA_OT_Update_Variant_Collections_2Aacb)
    bpy.utils.register_class(SNA_OT_Down_A4Bd3)
    bpy.utils.register_class(SNA_OT_Remove_55F23)
    bpy.utils.register_class(SNA_OT_Up_258D5)
    bpy.utils.register_class(SNA_OT_Add_Ef6F0)
    bpy.utils.register_class(SNA_PT_COLLECTION_VARIANTS_51FDF)
    bpy.utils.register_class(SNA_UL_display_collection_list_E8F8F)
    bpy.utils.register_class(SNA_OT_Op_All_On_Fe88D)
    bpy.utils.register_class(SNA_OT_Op_All_Off_7Be70)
    bpy.utils.register_class(SNA_OT_Op_Invert_Visible_Dede2)
    bpy.utils.register_class(SNA_OT_Toggle_Collections_53977)
    bpy.utils.register_class(SNA_PT_NEW_PANEL_C3C1F)

def unregister():
    
    global _icons
    bpy.utils.previews.remove(_icons)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_selectionvsallobjects
    del bpy.types.Scene.sna_tooglemode
    del bpy.types.Scene.sna_selected_variantcollection
    del bpy.types.Scene.sna_collection_variantcollections
    del bpy.types.Scene.sna_index_variantcollections
    del bpy.types.Scene.sna_toggle_variantcollectionssetup
    bpy.utils.unregister_class(SNA_GROUP_sna_group_variantcollections)
    
    
    bpy.utils.unregister_class(SNA_OT_Update_Variant_Collections_2Aacb)
    bpy.utils.unregister_class(SNA_OT_Down_A4Bd3)
    bpy.utils.unregister_class(SNA_OT_Remove_55F23)
    bpy.utils.unregister_class(SNA_OT_Up_258D5)
    bpy.utils.unregister_class(SNA_OT_Add_Ef6F0)
    bpy.utils.unregister_class(SNA_PT_COLLECTION_VARIANTS_51FDF)
    bpy.utils.unregister_class(SNA_UL_display_collection_list_E8F8F)
    bpy.utils.unregister_class(SNA_OT_Op_All_On_Fe88D)
    bpy.utils.unregister_class(SNA_OT_Op_All_Off_7Be70)
    bpy.utils.unregister_class(SNA_OT_Op_Invert_Visible_Dede2)
    bpy.utils.unregister_class(SNA_OT_Toggle_Collections_53977)
    bpy.utils.unregister_class(SNA_PT_NEW_PANEL_C3C1F)

