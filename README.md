# Resume Upload Script for Updating Personal Website

I created this script to help automate the process of updating the resume I display on my own [website](https://www.raglandconnor.com).

The script converts the PDF resume to PNG, moves both to the project directory, and pushes changes to GitHub.

## Prerequisites

- [Python3](https://www.python.org/downloads/)
- [Homebrew](https://brew.sh/)
- MacOS

## How to use

1. Clone repository to local:

```bash
git clone https://github.com/raglandconnor/resume-upload-script.git
cd resume-upload-script
```

2. Create virtual environment:

```bash
# in project repository
python3 -m venv .venv
source .venv/bin/activate  # activate python virtual environment (macOS)
```

3. Install dependencies:

```bash
# in project repository
pip install -r requirements.txt  # or (pip install pdf2image Pillow)
```

```bash
# in terminal
brew install poppler
```

4. Edit script paths/filenames
5. Place PDF in source directory
6. Run the script:

```bash
# in project repository
python3 script.py
```
