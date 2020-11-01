## Wandering around America with Mark Twain

This is my contribution for NaNoGenMo 2020. It was written in December 2019, mostly because I always end up being way too busy in November to do a NaNoGenMo project.

The "novel" finds U.S. place names from four Mark Twain novels, and then gives driving directions from one place to the next. The idea is that you can follow the fictional travels of Twain’s characters, while mostly sticking to today’s U.S. interstate system.

- `fetch_data.py` parses the Mark Twain texts, makes some API calls and saves all the Google Maps data. Running this requires a Google Maps API key, saved in a file called `settings.py`.
- `novelize.py` produces the "novel"
- you can see the end result at `novel.txt`
