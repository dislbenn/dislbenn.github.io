# Building Web-Crawler
Building a Web-Crawler Software is easy, and helps you take advantage of a data mining software. This document will help guide you through understanding this build process.

## Requirements

1. BeautifulSoup4, module is needed and can be installed with pip install BeautifulSoup4.
2. re, module is needed and can be installed with pip install re.
3. logging, module is needed and can be installed with pip install logging.

2. Web-Crawler, using one of the following configurations:
* **macOS** You can either use Web-Crawler for Mac or  See installation instructions.
* **Linux**  Install Web-Crawler according to the [instructions] for your OS.

## Overview

While it is possible to build a web-crawler using a local python installation, we have a build process that runs on a local environment.  This simplifies initial set up and provides for a very consistent build and test environment.

## Key scripts

The following scripts are found in the `build/` directory. Note that all scripts must be run from the Web-Crawler root directory.
1. `src/project/build/log_clean.sh`
2. `src/project/build/move_csv.sh`

## Basic Flow

The scripts directly under build/ are used to build and test. They will ensure that the web-crawler is built and then executed appropriatly command. These scripts will both ensure that the right data is stored from run to run for incremental builds and will copy the results back out of the database or csv.

## Proxy Settings


## Releasing

The build/release.sh script will build a release. It will build binaries, run tests, (optionally) build SQL Database.

## Reproducibility

