# wikit

This is a [wikit](https://github.com/KorySchneider/wikit) clone (or at least most features cloned) for python because I don't like node and don't want to install it, but the wikit tool seemed neat

A command line program for getting Wikipedia summaries easily.

 - [Installation](#installation)
 - [Usage](#usage)
   - [Examples](#examples)
   - [Flags](#flags)
   - [Output](#output)

## Installation

`$ pip install wikit`

## Usage

Syntax: `$ wikit <query> [-flags]`

Quotes are not required for multi-word queries.

### Examples

`$ wikit wikipedia`

`$ wikit empire state building`

`$ wikit linux -b`

`$ wikit jugo -l es --link -a`

### Flags

| Flag | Description |
| ---- | ----------- |
| `--lang langCode`<br>`-l langCode` | Specify language; `langCode` is an [HTML ISO language code](https://www.w3schools.com/tags/ref_language_codes.asp) |
| `--all`<br>`-a` | Print all sections of the article (the full page).  Recommended to pipe into a reader e.g. `less` |
| `--link` | Print a link to the full article after the summary |
| `-b` | Open full Wikipedia article in default browser |
| `--browser browser` | Open full Wikipedia article in specific `browser` |
| `-d` | Open disambiguation page |

### Output

The output will be the paragraphs of the wikipedia article before the table of contents.
Line length is neatly wrapped based on your terminal's window size, with a max
of about 80 characters. For example:

```
$ wikit arch linux
 Arch Linux (or Arch /ˈɑːrtʃ/) is a Linux distribution for computers based on x86-64
 architectures. Arch Linux is composed predominantly of free and open-source software,
 and supports community involvement. The design approach of the development team
 follows the KISS principle ("keep it simple, stupid") as the general guideline,
 and focuses on elegance, code correctness, minimalism and simplicity, and expects
 the user to be willing to make some effort to understand the system's operation.
 A package manager written specifically for Arch Linux, pacman, is used to install,
 remove and update software packages. Arch Linux uses a rolling release model, such
 that a regular system update is all that is needed to obtain the latest Arch software;
 the installation images released by the Arch team are simply up-to-date snapshots
 of the main system components. Arch Linux has comprehensive documentation in the
 form of a community wiki, called the ArchWiki. The wiki is widely regarded among
 the Linux community and ecosystem for often having the most recent information on
 a specific topic and being applicable beyond Arch Linux.
```
