import hou


def reset_node_color():
    # Get the node you want to reset the color of
    node = hou.node("/obj/PoseNet_Control_Rig_HDA/PoseNet_Control_Rig/Controls")

    if not node:
        print("Error: Node not found!")
        return

    # Define a dictionary of parameter names and their corresponding normalized RGB values
    # Use the Label parameter name
    param_dict = {
        'left_arm_color': (0.43529411764705883, 0.13725490196078433, 0.0),
        'left_shoulder_color': (0.23529411764705882, 0.7372549019607844, 0.0),
        'left_upper_arm_color': (0.2823529411764706, 0.43529411764705883, 0.0),
        'left_elbow_color': (0.28627450980392155, 0.43529411764705883, 0.0),
        'left_lower_arm_color': (0.13725490196078433, 0.4392156862745098, 0.0),
        'left_wrist_color': (0.0, 0.7333333333333333, 0.23137254901960785),

        'Left_Upper_Body': (0.0, 0.6, 0, 6),

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
# shelf = hou.ui.curDesktop().shelf()
# button = shelf.addTool('reset_nodes', tool_type=hou.shelf.toolType.Python, icon='BUTTONS_reload', script='reset_node_color_callback()')
# button.setHelp('Reset Node Colors')
