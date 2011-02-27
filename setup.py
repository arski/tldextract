import re
from setuptools import setup
import tldextract

# I don't want to learn reStructuredText right now, so strip Markdown links
# that make pip barf.
long_description_markdown = tldextract.tldextract.__doc__
long_description = re.sub(r'\[(.*?)\]\((http.*?)\)', r' \1 (\2)', long_description_markdown, flags=re.DOTALL)

setup(
    name = "tldextract",
    version = tldextract.__version__,
    author = "John Kurkowski",
    author_email = "john.kurkowski@gmail.com",
    description = ("Accurately separate the gTLD/ccTLD component from the "
        "registered domain and subdomains of a URL."),
    license = "BSD License",
    keywords = "tld domain subdomain url parse extract urlparse",
    url = "https://github.com/john-kurkowski/tldextract",
    packages = ['tldextract'],
    long_description = long_description,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
