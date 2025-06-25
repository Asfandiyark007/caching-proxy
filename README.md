# CLI Caching Proxy

A command-line interface (CLI) tool that implements a simple caching system for storing and retrieving words associated with URLs. The cache includes automatic expiration and cleanup features.

## Features

- Cache words associated with specific URLs
- Automatic cache expiration after 12 hours
- Cache hit/miss notifications
- JSON-based persistent storage
- Automatic cleanup of expired cache entries

## Installation

1. Ensure you have Python installed on your system
2. Install the required dependencies:
```bash
pip install click
```

## Usage

Run the script using Python and follow the prompts:

```bash
python CLI-Cache.py --url "example.com" --cache "word-to-cache"
```

Or simply run:
```bash
python CLI-Cache.py
```
And follow the interactive prompts to enter the URL and words to cache.

### Parameters

- `--url`: The URL to associate with the cached words
- `--cache`: The word you want to cache for the specified URL

## Cache Storage

The cache is stored in a JSON file (`cache_store.json`) with the following structure:

```json
{
    "example.com": {
        "cached_words": ["word1", "word2"],
        "last_access": "HH:MM:SS",
        "last_date": "YYYY-MM-DD"
    }
}
```

## Cache Expiration

- Cache entries expire after 12 hours from their last access time
- Expired entries are automatically cleaned up when loading the cache or adding new entries

## Error Handling

- Handles corrupted JSON cache files by resetting the cache
- Validates URL and cache word inputs
- Maintains data persistence across sessions

## Technical Details

- Built with Python
- Uses Click library for CLI interface
- Implements datetime-based cache expiration
- JSON-based persistent storage system

## Contributing

Feel free to submit issues and enhancement requests!

## License

[MIT License](LICENSE)
