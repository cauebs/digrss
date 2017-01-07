from queue import Queue
from threading import Thread
import feedparser
import json
import time


class Digrss:

    def __init__(self, feeds_file_path='feeds.json', interval=5, fetch_old=False):
        self.queue = Queue()
        self.interval = interval
        self.fetch_old = fetch_old
        self.feeds_file_path = feeds_file_path
        self._thread = Thread(target=self._poll)
        self._signal_stop = False

    def start(self):
        if not self._thread.is_alive():
            if self._signal_stop:
                self._thread = Thread(target=self.poll)
                self._signal_stop = False
            self._thread.start()

    def stop(self):
        self._signal_stop = True
        self._thread.join()

    def _poll(self):
        while not self._signal_stop:
            with open(self.feeds_file_path, 'r') as f:
                feeds = json.load(f)

            for sub in feeds:
                url = sub['url']
                if not url.startswith('http://'):
                    url = 'http://' + url
                last_etag = sub.get('etag')
                last_modified = sub.get('modified')
                feed = feedparser.parse(url, etag=last_etag, modified=last_modified)
                if feed.bozo:
                    continue

                for entry in feed.entries:
                    if not self.fetch_old:
                        if not last_modified:
                            break
                        if entry.updated_parsed <= feedparser._parse_date(last_modified):
                            continue

                    entry['target'] = sub.get('target')
                    self.queue.put(entry)

                sub['url'] = feed.get('href')
                sub['etag'] = feed.get('etag')
                sub['modified'] = feed.get('modified')

            with open(self.feeds_file_path, 'w') as f:
                json.dump(feeds, f, indent=4)

            time.sleep(self.interval * 60)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

    def __iter__(self):
        return self

    def __next__(self):
        return self.queue.get()
