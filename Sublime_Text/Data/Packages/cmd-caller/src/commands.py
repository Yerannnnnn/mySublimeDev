
import os.path
import subprocess
import shlex

import sublime
import sublime_plugin

from . import settings
from .support import log

# append text to view
class AppendTextCommand(sublime_plugin.TextCommand):
  def run(self, edit, text):
    log(self.__class__.__name__ + ':\n\t' + text)
    self.view.insert(edit, self.view.size(), text)

# execute one line of command
class CmdCaller(sublime_plugin.WindowCommand):

  # display output message
  def output(self, message):
    log(self.__class__.__name__ + '#output')
    message = '[CmdCaller] ' + message + '\n'
    panel = self.window.find_output_panel('cmd-caller')
    if not panel:
      panel = self.window.create_output_panel('cmd-caller')
    panel.run_command('append_text', {'text': message})
    self.window.run_command('show_panel', {'panel': 'output.cmd-caller'})

  # display error message with cmd string
  def error(self, message, cmd):
    log(self.__class__.__name__ + '#error')
    self.output(message + ':\n\t' + cmd)

  def get_settings(self, key, default = None):
    log(self.__class__.__name__ + '#get_settings')
    return settings.get(key, default)

  # run cmd
  def run_with_cmd(self, cmd):
    log(self.__class__.__name__ + '#run_with_cmd\n\t' + cmd)
    # cmd: [str] and [list of str]
    if isinstance(cmd, list):
      cmd = ' '.join(str(c) for c in cmd)
    elif not isinstance(cmd, str):
      self.error('Invalid argument: cmd should be a string or an array', cmd)
      return
    # replace variables
    disir = 'file file_name file_base_name file_extension file_path folder project_base_name'.split()
    dvars = self.window.extract_variables()
    nvars = {}
    for key in disir:
      nvars[key] = dvars.get(key, '')
    cmd = sublime.expand_variables(cmd, nvars)
    # exec
    try:
      if sublime.platform() == "windows":
        subprocess.Popen(cmd)
      else:
        subprocess.Popen(shlex.split(cmd))
    except FileNotFoundError:
      self.error('Cannot execute command', cmd)

  # run with app key
  def run_with_key(self, key):
    log(self.__class__.__name__ + '#run_with_key\n\t' + key)
    cmd = self.get_settings('apps')[key]['cmd']
    self.run_with_cmd(cmd)


# run default command
class CmdCallerDefaultCommand(CmdCaller):
  def run(self):
    log(self.__class__.__name__)
    dft = self.get_settings('default')
    super().run_with_key(dft)


# open a panel and run selected command
class CmdCallerListCommand(CmdCaller):
  def run(self):
    log(self.__class__.__name__)
    apps = self.get_settings('apps')
    self.keys = list(apps.keys())
    items = list(apps[key]['name'] if 'name' in apps[key] else key for key in self.keys)
    self.window.show_quick_panel(items, self.on_select)

  def on_select(self, idx):
    log(self.__class__.__name__ + '#on_select\n\t' + str(idx))
    if idx < 0:
      return
    super().run_with_key(self.keys[idx])
