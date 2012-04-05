Coming up with fun things I can do with DPLA data.  Wanted an excuse to use [the pretty Verite Timeline](https://github.com/VeriteCo/Timeline).

Done
----
+ build query
+ harvest and parse response
+ clean up json quirks so Timeline can read the result
+ output Timeline-formatted json (including hardcoded start date)
+ HTML page

Todo
----
+ figure out why query isn't returning what it should
+ allow for user input of search terms
+ better handling of dates (e.g. when the standard date field returns only a year, or something spurioius, do I want to harvest source-specific data?)
+ generate a logical start date
+ figure out a way of dealing with annoying NPR embeds spawning iTunes a million times (suppress, replace with better multimedia, etc.)