# Clear JSON (.cjson)

A minimalist, human-readable data serialization format designed to eliminate the "quote-heavy" syntax of standard JSON.

## Why .cjson?
- **No more quotes:** Clean, aesthetic syntax for configuration files.
- **Human-friendly:** Easy to write, read, and maintain by hand.
- **Robust:** Strict rules to prevent ambiguity while maintaining simplicity.

## Quick Syntax
{
  name: Alex Sander,
  gender: male,
  age: 33,
  skills: {
    progam: Javascript,
    football: dribbling
  },
  interest: [
    football, game
  ]
}

## Installation
**Python:** pip install cjson
