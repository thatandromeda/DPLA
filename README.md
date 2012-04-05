Coming up with fun things I can do with DPLA data.  Wanted an excuse to use [the pretty Verite Timeline](https://github.com/VeriteCo/Timeline).

Done
----
+ build query
+ harvest and parse response
+ clean up json quirks so Timeline can read the result
+ output Timeline-formatted json (including hardcoded start date)
+ HTML page
+ allow for user input of search terms

Todo
----
+ better handling of dates (e.g. when the standard date field returns only a year, or something spurioius, do I want to harvest source-specific data?)
+ generate a logical start date
+ figure out a way of dealing with annoying NPR embeds spawning iTunes a million times (suppress, replace with better multimedia, etc.)
+ get better embeds from biodiversity library
+ deal with NaN dates
+ redirect from user input page to timeline page; how does cherrypy find that page?