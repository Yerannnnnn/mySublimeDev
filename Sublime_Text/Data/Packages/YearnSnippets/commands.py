import sublime
import sublime_plugin
import plistlib
import uuid
import zlib
from datetime import datetime



def update_snippets_consts():
    settings = sublime.load_settings('YearnSnippets.sublime-settings')
    copyright_yera = datetime.utcnow().strftime("%Y")
    author = settings.get("author")
    email = settings.get("email")
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    preferences = dict(
        scope = '',
        name = 'Globals',
        uuid = str(uuid.uuid1()),
        settings = dict(
            shellVariables = [
                dict (name = 'TM_COPYRIGHT_YERAN',value = copyright_yera),
                dict (name = 'TM_AUTHOR',value = author),
                dict (name = 'TM_EMAIL',value = email),
                dict (name = 'TM_TIMESTAMP',value = timestamp),
            ]
        )
    )
    path= sublime.packages_path().replace('\\','/')+'/User/YearnSnippets.tmPreferences'
    plistlib.writePlist(preferences,path)

def plugin_loaded():
    update_snippets_consts()
