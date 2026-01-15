# urban_stories (placeholder)

A modular Ren'Py visual novel project built with scalability and maintainability in mind.

## Overview

urban_stories is a visual novel game developed using the Ren'Py engine. This project follows a strict **Separation of Concerns** architecture to ensure clean, maintainable code that can scale to 50+ hours of gameplay without becoming unwieldy.

## Features

- **Modular Architecture**: Scripts organized by purpose (definitions, state, flow, routes)
- **State Management**: Python-based state tracking for complex game logic
- **Branching Narratives**: Multiple character routes and decision trees
- **Clean Code Standards**: Enforced naming conventions and file organization

## Requirements

- Ren'Py 8.0+ (or latest stable version)
- Python 3.x (bundled with Ren'Py)

## Getting Started

1. Install Ren'Py from [renpy.org](https://www.renpy.org/)
2. Clone this repository
3. Open the project folder in the Ren'Py Launcher
4. Click "Launch Project" to start the game

## Project Structure

```
urban_stories/
├── game/                          # Main game directory
│   ├── script.rpy                 # Entry point - start label and flow control only
│   ├── options.rpy                # Game configuration and build options
│   ├── gui.rpy                    # GUI customization
│   ├── screens.rpy                # UI screens (main menu, preferences, etc.)
│   │
│   ├── scripts/                   # Modular story scripts (Separation of Concerns)
│   │   ├── 00_definitions.rpy     # Static definitions (Characters, Transforms, Audio)
│   │   ├── 01_state.rpy           # Variables, Classes, Save-state logic
│   │   ├── flow_[name].rpy        # Common route events (e.g., flow_prologue.rpy)
│   │   └── route_[name].rpy       # Character-specific routes (e.g., route_bad_reputation.rpy)
│   │
│   ├── images/                    # Visual assets
│   │   ├── bg/                    # Background images
│   │   └── sprites/               # Character sprites and expressions
│   │
│   ├── audio/                     # Sound assets
│   │   ├── bgm/                   # Background music
│   │   └── sfx/                   # Sound effects
│   │
│   ├── gui/                       # GUI elements and assets
│   ├── tl/                        # Translations
│   │   └── None/                  # Default language files
│   │
│   ├── saves/                     # Save game data
│   └── cache/                     # Compiled bytecode cache
│
├── README.md                      # This file
└── log.txt                        # Ren'Py runtime log
```

## Architecture Principles

### 1. Separation of Concerns

Each file has a specific purpose:

- **`00_definitions.rpy`**: Immutable definitions using `define` keyword
  - Character objects
  - Transform animations
  - Audio channel declarations

- **`01_state.rpy`**: Mutable state using `default` keyword
  - Game variables (relationship points, flags)
  - Python classes for complex state management
  - Inventory systems

- **`flow_*.rpy`**: Common narrative sequences
  - Events that happen regardless of route
  - Prologue, common chapters, epilogue

- **`route_*.rpy`**: Route-specific content
  - Character-specific storylines
  - Branch-exclusive scenes

- **`script.rpy`**: Traffic direction only
  - `start` label
  - High-level flow control via `jump` and `call`
  - NO narrative dialogue or scene descriptions

### 2. Label Naming Convention

All labels follow the namespaced format: `[route_id]_[chapter]_[event_name]`

**Examples:**
- ✅ `route_scifi_ch01_docking_bay`
- ✅ `flow_prologue_ch00_opening`
- ❌ `dinner` (too generic, will cause conflicts)

### 3. State Management

**DO:**
- Use `default` for all mutable variables in `01_state.rpy`
- Use Python classes for complex state tracking
- Initialize objects like `default player = PlayerState()`

**DON'T:**
- Never use `$ variable = value` to initialize variables inside labels
- This breaks save file compatibility

### 4. Decision Trees

Use a **State-Based Hub** architecture:
1. Track decisions with flags (`scifi_points`, `karma`, etc.)
2. Lock routes when confirmed (`route_locked = "scifi"`)
3. Jump to dedicated labels in separate files for major branches

## Development Guidelines

### Adding a New Route

1. Create `scripts/route_[name].rpy`
2. Add character definition to `scripts/00_definitions.rpy`
3. Add route variables to `scripts/01_state.rpy`
4. Use namespaced labels: `route_[name]_ch[##]_[event]`
5. Update `script.rpy` to include route entry points

### Adding a New Character

In `scripts/00_definitions.rpy`:
```renpy
define s = Character("Sarah", color="#c8ffc8")
```

### Adding State Variables

In `scripts/01_state.rpy`:
```renpy
default sarah_relationship = 0
default met_sarah = False
```

### Creating a Scene

In appropriate `flow_*.rpy` or `route_*.rpy` file:
```renpy
label flow_common_ch1_meet_sarah:
    scene bg park_sunset
    show s neutral at center
    
    s "Hello there."
    
    menu:
        "Greet her warmly":
            $ sarah_relationship += 1
            s "You're kind."
        
        "Ignore her":
            $ sarah_relationship -= 1
            s "How rude."
    
    return
```

## Contributing

When contributing to this project:

1. Follow the established file structure
2. Use proper label namespacing
3. Never initialize variables with `=` inside labels
4. Keep `script.rpy` minimal (flow control only)
5. Document major decisions in comments

## License

[TBD]

## Credits

Developed with Ren'Py Visual Novel Engine
[TBD]
