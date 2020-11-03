import subprocess

import sublime
import sublime_plugin

PIPE = subprocess.PIPE


class PythonFormat(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        file_name = view.file_name()
        if not file_name.endswith(".py"):
            return

        env = {"PYENV_VERSION": "3.7.8"}
        subprocess.Popen(
            ["/Users/dominik.schmid/.pyenv/shims/black", file_name],
            env=env,
            stderr=PIPE,
            stdout=PIPE,
        ).communicate()
        subprocess.Popen(
            ["/Users/dominik.schmid/.pyenv/shims/isort", file_name],
            env=env,
            stderr=PIPE,
            stdout=PIPE,
        ).communicate()
