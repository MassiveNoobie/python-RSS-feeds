# python-RSS-feeds
python RSS feeds and sends to wordpress post, in a single script per rss feed.

Is it possible for a website to grow passively by running scripts using our free task scheduler nodejs vuejs electronjs desktop app?
- update "10/19/2022" large spike in traffic, growth M/M consistent
- users grown from 10 per day to 100-200+ per day.
- Daily avg shifted to 158\ as of october.

single scripts to run on https://canopys.io per rss feed, best as possible 

protyping first, optimize later


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

- text analysis, ai/ml for usage across;
post.terms_names = {
    'post_tag': ['Startup', 'TechCrunch'],
    'category': ['Tech']
  }

# skipping database usage for now
For now, workaround is the ability to automatically delete any duplicates, allowing us to keep the new content.
Website end point running "Delete Duplicate Posts v. 4.7.9" a free wordpress plugin, the plugin allows the mono usage.


# project status
completed rss feed for cnn. ended up requiring 3 loops to catching most of the news, excluding live news.

# join?
discord available via request, @itylergarrett on twitter
