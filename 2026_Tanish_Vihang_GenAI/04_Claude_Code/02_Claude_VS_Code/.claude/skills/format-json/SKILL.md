---
name: format-json
description: Formats a non-formatted (minified or inconsistently indented) JSON file into a readable, pretty-printed layout. Use this whenever the user asks to "format json", "pretty-print json", "beautify json", "clean up this json", or points at a .json file that's hard to read, all on one line, or minified — even if they just paste a messy JSON blob or say something like "can you make this json readable".
---

# Format JSON

Pretty-prints a JSON file in place: 2-space indentation, consistent key order as given in
the source (no re-sorting), and a trailing newline.

## Steps

1. Identify the target JSON file from the user's message (ask for the path if not given
   or ambiguous).
2. Run the formatter script against it:

   ```
   python .claude/skills/format-json/scripts/format_json.py <path-to-file.json>
   ```

3. If the script reports invalid JSON, show the user the parse error (it includes line/column)
   instead of guessing at a fix.
4. On success, report the file path that was rewritten. Use `git diff <path>` to show the user
   what changed if they want to review before it's considered done.

## Notes

- The script overwrites the file in place — only run it on a file the user named, and make sure
  it's tracked by git (or the user is fine without a backup) since the rewrite isn't reversible
  outside of git.
- This is a demo skill: it only reformats whitespace/indentation, it does not sort keys, strip
  comments (JSON has none), or otherwise alter the data.
