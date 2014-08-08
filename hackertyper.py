import os.path
import sublime, sublime_plugin

hacker_enabled = False

class HackerTyperCommand(sublime_plugin.TextCommand):
    def run(self, edit, enable=False, content=False):
        global hacker_enabled
        hacker_enabled = enable

        if content is False:
            return

        # Replace contents
        self.view.replace(edit, sublime.Region(0, len(content)), content)


class HackerTyper(sublime_plugin.EventListener):
    solution_exists = False
    hacker_buffer = ""

    def on_activated(self, view):
        # Don't check for solution files if the plugin is disabled
        if hacker_enabled is False:
            return

        # Check if the current file has a solution
        filename = view.file_name()
        if filename is None:
            return

        solution = filename + ".hackertyper"
        self.solution_exists = os.path.isfile(solution)

        # Give a feedback message if no solution was found
        # Clear the status bar if one was found
        if not self.solution_exists:
            err = "HackerTyper Error: " + os.path.basename(filename)
            err += ".hackertyper not found"
            return sublime.status_message(err)
        else:
            sublime.status_message("")

        # Read the entire solution text
        self.hacker_buffer = open(solution).read()

    def on_modified_async(self, view):
        global hacker_enabled

        if hacker_enabled is False or self.solution_exists is False:
            return

        # Fetch correct part of the buffer
        bufSize = view.size()

        # Fall back if we're outrunning the original solution
        if bufSize > len(self.hacker_buffer):
            return

        newBuf  = self.hacker_buffer[:bufSize]

        view.run_command("hacker_typer", { "enable": True, "content": newBuf });
