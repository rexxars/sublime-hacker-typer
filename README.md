# sublime-hacker-typer

Pretend you're an expert hacker and can type flawlessly.
Inspired by http://hackertyper.com/

## Summary

Basically, the plugin (when enabled) looks for a file with the same name as the one you are editing, with an additional ".hackertyper"-extension.

When it finds this file, it treats it as the "solution" for the file. Whenever you type something, it will try to read the same number of characters from the solution file and replace whatever you typed.

## Why!?

Partly because it was fun. Partly because it can be useful when "live coding" something. Usually, when you're doing a talk and you're a little busy trying to make sense to your audience, you tend to do a lot of typos and silly mistakes. I still think it's a great way to engage the audience - but I'd rather skip all the mistakes ;-)

## Usage

1. Install the package through [Sublime Package Control](https://sublime.wbond.net/). Search for HackerTyper.
2. Enable the plugin through the command palette (Shift+Ctrl+P). "HackerTyper: Enable".
3. Create solution files alongside the files you want to pretend you're writing. So, to create an `index.html`-file based on a solution, create a `index.html.hackertyper`-file with the content you want to be typed out.
4. Open `index.html` and start writing.

Protip: You might want to include `"file_exclude_patterns": ["*.hackertyper"]` in your project settings or user preferences to prevent the solution files from showing up in the sidebar etc.


## Issues

  - It operates on length of the file instead of characters pressed. This means if you press enter and sublime would insert some tabs/spaces, it will add as many characters. This doesn't match up to your keypresses and seems weird. There does not seem to be a "key down" event in Sublime, however, which would have fixed this.
  
  - The only reliable way of seeing if content has been added/removed seems to be the "modified" event. Since we cannot edit in an eventlistener, we need to run a command. This command changes the content of the editor, which triggers a modified event, creating a recursion loop. It is eventually stopped because of a max recursion depth limit, but this is obviously unwanted behaviour. Not sure how to work around this.

## License

MIT-licensed. See LICENSE.
