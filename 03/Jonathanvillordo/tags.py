from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    
    xml = open(RSS_FEED,'r')
    lst = ''
    
    for i in xml:
        lst = TAG_HTML.findall(i)
    
    return lst



def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    c = Counter(tags)
    
    return c.most_common(10)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""

    words = {}

    for str1,str2 in product(tags, tags):
        plural = str2
        singular = str1

        if singular[0] == plural[0] and singular != plural:
            ratio = SequenceMatcher(None, singular, plural).ratio()
            
            if singular.endswith("s"):
                plural = singular
                singular = plural
            if SIMILAR <= ratio and singular not in words:
                words[singular] = plural
                
    return words
   


if __name__ == "__main__":
    
    tags = get_tags()
    top_tags = get_top_tags(tags)
    
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
