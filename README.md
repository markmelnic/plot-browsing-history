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
python main.py <file> <type>
```

Replace the string `<file>` from above with the `BrowserHistory.json` JSON file from Google Takeout.

Replace `<type>` with either `chart` to display the most visited sites chart or `hist` to see an activity histogram.

### Usage:

**usage:** main.py [-h] [-s SIZE] [-d DAYS] file type

<br>

**positional arguments:**

  __file__                  Your browsing history JSON file from Google Takeout.

  __type__                  Option to display either most visited sites chart or an activity histogram. Values: `chart` for chart and `hist` for histogram.

<br>

**optional arguments:**

  __-s, --size__            Number of sites display *(20 by default)*
  
  __-d, --days__            Number of last X days to show data for *(365 by default)*

### Examples:

```shell
python main.py BrowserHistory.json chart
```

```shell
python main.py BrowserHistory.json chart -s=50
```

```shell
python main.py BrowserHistory.json chart -s=50 --days=90
```

### 4. Review the results and if you enjoyed the project, don't hesitate to leave a star. Thanks!
