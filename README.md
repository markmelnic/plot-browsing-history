# Visualize your chrome browsing history

A tool to visualize your chrome browsing history with google takeout data.

![Imgur](https://i.imgur.com/3u9ZdSG.png)

## Getting Started

### 1. Initial setup

First follow [these instructions](https://github.com/Google-Takeout/Setup-Instructions) and make sure you satisfy all requirements.

### 2. Get Your Location Data

To use this script, you only need to download your "Chrome BrowserHistory", which Google will provide to you as a JSON file by default.

Make sure to put the file in the same directory with the script.

### 3. Run the Script

In the command prompt or Terminal window, type the following, and press enter:

```shell
python main.py <file> <size>
```

Replace the string `<file>` from above with the `BrowserHistory.json` JSON file from Google Takeout.

The integer `<size>` is a positional and optional argument which defines the number of links *(order descending by number of visits)* to be displayed. *(20 by default)*

#### Example:

```shell
python main.py BrowserHistory.json
```

```shell
python main.py BrowserHistory.json 50
```

### 4. Review the results and enjoy, I guess :D
