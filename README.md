![Repo Size](https://img.shields.io/github/repo-size/eifal/Auto-Pixiv)

## Pixiv Downloader

![Pixiv](https://raw.githubusercontent.com/Eifal/Auto-Pixiv/main/pix/illust_id_119695250_プロセカツイログ⑨.jpg)

## Overview

This project provides a script and API to download illustrations from Pixiv using the powerful [pixivpy](https://github.com/upbit/pixivpy) library.

## Features

- **Automated Downloads**: Schedule and automate the download of recommended illustrations from Pixiv.
- **Customizable**: Easily configure which illustrations to download and how they are saved.
- **Extensible**: Built on top of `pixivpy`, allowing for further customization and extension.

## Installation

Clone the repository and install the required dependencies:

```sh
git clone https://github.com/Eifal/Auto-Pixiv.git
cd Auto-Pixiv
pip install -r requirements.txt
```

## Usage

**Scheduled Downloads**

This project uses GitHub Actions to schedule downloads. By default, it runs every hour.

## Running Locally

To run the script locally, simply execute:

```sh
python pixiv.py
```

## Configuration

Update the _REFRESH_TOKEN in pixiv.py with your Pixiv refresh token to authenticate API requests.
To get refresh_token
[@ZipFile Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362)
> or
> [OAuth with Selenium/ChromeDriver](https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)

```sh
_REFRESH_TOKEN = "your_refresh_token_here"
```
