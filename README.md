# Visualize your chrome browsing history

A tool to visualize your chrome browsing history with google takeout data.
![Chart Example](https://i.imgur.com/JFEZZAY.png)

## Getting Started

### 1. Initial setup

First follow [these instructions](https://gist.github.com/markmelnic/b5a6d399b2c08008c989829cbf9c3618) and make sure you satisfy all requirements.

### 2. Get Your Location Data

Here you can find out how to download your Google data: <https://support.google.com/accounts/answer/3024190?hl=en></br>
Here you can download all of the data that Google has stored on you: <https://takeout.google.com/>

To use this script, you only need to download your the data specified in the repository description, which Google will provide to you.

To use this script, you only need to download your "Chrome BrowserHistory", which Google will provide to you as a JSON file by default.

Make sure to put the file in the same directory with the script.

### 3. Run the Script

In the command prompt or Terminal window, type the following, and press enter:

```shell
python main.py <file>
```

Replace `<file>` with `BrowserHistory.json` file from Google Takeout (the file name might variate, so use the one suitable in your case).

### 4. Usage

`main.py <file> [-h] [-s SIZE] [-d DAYS]`

**positional arguments:**

  __file__                  Your JSON file downloaded from Google Takeout.

**optional arguments:**

  __-h__            Help option, prints the usage section in the console.

  __-s, --size__            Number of sites display *(20 by default)*
  
  __-d, --days__            Number of last X days to show data for *(60 by default)*

### 5. Examples

```shell
python main.py BrowserHistory.json
```

```shell
python main.py BrowserHistory.json -d 50
```

```shell
python main.py BrowserHistory.json --size 30
```

```shell
python main.py BrowserHistory.json -s 50 --days 90
```

### 6. Review the results and if you enjoyed the project, don't hesitate to leave a star. Thanks!
