from operator import itemgetter
import sys

current_headline = None
current_count = 0
heading = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    headline = line.strip()

    # parse the input we got from mapper.py
    article, count = headline.split('\t', 1)
    heading, desc = article.split("|")

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_headline == heading:
        current_count += count
    else:
        if current_headline:
            # write result to STDOUT
            if current_count>1:
                print('%s\t%s' % ("Heading:",current_headline," | Description:",desc, " | Count" current_count))
        current_count = count
        current_headline = heading

# do not forget to output the last word if needed!
if current_headline == heading:
    if current_count>1:
        print('%s\t%s' % ("Heading:",current_headline," | Description:",desc, " | Count" current_count))