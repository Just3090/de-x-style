# de-x-style

This Python script recursively renames files and directories by removing a specified prefix (by default, `x-`) from their names.

## Features
- Removes the prefix from all files and directories within the given root directory.
- Renames files first, then directories (from the deepest level up) to avoid conflicts.
- Prints each rename operation to the console for tracking.

## Usage

1. Place the script in the root directory where you want to remove the prefix.
2. By default, it removes the prefix `x-` from all files and directories.
3. Run the script:

```bash
python de-x-style.py
```

## Customization

- To use a different prefix, modify the `prefix` argument in the `rename_in_tree` function call at the end of the script.

## Example

Suppose your directory contains:
```
x-folder/
  x-file.txt
  x-subfolder/
    x-anotherfile.txt
```
After running the script, it will become:
```
folder/
  file.txt
  subfolder/
    anotherfile.txt
```

## Requirements
- Python 3.x

## License
MIT License
