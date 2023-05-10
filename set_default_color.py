import hou

def reset_node_color():
    # Get the node you want to reset the color of
    node = hou.node("/obj/PoseNet_Control_Rig_HDA/PoseNet_Control_Rig/Controls")

    if not node:
        print("Error: Node not found!")
        return

    # Get the parm tuple for the color parameter
    color_parm = hou.parmTuple('/obj/PoseNet_Control_Rig_HDA/PoseNet_Control_Rig/Controls/left_arm')

    if not color_parm:
        print("Error: Color parameter not found on node!")
        return

    # Reset the color of the node to the default color
    color_parm.set((1.0, 0.0, 0.0))

# Define the callback function for the button
def reset_node_color_callback():
    reset_node_color()

# Add the button to the shelf
shelf = hou.ui.curDesktop().shelf()
button = shelf.addTool('reset_nodes', tool_type=hou.shelf.toolType.Python, icon='BUTTONS_reload', script='reset_node_color_callback()')
button.setHelp('Reset Node Colors')
