import hou

def reset_node_color():
    # Get the node you want to reset the color of
    node = hou.node("/obj/PoseNet_Control_Rig_HDA/PoseNet_Control_Rig/Controls")

    if not node:
        print("Error: Node not found!")
        return

    # Define a dictionary of parameter names and their corresponding RGB values
    param_dict = {
        'left_arm': (34.0, 13.0, 0.0),
        'left_shoulder': (0.0, 1.0, 0.0),
        'left_Upper_arm': (0.0, 0.0, 1.0),
        'left_elbow': (1.0, 1.0, 0.0),
        'left_wrist': (1.0, 0.0, 1.0),
        
        'right_arm': (1.0, 0.0, 0.0),
        'right_shoulder': (0.0, 1.0, 0.0),
        'right_upper_arm': (0.0, 0.0, 1.0),
        'right_elbow': (1.0, 1.0, 0.0),
        'right_wrist': (1.0, 0.0, 1.0)
    }

    # Loop through the parameter dictionary and reset the color of each parameter to its corresponding RGB value
    for param_name, rgb_values in param_dict.items():
        color_parm = hou.parmTuple(f'/obj/PoseNet_Control_Rig_HDA/PoseNet_Control_Rig/Controls/{param_name}')
        if not color_parm:
            print(f"Error: Color parameter not found for {param_name}")
            continue
        color_parm.set(rgb_values)

# Define the callback function for the button
def reset_node_color_callback():
    reset_node_color()

# Add the button to the shelf
shelf = hou.ui.curDesktop().shelf()
button = shelf.addTool('reset_nodes', tool_type=hou.shelf.toolType.Python, icon='BUTTONS_reload', script='reset_node_color_callback()')
button.setHelp('Reset Node Colors')
