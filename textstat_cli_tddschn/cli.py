#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2024-05-10
Purpose: TextStat CLI
"""

import argparse
import json
from pathlib import Path
import textstat
from tabulate import tabulate


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="TextStat (https://github.com/textstat/textstat) CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file", help="Input file", metavar="FILE", type=argparse.FileType("rt")
    )

    parser.add_argument(
        "-j", "--json", help="Output in JSON format", action="store_true"
    )

    parser.add_argument(
        "-T",
        "--no-tabulate",
        help="Do not output in tabulated format",
        action="store_true",
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    text_content = args.file.read()
    results = {
        "flesch_reading_ease": textstat.flesch_reading_ease(text_content),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text_content),
        "smog_index": textstat.smog_index(text_content),
        "coleman_liau_index": textstat.coleman_liau_index(text_content),
        "automated_readability_index": textstat.automated_readability_index(
            text_content
        ),
        "dale_chall_readability_score": textstat.dale_chall_readability_score(
            text_content
        ),
        "difficult_words": textstat.difficult_words(text_content),
        "linsear_write_formula": textstat.linsear_write_formula(text_content),
        "gunning_fog": textstat.gunning_fog(text_content),
        "text_standard": textstat.text_standard(text_content),
        "fernandez_huerta": textstat.fernandez_huerta(text_content),
        "szigriszt_pazos": textstat.szigriszt_pazos(text_content),
        "gutierrez_polini": textstat.gutierrez_polini(text_content),
        "crawford": textstat.crawford(text_content),
        "gulpease_index": textstat.gulpease_index(text_content),
        "osman": textstat.osman(text_content),
        "spache_readability": textstat.spache_readability(text_content),
        "mcalpine_eflaw": textstat.mcalpine_eflaw(text_content),
        "reading_time": textstat.reading_time(text_content),
        "syllable_count": textstat.syllable_count(text_content),
        "lexicon_count": textstat.lexicon_count(text_content),
        "sentence_count": textstat.sentence_count(text_content),
        "char_count": textstat.char_count(text_content),
        "letter_count": textstat.letter_count(text_content),
        # "polysyllable_count": textstat.polysyllablecount(text_content),
        # "monosyllable_count": textstat.monosyllable_count(text_content),
    }

    if args.json:
        print(json.dumps(results, indent=2))
    elif args.no_tabulate:
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print(tabulate(results.items(), headers=["Metric", "Value"]))
        print(
            f"\nExplanation of the metircs can be found at https://github.com/textstat/textstat\n\nPlease note that some of these metrics are not meant for English texts."
        )


if __name__ == "__main__":
    main()
