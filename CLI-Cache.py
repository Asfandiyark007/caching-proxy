import click
import json
import os
import time
from datetime import datetime, timedelta

CACHE_FILE = "cache_store.json"


def is_cache_expired(timestamp_str):
    cache_time = datetime.strptime(timestamp_str, "%H:%M:%S")
    cache_time = cache_time.replace(
        year=datetime.now().year, month=datetime.now().month,
        day=datetime.now().day
    )
    current_time = datetime.now()
    expiration_time = timedelta(hours=12)
    return current_time - cache_time > expiration_time


def cleanup_expired_cache(store):
    urls_to_remove = []
    for url, data in store.items():
        if is_cache_expired(data["last_access"]):
            urls_to_remove.append(url)

    for url in urls_to_remove:
        del store[url]
    return store


def load_store():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            try:
                store = json.load(f)
                return cleanup_expired_cache(store)
            except json.JSONDecodeError:
                return {}
    return {}


def save_store(store):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False)


@click.command()
@click.option("--url", prompt="Enter URL", help="Dummy website url")
@click.option(
    "--cache", prompt="Enter the words", help="The words" +
    "you want to cache!"
)
def check(cache, url):
    store = load_store()
    current_time = time.strftime("%H:%M:%S")
    current_datetime = datetime.now()
    only_date = current_datetime.date()

    # cleanup expired entries before checking
    store = cleanup_expired_cache(store)

    # initialize url entry if it doesn't exist
    if url not in store:
        store[url] = {
            "cached_words": [],
            "last_access": current_time,
            "last_date": only_date.isoformat(),
        }

    if cache in store[url]["cached_words"]:
        click.echo("Cache Hit Alert !!!")
    else:
        click.echo("Cache Miss Alert !!!")
        store[url]["cached_words"].append(cache)
        store[url]["last_access"] = current_time
        store[url]["last_date"] = only_date.isoformat()
        save_store(store)


if __name__ == "__main__":
    check()
