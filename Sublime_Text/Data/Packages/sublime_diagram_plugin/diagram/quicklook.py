from .base import BaseViewer
from subprocess import check_call, Popen as run_command
from sublime import platform

class QuickLookViewer(BaseViewer):
    def load(self):
        if platform() not in ('osx',):
            raise Exception("Currently only supported on MacOS")
        if not check_call("which qlmanage > /dev/null", shell=True) == 0:
            raise Exception("Can't find qlmanage")

    def view(self, diagram_files):
        displaycmd = ['qlmanage', '-p']
        displaycmd.extend(diagram_file.name for diagram_file in diagram_files)
        run_command(displaycmd).wait()
