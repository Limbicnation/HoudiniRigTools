import hou

def adjust_attrib_gain():
    # Get the attribadjustcolor node
    aac_node = hou.node('/obj/geo1/attribadjustcolor1')

    # Get the slider value
    slider_value = hou.parm('/obj/other_hda/gain').eval()

    # Set the gain parameter on the attribadjustcolor node
    aac_node.parm('gain').set(slider_value)

# Register the adjust_attrib_gain function with the slider parameter's valueChanged event
hou.parm('/obj/other_hda/gain').addChangeCallback(adjust_attrib_gain)
