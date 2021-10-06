import i3
# get a list of workspaces
for workspace in i3.get_workspaces():
    # get the workspace tree data
    workspace_tree = i3.filter(num=workspace.get('num'))
    # get a list of existing leaf windows in that workspace
    for window in i3.filter(workspace_tree, nodes=[]):
        # do something useful here
        print ('workspace %d' % workspace.get('num'), 'window:', window.get('name'))
