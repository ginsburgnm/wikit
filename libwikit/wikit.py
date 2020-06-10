#!/usr/bin/env python3
"""Wiki it as a python script because why do I want npm?"""
import argparse
import webbrowser
import wikipediaapi

def parse_args():
    """Get commandline args"""
    parser = argparse.ArgumentParser(description='Search Wikipedia')
    parser.add_argument('subject', type=str, nargs='+', help='string to search Wikipedia for')
    parser.add_argument('-a', action='store_true', help='Full text of wiki page')
    parser.add_argument('-l', type=str, help='Language code', default='en')
    parser.add_argument('--link', action='store_true', help='Display link at end')
    parser.add_argument('-d', action='store_true', help='grab disambiguation')
    parser.add_argument('-b', action='store_true', help='Open page in default browser')
    parser.add_argument('--browser', type=str, help='Specify a browser')
    args = vars(parser.parse_args())
    args['subject'] = '_'.join(args['subject'])
    args['subject'] = "%s_(disambiguation)" % args['subject'] if args['d'] else args['subject']
    return args

def main():
    """Parse arguments, create wikiapi object, print output"""
    args = parse_args()
    page_py = wikipediaapi.Wikipedia(args['l']).page(args['subject'])
    if page_py.exists():
        if args['b'] or args['browser']:
            webbrowser.get(args['browser']).open(page_py.fullurl)
        else:
            print(page_py.text if args['a'] else page_py.summary)
            if args['link']:
                print(page_py.fullurl)
    else:
        print("Page not found")

if __name__ == "__main__":
    main()
