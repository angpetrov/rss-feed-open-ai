import openai
import findfeed
import feedparser
import datetime

class CommandHandler:
    def __init__(self, db):
        self.db = db

    def handle_add_command(self, args):
        self.db.insert_rss_feed(args.feed_url)
        print(f"RSS feed {args.feed_url} added to the database.")

    def handle_parse_command(self, args):
        feed = feedparser.parse(args.feed_url)
        pub_date = datetime.datetime.now()
        for entry in feed.entries:
            self.db.insert_rss_item(entry.title, entry.link, entry.description, args.feed_url, pub_date)
        print(f"RSS feed {args.feed_url} parsed and added to the database.")

    def handle_view_all_command(self, args):
        feeds = self.db.read_rss_feeds()
        for feed in feeds:
            print(feed)

    def handle_read_command(self, args):
        entries = self.db.read_rss_entries(args.feed_url)
        for entry in entries:
            print(f"Title: {entry[1]}\nLink: {entry[2]}\nDescription: {entry[3]}")

    def handle_findfeed_command(self, args):
        feed_urls = findfeed.find_feed(args.website_url)
        for url in feed_urls:
            print(url)
            self.db.insert_rss_feed(url)
        print(f"RSS feeds found on {args.website_url} added to the database.")

    def handle_delete_command(self, args):
        self.db.delete_rss_feed(args.feed_url)
        print(f"RSS feed {args.feed_url} deleted from the database.")

    def handle_classify_command(self, args):
        openai.api_key = "YOUR_API_KEY"
        model_engine = "ENGINE_SELECTED"

        feed_url = args.feed_url

        prompt = f"Classify the entries of the RSS feed at {feed_url}"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        print(message)
