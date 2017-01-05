Digrss: simple feed polling
===========================

Instalation
-----------

For now, you can only install it directly from GitHub:
```
pip install https://github.com/cauebs/digrss/archive/master.zip
```

Usage
-----

```python
from digrss import Digrss

with Digrss(feeds_file_path='feeds.json', 
            interval=5, fetch_old=False) as d:

    for entry in d:
        print(entry['title'])
        print(entry['summary'])
```

+ `interval` is the polling interval in minutes
+ `fetch_old` defines whether past entries should be fetched on the first run
+ `feeds_file_path` must lead to a JSON file containing a list of feeds, e.g.:
```json
[
    {
        "url": "https://bost.ocks.org/mike/index.rss",
        "target": "optional@gmail.com"
    },
    {
        "url": "http://store.steampowered.com/feeds/news.xml",
        "target": "@optional"
    }
]
```

+ _The `target` attribute is completely optional and will be returned with each entry._

+ This file will be overwritten to save the `etag` and `modified` information, in order to ensure persistence. The `url` may also be replaced, if the original one led to a redirection or if it was incomplete.

The returned entries are FeedParserDicts and contain, among others*, the following attributes:

```link, title, authors, summary, content, links, published_parsed, updated_parsed, target```


_* read more in the [feedparser documentation](http://pythonhosted.org/feedparser/), under `entries[i]`_