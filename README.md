# Alipin Lyrics

A tiny Python script that "plays" the lyrics of **"Alipin"** in your terminal with a typewriter effect. Each line is typed out character by character, with a configurable pause between lines, so the text appears in time with the song.

No dependencies, no audio playback — just Python printing to standard output.

## Features

- Typewriter-style output using `sys.stdout.write` and `time.sleep`
- Per-line and per-character timing
- Plain Python with no third-party packages
- Lyrics and timings are stored in a simple list, so they are easy to edit

## Requirements

- Python 3.6 or newer
- A terminal that supports standard output (any OS)

## Getting Started

Clone the repository and run the script:

```bash
git clone https://github.com/miggy158/Python--alipin-lyrics-.git
cd Python--alipin-lyrics-
python main.py
```

On Windows you can also use the Python launcher:

```powershell
py main.py
```

On systems where Python 3 is installed as `python3`:

```bash
python3 main.py
```

The output starts with:

```text
Now playing: Alipin
```

followed by the lyrics typed out one character at a time. Press `Ctrl+C` to stop playback early.

## How It Works

`main.py` is organized into three small parts:

| Name | Purpose |
| --- | --- |
| `lyrics` | List of `(line, line_delay, char_delay)` tuples containing the song text and its timings. |
| `type_out(text, char_delay=0.1)` | Writes `text` one character at a time, flushing after each character so it appears immediately, then prints a newline. |
| `play_lyrics(lyrics)` | Loops over the lyrics, calls `type_out` for each line, and waits `line_delay` seconds before moving to the next line. |

The script runs `play_lyrics(lyrics)` when executed as the main module:

```python
if __name__ == "__main__":
    print("Now playing: Alipin\n")
    print("\n\n")
    play_lyrics(lyrics)
```

## Customizing the Lyrics and Timing

Each entry in the `lyrics` list follows this format:

```python
("Line of the song", line_delay, char_delay)
```

- **`line`** — the text to type out.
- **`line_delay`** — seconds to wait after the line finishes, before the next line starts. Use this to match pauses in the song.
- **`char_delay`** — seconds to wait between each character of the line. Larger values type more slowly.

For example, to slow down a single line:

```python
("Ako'y alipin mo kahit hindi batid", 1.60, 0.20),
```

To change the default typing speed for every line that does not specify its own value, edit the default in the function signature:

```python
def type_out(text, char_delay=0.1):
```

You can replace the contents of `lyrics` with any text you like — the script is not tied to this song.

## Project Structure

```text
Python--alipin-lyrics-/
├── main.py      # Lyrics data, typewriter output, and playback loop
└── README.md    # This documentation
```

## Notes and Limitations

- Timings are tuned by hand and are approximate; they may drift from the actual song depending on your terminal and machine.
- The entire song is typed to standard output, so terminal scrollback will contain the full lyrics after playback.
- `printlyrics()` is currently unused and can be ignored or removed if you are cleaning up the script.

## Contributing

Issues and pull requests are welcome. If you adjust the timings for better sync with the song, feel free to share them.

## License

This repository does not currently include a license file. Contact the repository owner before reusing the code or lyrics.
