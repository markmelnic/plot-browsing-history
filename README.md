
# Visualize Your Chrome Browsing History

A lightweight tool to visualize your Chrome browsing history using Google Takeout data.

![Chart Example](https://i.imgur.com/sJCc9gq.png)

---

## Getting Started

Follow these steps to visualize your browsing history:

### 1. Initial Setup

Ensure you meet all requirements by following [this guide](https://gist.github.com/markmelnic/b5a6d399b2c08008c989829cbf9c3618).

### 2. Download Your Browsing Data

1. Learn how to download your Google data: [Google Takeout Guide](https://support.google.com/accounts/answer/3024190?hl=en).  
2. Download your data from [Google Takeout](https://takeout.google.com/).

> **Note:** You only need to download your Chrome browsing history. Google provides it as a JSON file by default.

Save the `History.json` file in the same directory as the script.

### 3. Run the Script

Open your terminal or command prompt and execute the following command:

```shell
python main.py <file>
```

Replace `<file>` with the name of your downloaded `History.json` file (the name may vary).

---

## Script Usage

### Command Syntax

```shell
main.py <file> [-h] [-s SIZE] [-d DAYS]
```

#### Positional Arguments:
- **`<file>`**: The JSON file downloaded from Google Takeout.

#### Optional Arguments:
- **`-h`**: Display help information.
- **`-s, --size`**: Number of top sites to display (default: 20).
- **`-d, --days`**: Number of recent days to analyze (default: 60).

---

## Examples

1. Basic usage with default settings:
   ```shell
   python main.py History.json
   ```

2. Display data from the last 50 days:
   ```shell
   python main.py History.json -d 50
   ```

3. Show the top 30 sites:
   ```shell
   python main.py History.json --size 30
   ```

4. Analyze 90 days and display the top 50 sites:
   ```shell
   python main.py History.json -s 50 --days 90
   ```
