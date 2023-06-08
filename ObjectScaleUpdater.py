import hou

def update_scale(**kwargs):
    # Get the current transform node
    node = kwargs["/obj/PoseNet_Control_Rig/transform4"].node()

    # Get the Y and Z scale parameters
    y_scale = node.parm('scaley')
    z_scale = node.parm('scalez')

    # Define the range for the slider (0 to 1)
    slider_min = 0
    slider_max = 1

    # Get the slider value
    slider_value = node.parm('slider').eval()

    # Calculate the new Y and Z scale values based on the slider value
    new_y_scale = slider_value
    new_z_scale = 1 - slider_value

    # Set the new Y and Z scale values using setWorldTransform
    matrix = hou.Matrix4()
    matrix.setToIdentity()
    matrix.setScale(hou.Vector3(1, new_y_scale, new_z_scale))
    node.setWorldTransform(matrix)

# Register the update_scale function with the slider and scale parameters' changed events
hou.parm('/obj/PoseNet_Control_Rig/transform4/scaley')
hou.parm('/obj/PoseNet_Control_Rig/transform4/scalez')
hou.parm('/obj/PoseNet_Control_Rig/transform4/slider')
