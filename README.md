# textstat-cli-tddschn

- [textstat-cli-tddschn](#textstat-cli-tddschn)
  - [Motivation](#motivation)
  - [Demo](#demo)
  - [Features](#features)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
  - [Develop](#develop)


## Motivation

Get quick and easy readability and other metrics for your texts right on the command line with [`textstat`](https://github.com/textstat/textstat), offering more insights than `wc` and LLM token count.

There's another project on PyPI `textstat-cli` made by another person, I tried that one before making this. Sadly that one doesn't run on my machine, so I made this one.

## Demo

```plain
# Using the tool on my latest blog post at https://teddysc.me/blog/raleigh-menswear-stores-review

$ textstat-cli teddysc.me/data/blog/raleigh-menswear-stores-review.mdx

Metric                        Value
----------------------------  ------------------
flesch_reading_ease           67.65
flesch_kincaid_grade          6.8
smog_index                    8.7
coleman_liau_index            13.38
automated_readability_index   13.7
dale_chall_readability_score  8.12
difficult_words               111
linsear_write_formula         4.7272727272727275
gunning_fog                   6.1
text_standard                 8th and 9th grade
fernandez_huerta              104.5
szigriszt_pazos               102.97
gutierrez_polini              38.19
crawford                      2.1
gulpease_index                52.1
osman                         35.41
spache_readability            3.66
mcalpine_eflaw                16.4
reading_time                  77.86
syllable_count                1264
lexicon_count                 858
sentence_count                71
char_count                    5300
letter_count                  4669

Explanation of the metircs can be found at https://github.com/textstat/textstat

Please note that some of these metrics are not meant for English texts.
```

## Features

- Lots of metrics, see demo above.
- 3 output formats, table by tabulate (see demo), plain text, or JSON.

## Installation

Requires Python>=3.10, <3.12 (`textstat` requires pkg_resources, which is not available in Python 3.12).

### pipx

This is the recommended installation method.

```
$ pipx install textstat-cli-tddschn
```

### [pip](https://pypi.org/project/textstat-cli-tddschn/)

```
$ pip install textstat-cli-tddschn
```

## Usage

```plain
$ textstat-cli --help

usage: textstat-cli [-h] [-j] [-T] FILE

TextStat (https://github.com/textstat/textstat) CLI

positional arguments:
  FILE               Input file

options:
  -h, --help         show this help message and exit
  -j, --json         Output in JSON format (default: False)
  -T, --no-tabulate  Do not output in tabulated format (default: False)
```

## Develop

```
$ git clone https://github.com/tddschn/textstat-cli-tddschn.git
$ cd textstat-cli-tddschn
$ poetry install
```