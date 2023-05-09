import hou

def ZeroAll():

    # This function sets t: and r: parms to zero

    # Grab reference to the list of nodes on the HDA

    fkControls = hou.pwd().parm('fkNodes').evalAsString().split()

    for fk in fkControls:

        fk = hou.node(fk)

        fk.parmTuple('t').set([0, 0, 0])
        fk.parmTuple('r').set([0, 0, 0])

# Implement the hide function as a toggle
def ToggleVisibility():

    # This function toggles the visibility of all the control nodes

    fkControls = hou.pwd().parm('fkNodes').evalAsString().split()
    fkTwistControls = hou.pwd().parm('fkTwistNodes').evalAsString().split()

    for fk in fkControls + fkTwistControls:

        fk = hou.node(fk)

        # Use the 'display' parameter to show/hide the control node
        current_display_value = fk.evalParm('display')
        fk.parm('display').set(1 - current_display_value)
        
def ToggleBonesVisibility():
    # Get the value of the 'boneNodes' parameter
    bone_nodes_param = hou.pwd().parm('boneNodes')
    if bone_nodes_param is None or not bone_nodes_param.eval():
        hou.ui.displayMessage("Error: 'boneNodes' parameter is not set.")
        return

    bone_nodes = bone_nodes_param.evalAsString().split()
    
    # Check if there are any bones in the list
    if not bone_nodes:
        hou.ui.displayMessage("Error: No bones found in 'boneNodes' parameter.")
        return
    
    for bone in bone_nodes:
        bone_node = hou.node(bone)
        if not bone_node:
            hou.ui.displayMessage(f"Error: Bone node '{bone}' not found.")
            continue
        
        # Use the 'tdisplay' parameter to show/hide the bone node
        current_display_value = bone_node.evalParm('tdisplay')
        if current_display_value:
            bone_node.parm('tdisplay').set(0)
        else:
            bone_node.parm('tdisplay').set(1)


def KeyAll():
    # Create a keyframe on our Conrol Nodes

    fkControl = hou.pwd().evalParm('fknNodes').split()
    for fk in fkControl:
        fk = hou.node(fk)
        # Create our first keyframe object
        k = hou.keyframe()
        k.setSlopeAuto(True)

        # Keyframe the rotation parameters

        # Check if the x channel is Locked
        if not fk.parm('rx').isLocked():
            k.setValue(fk.evalparm('rx'))
            # Set the actual keyframe
            fk.parm('rx').setKeyframe()
             
        # Check if the y channel is Locked
        if not fk.parm('ry').isLocked():
            k.setValue(fk.evalparm('ry'))
            # Set the actual keyframe
            fk.parm('ry').setKeyframe()

         # Check if the z channel is Locked
        if not fk.parm('rz').isLocked():
            k.setValue(fk.evalparm('rz'))
            # Set the actual keyframe
            fk.parm('rz').setKeyframe()
        
        # Keyframe the translation parameters

        # Check if the y channel is Locked
        if not fk.parm('tx').isLocked():
            k.setValue(fk.evalparm('tx'))
            # Set the actual keyframe
            fk.parm('ry').setKeyframe()

                    # Check if the y channel is Locked
        if not fk.parm('ty').isLocked():
            k.setValue(fk.evalparm('ty'))
            # Set the actual keyframe
            fk.parm('ty').setKeyframe()


        # Check if the y channel is Locked
        if not fk.parm('tz').isLocked():
            k.setValue(fk.evalparm('tz'))
            # Set the actual keyframe
            fk.parm('tz').setKeyframe()