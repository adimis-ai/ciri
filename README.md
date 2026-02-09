# CIRI Copilot

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![uv](https://img.shields.io/badge/built%20with-uv-blueviolet)](https://docs.astral.sh/uv/)

**CIRI (Contextual Intelligent Runtime Interface) Copilot** is a desktop-class personal AI copilot intended to be run locally. This CLI provides tools for managing and interacting with the Ciri AI agent system.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
  - [Windows](#windows-prerequisites)
  - [macOS](#macos-prerequisites)
  - [Linux](#linux-prerequisites)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Install CIRI](#install-ciri)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands Reference](#commands-reference)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Interactive AI Chat**: Real-time streaming conversations with AI models
- **File & Skills Autocomplete**: Use `@` for file paths and `@skills:` for skills
- **Thread Management**: Save, switch, and manage conversation threads
- **Model Selection**: Choose from available OpenRouter models
- **Human-in-the-Loop**: Approve, reject, or edit tool executions
- **Secure Storage**: Encrypted local database for conversations

---

## Prerequisites

Before installing CIRI, you need to set up your development environment. Follow the instructions for your operating system below.

### Windows Prerequisites

<details>
<summary><strong>Click to expand Windows setup guide</strong></summary>

#### 1. Install Git

1. Download Git from [git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the downloaded installer (`.exe` file)
3. Follow the setup wizard, keeping the default options
4. **Important**: Ensure "Add Git to PATH" is selected during installation
5. Verify installation by opening **Command Prompt** or **PowerShell** and running:
   ```powershell
   git --version
   ```
   You should see something like: `git version 2.x.x.windows.x`

#### 2. Install Python 3.12+

1. Download Python from [python.org/downloads](https://www.python.org/downloads/)
2. Run the downloaded installer
3. **Critical**: Check ✅ "Add Python to PATH" at the bottom of the installer
4. Click "Install Now"
5. Verify installation:
   ```powershell
   python --version
   ```
   You should see: `Python 3.12.x` or higher

#### 3. Install uv (Python Package Manager)

1. Open **PowerShell** (search "PowerShell" in Start menu)
2. Run the following command:
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3. Close and reopen PowerShell
4. Verify installation:
   ```powershell
   uv --version
   ```

</details>

---

### macOS Prerequisites

<details>
<summary><strong>Click to expand macOS setup guide</strong></summary>

#### 1. Install Homebrew (Package Manager)

If you don't have Homebrew installed, open **Terminal** (Applications → Utilities → Terminal) and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions. After installation, run the commands shown to add Homebrew to your PATH.

#### 2. Install Git

Git may already be installed on macOS. Check by running:

```bash
git --version
```

If not installed, you'll be prompted to install Xcode Command Line Tools. Click "Install" to proceed.

Alternatively, install via Homebrew:

```bash
brew install git
```

#### 3. Install Python 3.12+

Install Python using Homebrew:

```bash
brew install python@3.12
```

Verify installation:

```bash
python3.12 --version
```

#### 4. Install uv (Python Package Manager)

Run the following command in Terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen Terminal, then verify:

```bash
uv --version
```

</details>

---

### Linux Prerequisites

<details>
<summary><strong>Click to expand Linux setup guide (Ubuntu/Debian)</strong></summary>

#### 1. Update System Packages

Open a terminal and run:

```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Git

```bash
sudo apt install git -y
```

Verify:

```bash
git --version
```

#### 3. Install Python 3.12+

For Ubuntu 22.04 and newer, Python 3.12 may not be in the default repositories. Add the deadsnakes PPA:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y
```

Verify:

```bash
python3.12 --version
```

#### 4. Install uv (Python Package Manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal, then verify:

```bash
uv --version
```

**Note**: If you're using a different distribution (Fedora, Arch, etc.), use your native package manager (`dnf`, `pacman`) to install Git and Python.

</details>

---

## Installation

### Clone the Repository

First, clone the CIRI repository to your local machine.

**Using SSH** (recommended if you have SSH keys set up with GitHub):

```bash
git clone git@github.com:adimis-ai/ciri.git
cd ciri
```

**Using HTTPS** (easier for beginners):

```bash
git clone https://github.com/adimis-ai/ciri.git
cd ciri
```

> **💡 Tip**: If you don't have SSH keys set up, use the HTTPS method. To set up SSH keys, see [GitHub's SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### Install CIRI

#### Option 1: Global Installation (Recommended for Regular Use)

This makes `ciri` accessible from any terminal window:

```bash
uv tool install .
```

This installs `ciri` in an isolated environment and adds it to your PATH (typically `~/.local/bin`).

**Verify installation:**

```bash
ciri --help
```

#### Option 2: Local Development Installation

For development or testing changes:

```bash
# Create and activate virtual environment
uv sync

# Install in editable mode
uv pip install -e .
```

---

## Configuration

### OpenRouter API Key

CIRI uses OpenRouter to access various AI models. You'll need an API key:

1. **Get an API Key**:
   - Visit [openrouter.ai](https://openrouter.ai/)
   - Create an account or sign in
   - Go to your dashboard and generate an API key

2. **Set Up the API Key**:

   When you first run `ciri`, you'll be prompted to enter your API key. It will be saved automatically for future sessions.

   Alternatively, set it manually:

   **Option A: Environment Variable**

   ```bash
   # Linux/macOS
   export OPENROUTER_API_KEY="your-api-key-here"
   
   # Windows PowerShell
   $env:OPENROUTER_API_KEY="your-api-key-here"
   ```

   **Option B: Create a `.env` file** in the CIRI directory:

   ```bash
   echo 'OPENROUTER_API_KEY=your-api-key-here' > .env
   ```

> ⚠️ **Security Warning**: Never commit your API key to version control. The `.env` file is already in `.gitignore`.

---

## Usage

### Starting CIRI

Simply run:

```bash
ciri
```

On first launch:
1. You'll be prompted for your OpenRouter API key (if not set)
2. You'll choose an AI model (Tab for autocomplete options)
3. The interactive chat will start

### Interactive Features

| Feature | How to Use |
|---------|-----------|
| **File Autocomplete** | Type `@` followed by a path to autocomplete files |
| **Skills Autocomplete** | Type `@skills:` to autocomplete available skills |
| **Exit Chat** | Type `exit`, `quit`, or `bye` |

### Example Session

```
You> Hello, analyze the @src/__main__.py file
CIRI: [Analyzes and responds about the file...]

You> /threads
# Shows all conversation threads

You> exit
Goodbye!
```

---

## Commands Reference

### Chat Commands

| Command | Description |
|---------|-------------|
| `/threads` | List all conversation threads and optionally switch |
| `/new-thread` | Create a new conversation thread |
| `/delete-thread` | Delete the current thread |
| `/model [name]` | Switch to a different AI model |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Autocomplete file paths or model names |
| `Ctrl+C` | Cancel current operation |

---

## Troubleshooting

### Common Issues

<details>
<summary><strong>Command 'ciri' not found</strong></summary>

**Cause**: The uv tools bin directory is not in your PATH.

**Solution**:

**Linux/macOS**: Add to your shell config (`~/.bashrc`, `~/.zshrc`):
```bash
export PATH="$HOME/.local/bin:$PATH"
```
Then restart your terminal.

**Windows**: The installer should add it automatically. If not, add `%USERPROFILE%\.local\bin` to your PATH in System Environment Variables.

</details>

<details>
<summary><strong>Python version error</strong></summary>

**Cause**: You have an older Python version installed.

**Solution**: Ensure Python 3.12+ is installed and in your PATH:
```bash
python3.12 --version  # Linux/macOS
python --version      # Windows
```

If you have multiple Python versions, uv will automatically use the correct one.

</details>

<details>
<summary><strong>API Key errors</strong></summary>

**Cause**: Invalid or missing OpenRouter API key.

**Solution**:
1. Verify your API key at [openrouter.ai/keys](https://openrouter.ai/keys)
2. Delete the saved key and re-enter:
   - Delete `~/.ciri/.env` (if it exists)
   - Run `ciri` again and enter a valid key

</details>

<details>
<summary><strong>Permission denied errors</strong></summary>

**Cause**: CIRI cannot write to its data directory.

**Solution**:
- Ensure you own `~/.ciri` directory
- On Linux: `sudo chown -R $USER:$USER ~/.ciri`

</details>

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get started.

---

## License

Distributed under the MIT License. See [LICENSE.md](LICENSE.md) for the full text.

---

## Contact

**Aditya Mishra** - [@adimis-ai](https://github.com/adimis-ai)

Project Link: [https://github.com/adimis-ai/ciri](https://github.com/adimis-ai/ciri)

---

<div align="center">

**Built by [Aditya Mishra](https://github.com/adimis-ai)**

</div>
