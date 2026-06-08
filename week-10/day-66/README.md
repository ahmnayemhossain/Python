# Day 66 - Pomodoro Timer GUI

## What I Learned

- How Tkinter handles events
- How state controls timer flow
- How `after()` updates a timer over time

## Features

- Starts a work timer
- Switches between work and break mode
- Resets the timer and state cleanly

## How to Run

```bash
python main.py
```

## Example Output

```text
Opens a Pomodoro timer GUI with start and reset controls.
```

## Mistakes I Fixed

- Stored timer state inside a class
- Cancelled scheduled updates when resetting

## Future Improvement

- Add sound notifications
