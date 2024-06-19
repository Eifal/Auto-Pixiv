![GitHub repo size](https://img.shields.io/github/repo-size/Eifal/Auto-Pixiv?style=for-the-badge&logo=Github&labelColor=%234169e1&color=%23191970)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/eifal/Auto-Pixiv?style=for-the-badge&logo=Github&labelColor=4169e1&color=191970)

## Overview

This project provides a script and API to download illustrations from Pixiv using the powerful [pixivpy](https://github.com/upbit/pixivpy) library.

## Features

- **Automated Downloads**: Schedule and automate the download of recommended illustrations from Pixiv.
- **Customizable**: Easily configure which illustrations to download and how they are saved.
- **Extensible**: Built on top of `pixivpy`, allowing for further customization and extension.

## Installation and Running Locally

```sh
# git clone
git clone https://github.com/Eifal/Auto-Pixiv.git -b unm
pip install pixivpy3 --upgrade

# execute 
python pixiv.py
```

## Configuration

Update the _REFRESH_TOKEN in pixiv.py with your Pixiv refresh token to authenticate API requests.

>To get `refresh_token`, see
>[@ZipFile Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362)
> or
> [OAuth with Selenium/ChromeDriver](https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)

```sh
_REFRESH_TOKEN = "your_refresh_token_here"
```

## Scheduled Downloads

This project uses GitHub Actions to schedule downloads. By default, it runs every hour.
