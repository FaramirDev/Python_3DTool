import maya.cmds as cmds
import os 

###### ======= 
## MADE by Alexis Rousseau
## Version : 6 
## Date : 23/05/2025
###### ======= 

## SET env fbx 
mel.eval('FBXPushSettings;')

## SET Images
image_path_teeth = "Miraculous_Tool3D/asset/T_D_Teeth.1001.png"  
image_path_Lashes_boy = "Miraculous_Tool3D/asset/T_O_Lashes_Masked_Boy.1001.png" 
image_path_Lashes_girl = "Miraculous_Tool3D/asset/T_O_Lashes_Masked_Girl.1001.png" 
logo = "Miraculous_Tool3D/asset/miraculous_logo.png"

## SET Path fbx AutoTransfert pour Body_msh
auto_transfert_path = "Miraculous_Tool3D/asset/body_msh.fbx"


####################
## == Fonction == ##

def rename_node():
    selection = cmds.ls(selection=True)
    
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    base_name = os.path.splitext(scene_name)[0]  
    new_name = 'Mi_' + base_name.split('_')[0] + "_" 
    
    cmds.rename(selection[0], new_name)
    print("rename Ok")

def add_file():
    selection = cmds.ls(selection=True)

    if not selection:
        cmds.warning("Veuillez sélectionner un mat de Type Lambert. Ty")
        return

    
    node_type = cmds.nodeType(selection[0])
    if node_type != 'lambert':
        cmds.warning("Only Lambert.")
        return

    lambert_name = selection[0]

    file_node = cmds.shadingNode('file', asTexture=True, name=f"{lambert_name}_file")

    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=f"{lambert_name}_place2dTexture")

    cmds.connectAttr(f'{place2d_node}.outUV', f'{file_node}.uvCoord', force=True)
    cmds.connectAttr(f'{place2d_node}.outUvFilterSize', f'{file_node}.uvFilterSize', force=True)

    cmds.connectAttr(f'{file_node}.outColor', f'{lambert_name}.color', force=True)

def add_lambert_file():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')
 
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
 
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_clothes(): 
    scene_name = cmds.file(query=True, sceneName=True, shortName=True) 
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Clothes' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name) 
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture') 
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_acces():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Acces'
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')

    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')

    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_skin():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Skin'
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_hair(): 
    scene_name = cmds.file(query=True, sceneName=True, shortName=True) 
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Hair' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name) 
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')
    cmds.setAttr(lambert_shader + '.color', 0.37, 0.28, 0.15, type='double3')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_glass(): 
    scene_name = cmds.file(query=True, sceneName=True, shortName=True) 
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Glass' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name) 
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')
    cmds.setAttr(lambert_shader + '.color', 0.52, 0.6, 0.6, type='double3')
    cmds.setAttr(lambert_shader + '.transparency', 0.92, 0.92, 0.92, type='double3')

    print(f"Shader Lambert '{lambert_name}'a été créé.")

def add_lambert_lashes_girl():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Lashes' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    cmds.setAttr(lambert_shader + '.color', 0, 0, 0, type='double3')
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outTransparency', lambert_shader + '.transparency')
    cmds.connectAttr(lambert_shader + '.outTransparency', shading_group + '.surfaceShader')
    cmds.setAttr(file_node + '.fileTextureName', image_path_Lashes_girl, type='string')
    
    print(f"Shader Lambert '{lambert_name}' créé avec texture.")

def add_lambert_lashes_boy():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Lashes' 
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    cmds.setAttr(lambert_shader + '.color', 0, 0, 0, type='double3')
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outTransparency', lambert_shader + '.transparency')
    cmds.connectAttr(lambert_shader + '.outTransparency', shading_group + '.surfaceShader')
    cmds.setAttr(file_node + '.fileTextureName', image_path_Lashes_boy, type='string')
    
    print(f"Shader Lambert '{lambert_name}' créé avec texture.")

def add_lambert_teeth():
    scene_name = cmds.file(query=True, sceneName=True, shortName=True)
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_Teeth'
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name)
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture')
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')
    cmds.setAttr(file_node + '.fileTextureName', image_path_teeth, type='string')

    print(f"Shader Lambert '{lambert_name}' créé avec texture.")
    
def uv_set_reset():
    geo_group = cmds.listRelatives('GEO', allDescendents=True, type='transform', fullPath=True)

    if not geo_group:
        cmds.warning("Aucun objet trouvé dans le groupe 'GEO'.")
        return

    for transform in geo_group:
        shapes = cmds.listRelatives(transform, shapes=True, type='mesh', fullPath=True)
        if not shapes or len(shapes) > 1:
            continue

        mesh = shapes[0]
        uv_sets = cmds.polyUVSet(mesh, query=True, allUVSets=True)

        if uv_sets:
            cmds.polyUVSet(mesh, currentUVSet=True, uvSet=uv_sets[0])
            print(f"Le premier UV set '{uv_sets[0]}' a été sélectionné pour la shape '{mesh}'.")
        else:
            cmds.warning(f"La shape '{mesh}' sous le transform '{transform}' n'a pas de UV sets.")

def auto_export():
    path = cmds.file(query=True, sceneName=True)
    path_export = path.replace("UV", "Exports")

    if cmds.objExists("GEO"):
        cmds.duplicate("GEO", name="GEO_Export")

    objects = cmds.listRelatives("GEO_Export", children=True, fullPath=True) 
    
    for obj in objects:
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)
        if any(cmds.objectType(shape) == "mesh" for shape in shapes):
            cmds.select(obj, replace=True)
            cmds.polySmooth(
        	obj,
        	subdivisionType=2,
        	osdVertBoundary=1,
        	osdFvarBoundary=1,
        	osdFvarPropagateCorners=0,
        	osdSmoothTriangles=0,
        	osdCreaseMethod=0,
        	divisions=1,
        	constructionHistory=False,)


    all_selection= cmds.listRelatives("GEO_Export", allDescendents=True, fullPath=True) or []
    
    meshes = [obj for obj in all_selection if cmds.objectType(obj) == "mesh"]
    
    if meshes:
        cmds.select(meshes, replace=True)
        selection = cmds.ls(selection=True, long=True)
        cmds.file(path_export, exportSelected=True, type="FBX export", force=True, prompt=False)

    cmds.delete("GEO_Export") 

    print("Fonction auto export a été exécutée")

def auto_transfert_uv():
    coucou = cmds.file(auto_transfert_path, i=True, type="FBX", returnNewNodes=True)
    name_fbx = "body_for_transfert"

    geo_group = "GEO"
    body = geo_group + "|body__msh"

    uv_sets = cmds.polyUVSet(body, query=True, allUVSets=True)

    default_uv_set = uv_sets[0]  
    for uv_set in uv_sets:
        if uv_set != default_uv_set:
            cmds.polyUVSet(body, uvSet=uv_set, delete=True)

    # Rename UV set 0 sinon bug
    new_name_default = "kill"  
    cmds.polyUVSet(body, rename=True, newUVSet=new_name_default , uvSet=default_uv_set)

    # Transfer de Attrib UV du mesh a body
    transfert = cmds.transferAttributes(name_fbx, body, transferPositions=0, transferNormals=0, transferUVs=2, transferColors=0, sampleSpace=4, searchMethod=3, flipUVs=False)

    try:
        transfert
        print("Le Transfert est ok")
        ## RESET les uv set avec leur nouveau nom
        uv_sets = cmds.polyUVSet(body, query=True, allUVSets=True)
        default_uv_set = uv_sets[0]

       
        uv_set_2 = cmds.polyUVSet(body, query=True, allUVSets=True)[1]
        cmds.polyUVSet(body, copy=True, uvSet=uv_set_2, newUVSet=default_uv_set)

        # Renaaame le UVset par défaut avec la basecolor
        new_uv_set_name = "BaseColor"  
        cmds.polyUVSet(body, rename=True, newUVSet=new_uv_set_name, uvSet=default_uv_set)

        # Supprl'UVset 1
        cmds.polyUVSet(body, delete=True, uvSet=uv_set_2)

        # Supp all histo
        cmds.select(body)
        cmds.delete(constructionHistory=True)

        # Supp le mesh importe de base
        cmds.delete(coucou)

    except:
        print("Il y a eu une erreur lors du transfert")
        cmds.delete(coucou)

def rename_shader_engines():
    lambert_shaders = cmds.ls(type='lambert')

    for shader in lambert_shaders:
        shading_engines = cmds.listConnections(shader, type='shadingEngine')

        if shading_engines:
            for sg in shading_engines:
                try:
                    if not cmds.getAttr(f'{sg}.nodeState') == 1: 
                        new_name = shader + 'SG'
                        cmds.rename(sg, new_name)
                        print(f'Renamed {sg} to {new_name}')
                except RuntimeError:
                    pass

def clean_scene():
    if not cmds.objExists('GEO'):
        cmds.warning("Le groupe 'GEO' n'existe pas dans la scène.")
        return

    geo_group = cmds.listRelatives('GEO', allDescendents=True, type='mesh', fullPath=True)

    if not geo_group:
        cmds.warning("Aucun mesh trouvé sous le groupe 'GEO'.")
        return
 
    for mesh in geo_group:
        if cmds.objExists(mesh):
            cmds.delete(mesh, constructionHistory=True)
            print(f"Historique supprimé pour le mesh : {mesh}")
        else:
            print(f"Le mesh {mesh} n'existe pas dans la scène.")

    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

    print("Noeuuds inutilisés supprimés. It's oook boys")

def reset_pivot():
    geo_group = cmds.listRelatives('GEO', allDescendents=True, type='mesh', fullPath=True)
    if geo_group is None:
        print("Aucun mesh dans le 'GEO'.")
        return

    for mesh in geo_group:
        if cmds.objExists(mesh):
            transform = cmds.listRelatives(mesh, parent=True, fullPath=True)[0]
            
            cmds.setAttr(f'{transform}.translate', 0, 0, 0)
            cmds.setAttr(f'{transform}.rotate', 0, 0, 0)
            cmds.setAttr(f'{transform}.scale', 1, 1, 1)
            
            cmds.xform(transform, worldSpace=True, pivots=(0, 0, 0))
            print(f'Reset ok.')
    
def reset_display_color():
    groupe = "GEO"
    if not cmds.objExists(groupe):
        cmds.warning(f"Le gr '{groupe}' n'existe pas. mais devrait exister ahah")
        return
 
    list_obj = cmds.listRelatives(groupe, allDescendents=True, type='mesh', fullPath=True) or []

    if not list_obj:
        cmds.warning(f"Aucun mesh trouvé dans le gr :'{groupe}'.")
        return

    for mesh in list_obj:
        try:
            cmds.setAttr(f"{mesh}.displayColors", 0)
            print(f"Display colors désactivé pour : {mesh}")
        except Exception as e:
            cmds.warning(f"Erreur sur {mesh} : {e}")
    			
def all_lambert_boy():
    add_lambert_clothes()
    add_lambert_acces()
    add_lambert_skin()
    add_lambert_lashes_boy()
    add_lambert_teeth()
    add_lambert_hair()

def all_lambert_girl():
    add_lambert_clothes()
    add_lambert_acces()
    add_lambert_skin()
    add_lambert_lashes_girl()
    add_lambert_teeth()
    add_lambert_hair()

def create_shader_perso(field_id):
    nom_shader = cmds.textField(field_id, query=True, text=True)

    scene_name = cmds.file(query=True, sceneName=True, shortName=True) 
    lambert_name = 'Mi_' + scene_name.split('_')[0] + '_' + nom_shader
    lambert_shader = cmds.shadingNode('lambert', asShader=True, name=lambert_name) 
    file_node = cmds.shadingNode('file', asTexture=True, name=lambert_name + 'FileTexture') 
    place2d_node = cmds.shadingNode('place2dTexture', asUtility=True, name=lambert_name + 'Place2dTexture')
    cmds.connectAttr(place2d_node + '.outUV', file_node + '.uvCoord')
    cmds.connectAttr(place2d_node + '.outUvFilterSize', file_node + '.uvFilterSize')
    shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_name + 'SG')
    cmds.connectAttr(file_node + '.outColor', lambert_shader + '.color')
    cmds.connectAttr(lambert_shader + '.outColor', shading_group + '.surfaceShader')

def create_fxtransform_uvset():
    selected_meshes = cmds.ls(selection=True, dag=True, type='mesh')
 
    if not selected_meshes:
        cmds.warning("Aucun mesh sélectionné.")
        return
 
    for mesh in selected_meshes:
        uv_sets = cmds.polyUVSet(mesh, query=True, allUVSets=True) or []
 
        if "FXTransform" in uv_sets:
            print(f"UV Set 'FXTransform' existe déjà sur {mesh}.")
            continue
 
        base_uv_set = uv_sets[0] if uv_sets else "map1"
 
        cmds.polyUVSet(mesh, copy=True, newUVSet="FXTransform", uvSet=base_uv_set)
        cmds.polyUVSet(mesh, currentUVSet=True, uvSet="FXTransform")
 
        print(f"UV Set 'FXTransform' créé sur {mesh}.")

def add_button(label, command, color=(0.2, 0.2, 0.2)):
    cmds.button(label=label, command=command, backgroundColor=color, height=30 )
    
## == INTERFACE == ## 

def create_ui():  
    if cmds.window("CharaTool", exists=True):
        cmds.deleteUI("CharaTool")

    window = cmds.window("CharaTool", title=" CHARA TOOL v6", widthHeight=(1,1), sizeable=False, )

    cmds.scrollLayout(horizontalScrollBarThickness=0)
    cmds.columnLayout(adjustableColumn=True)

    if os.path.exists(logo):
        cmds.rowLayout(numberOfColumns=1, columnAlign=(1, 'center'))
        cmds.image(image=logo,height=80)
        cmds.setParent("..")
  
    cmds.frameLayout(label="1. RENAME and CLEAN", collapsable=True, marginHeight=8, marginWidth=6)
    cmds.columnLayout(adjustableColumn=True)

    add_button("Rename Node Asset Selected", "rename_node()", color=[0.15, 0.15, 0.4])
    add_button("Rename ALL SG", "rename_shader_engines()", color=[0.2, 0.15, 0.45])
    cmds.separator(height=10, style='in')
    add_button("Clean Histo - ShaderNotUsed", "clean_scene()", color=[0.1, 0.35, 0.4])
    add_button("Reset Pivot", "reset_pivot()", color=[0.15, 0.25, 0.42])
    add_button("Reset DisplayColor", "reset_display_color()", color=[0.2, 0.32, 0.42])

    cmds.setParent("..")
    cmds.setParent("..")

    cmds.frameLayout(label="2. SHADER", collapsable=True, marginHeight=8, marginWidth=6)
    cmds.columnLayout(adjustableColumn=True)  

    cmds.separator(height=10, style='in')
    cmds.text(label="Ajoute File Texture au Lambert sélectionné", align="center")
    add_button("Add file au Lambert", "add_file()", color=[0.1, 0.1, 0.4])

    cmds.separator(height=10, style='in')
    
    cmds.text(label="Nom du Shader :", align="left", height=15)
    asset_name_field = cmds.textField(placeholderText="Entrez le nom ici...")
    cmds.button(label="Create Shader", command=lambda x: create_shader_perso(asset_name_field), backgroundColor=(0.4, 0.1, 0.5))
    cmds.separator(height=10, style='in')

    cmds.text(label="Shader", align="center", height=15)
    add_button("Lambert Clothes", "add_lambert_clothes()", color=[0.2, 0.3, 0.5])
    add_button("Lambert Acces", "add_lambert_acces()", color=[0.3, 0.25, 0.45])
    add_button("Lambert Skin", "add_lambert_skin()", color=[0.28, 0.22, 0.485])
    add_button("Lambert Hair", "add_lambert_hair()", color=[0.22, 0.32, 0.45])
    add_button("Lambert Glass", "add_lambert_glass()", color=[0.32, 0.4, 0.35])

    cmds.separator(height=10, style='in')
    cmds.text(label="Lambert Lashes & Teeth", align="center")
    add_button("Lashes BOY", "add_lambert_lashes_boy()", color=[0.2, 0.4, 0.5])
    add_button("Lashes GIRL", "add_lambert_lashes_girl()", color=[0.35, 0.2, 0.4])
    add_button("Teeth", "add_lambert_teeth()", color=[0.2, 0.2, 0.4])

    cmds.separator(height=10, style='in')
    cmds.text(label="Lambert complet", align="center")
    add_button("All Lambert + Lashes Boy", "all_lambert_boy()", color=[0.2, 0.4, 0.5])
    add_button("All Lambert + Lashes Girl", "all_lambert_girl()", color=[0.4, 0.2, 0.4])

    cmds.setParent("..")
    cmds.setParent("..")

    cmds.frameLayout(label="3. Tool MESH", collapsable=True, marginHeight=8, marginWidth=6)
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="UVSet -> 1 pour tous les mesh du gr_Geo", align="center")
    add_button("Set UVSet to 1", "uv_set_reset()", color=[0.05, 0.5, 0.2])

    cmds.separator(height=10, style='in')
    cmds.text(label="Smooth + Export automatique pour Substance", align="center")
    add_button("Auto Export Painter", "auto_export()", color=[0.2, 0.5, 0.2])

    cmds.separator(height=10, style='in')
    cmds.text(label="Transfert UVset Body_msh", align="center")
    add_button("AutoTransfert UVset Body", "auto_transfert_uv()", color=[0.15, 0.5, 0.3])

    cmds.separator(height=10, style='in')
    cmds.text(label="ADD UVset ( Select Mesh )", align="center")
    add_button("Add FXTransform UVset", "create_fxtransform_uvset()", color=[0.2, 0.45, 0.4])

    cmds.setParent("..")
    cmds.setParent("..")

    cmds.separator(height=20, style='none')
    cmds.text(label="by Alexis Rousseau - v6", align="center", font="smallPlainLabelFont")
    cmds.separator(height=10, style='none')

    cmds.showWindow(window)

## == START == ## 
create_ui()