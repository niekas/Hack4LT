import unicodedata
import re


def slugify(s, sep='-', allowed_chars='_-'):
    """
    >>> print slugify(u'a.b@gmail.com')
    a.b-at-gmail.com
    >>> print slugify(u'a.b@gmail.com', allowed_chars='-')
    a-b-at-gmail-com
    >>> print slugify(u'A - b -- c -')
    a-b-c
    >>> print slugify(u'A - b -- c - . Ttt')
    a-b-c.ttt
    >>> print slugify(U'2012-05-02 12:12.txt')
    2012-05-02-12-12.txt
    >>> print slugify(u'2012-05-02 12:12.txt', sep='_', allowed_chars='-_.:')
    2012-05-02_12:12.txt
    """
    if not sep in allowed_chars:
        raise Exception('Separator should be in allowed characters')
    s = s.replace('@', '-at-')
    slug = unicodedata.normalize('NFKD', s)
    slug = slug.encode('ascii', 'ignore').lower()
    rsep = re.escape(sep)
    rchars = re.escape(allowed_chars)
    r = r'([^\w%s]+)' % rchars
    slug = re.sub(r, sep, slug).strip(sep)
    r = r'(%s*)([%s])(%s*)' % (rsep, rchars, rsep)
    slug = re.sub(r, r'\2', slug)
    return slug
