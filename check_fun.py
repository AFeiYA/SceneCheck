#!/usr/bin/python
# -*- coding: utf-8 -*-
import unicodedata
import re
import maya.cmds as cmds
def duplicated_transform_nodes_check():
    d_list=[]
    tr_nodes =  cmds.ls( tr=True)
    filter(None, tr_nodes)   #remove NoneType
    maj_set = set(tr_nodes)
    duplicates = [f for f in maj_set if '|' in f]
    duplicates.sort(key=lambda obj:obj.count('|'), reverse = True)
    if duplicates:
        for name in duplicates:
            # extract the base name
            m = re.compile("[^|]*$").search(name)
            short_name=m.group(0)
            d_list.append(short_name)
    d_set = set(d_list)
    warning=""
    for d_name in d_set:
        warning += str(d_list.count(d_name))+u'个叫' + d_name + u'在场景中'+"\n"+"\n"
        #warning += str(d_list.count(d_name))+" objects named "+d_name +"in the scene!"+"\n"
    if warning:
        cmds.confirmDialog( title=u'重名检查', message=warning, button = u"确认")
    else:
        cmds.confirmDialog( title=u'重名检查', message="Scene is cleaned", button = u"确认")
def init_blendshape_check():
    bs_nodes =  cmds.ls(type = "blendShape")
    warning=""
    for bs in bs_nodes:
        bs_names = cmds.listAttr(bs, multi=1, string = "weight")
        for bs_name in bs_names:
            bs_weight = bs+"."+bs_name
            if cmds.getAttr(bs_weight):
                warning += bs_weight + u"为非零值"+"\n"
                #cmds.setKeyframe(bs+"."+bs_name, t=0)
    if warning:
        cmds.confirmDialog( title=u'blendshapeCheck', message=warning, button = u"确认")
    else:
        cmds.confirmDialog( title=u'blendshapeCheck', message=u"所有blendshape初始值为0", button = u"确认")
def bindpose_check():
    #TODO check bing pose
    pass
