import hou

def ZeroAll():

    # This function sets t: and r: parms to zero

    # Grab reference to the list of nodes on the HDA

    fkControls = hou.pwd().parm('fkControlNodes').evalAsString().split()

    for fk in fkControls:

        fk = hou.node(fk)

        fk.parmTuple('t').set([0, 0, 0])
        fk.parmTuple('r').set([0, 0, 0])

def ToggleVisibility():

    # This function toggles the visibility of all the control nodes

    fkControls = hou.pwd().parm('fkControlNodes').evalAsString().split()
    fkTwistControls = hou.pwd().parm('fkTwistNodes').evalAsString().split()

    for fk in fkControls + fkTwistControls:

        fk = hou.node(fk)

        # Use the 'display' parameter to show/hide the control node
        current_display_value = fk.evalParm('display')
        fk.parm('display').set(1 - current_display_value)
        

def ToggleBonesVisibility():
    # This function toggles the visibility of all the bone nodes

    boneNodes = hou.pwd().parm('boneNodes').evalAsString().split()

    for bone in boneNodes:

        bone = hou.node(bone)

        # Use the 'display' parameter to show/hide the bone node
        current_display_value = bone.evalParm('display')
        bone.parm('display').set(1 - current_display_value)
        
def KeyFrame():
    # Create a keyframe on our Conrol Nodes

    fkControlNodes = hou.pwd().evalParm('fkControlNodes').split()
    for fk in fkControlNodes:
        fk = hou.node(fk)
        # Create our first keyframe object
        k = hou.Keyframe()
        k.setSlopeAuto(True)
        k.setInSlopeAuto(True)

        # Keyframe the rotation parameters

        # Check if the x channel is Locked
        if not fk.parm('rx').isLocked():
            k.setValue(fk.evalParm('rx'))
            # Set the actual keyframe
            fk.parm('rx').setKeyframe(k)

        # Check if the y channel is Locked
        if not fk.parm('ry').isLocked():
            k.setValue(fk.evalParm('ry'))
            # Set the actual keyframe
            fk.parm('ry').setKeyframe(k)

        # Check if the z channel is Locked
        if not fk.parm('rz').isLocked():
            k.setValue(fk.evalParm('rz'))
            # Set the actual keyframe
            fk.parm('rz').setKeyframe(k)

        # Keyframe the translation parameters

        # Check if the x channel is Locked
        if not fk.parm('tx').isLocked():
            k.setValue(fk.evalParm('tx'))
            # Set the actual keyframe
            fk.parm('tx').setKeyframe(k)

        # Check if the y channel is Locked
        if not fk.parm('ty').isLocked():
            k.setValue(fk.evalParm('ty'))
            # Set the actual keyframe
            fk.parm('ty').setKeyframe(k)

        # Check if the z channel is Locked
        if not fk.parm('tz').isLocked():
            k.setValue(fk.evalParm('tz'))
            # Set the actual keyframe
            fk.parm('tz').setKeyframe(k)
