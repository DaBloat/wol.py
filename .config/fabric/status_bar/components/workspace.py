from fabric.hyprland.widgets import Workspaces, WorkspaceButton

class WorkSpace(Workspaces):
    def __init__(self):
        super().__init__(
            name = 'workspaces',
            spacing = 5,
            buttons = [WorkspaceButton(id=wd+1, label=str(wd+1)) for wd in range(5)],
            buttons_factory = lambda wd: WorkspaceButton(id=wd, label=str(wd)) if wd != -99 else WorkspaceButton(id=wd, label="SECRET")
        )

