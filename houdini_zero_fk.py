import hou
import os

def ZeroAll():

    # This function sets t: and r: parms to zero
    
    # Grab reference to the list of nodes on the HDA
    
    fkControls = hou.pwd().parm('fkNodes').evalAsString().split()
    
    for fk in fkControls:
    
        fk = hou.node(fk)
        
        fk.parmTuple('t').set([0, 0, 0])
        fk.parmTuple('r').set([0, 0, 0])
