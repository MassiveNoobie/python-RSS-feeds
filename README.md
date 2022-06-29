# python-RSS-feeds
python RSS feeds and sends to wordpress post, in a single script per rss feed.

Is it possible for a website to grow passively by running monolithic scripts using our free task scheduler nodejs vuejs electronjs desktop app?

mono = monolithic to run on https://canopys.io 
"A monolith is a codebase composed all in one piece. This typically means all code in one massive codebase."

Each rss feed is one monolith chunk of code.

# notes on rss feeds in python
the bigger the rss feed, the more difficult the html, css, and javascript, however it also makes me learn a lot about what i dislike about my code. lot of room for easy deleting content or strange implemented advertisements in future solves as i begin to learn best practices for wildcard matching removal of content.

# future goals;
- create functions
- filter better
- score content/sentiment
- add more rss feeds
- automate it all using canopys.io
- optimize everything
- microservice build? ehhh maybe way down road

# skipping database usage for now
For now, workaround is the ability to automatically delete any duplicates, allowing us to keep the new content.
Website end point running "Delete Duplicate Posts v. 4.7.9" a free wordpress plugin, the plugin allows the mono usage.


# project status
stuck on CNN rss feed, it's a beast, however getting closer.
    result = str(soup.find_all("div", {"class": "zn-body__paragraph"}))
That is all for now.

# join?
discord available via request, @itylergarrett on twitter
