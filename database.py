import sqlite3
import feedparser

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table("rss_feeds", "id INTEGER PRIMARY KEY, url TEXT, name TEXT, description TEXT")
        self.create_table("rss_items", "id INTEGER PRIMARY KEY, title TEXT, link TEXT, description TEXT, feed_url TEXT, pub_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP")

    def create_table(self, table_name, columns):
        """Create a table in the database"""
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_rss_feed(self, url):
        """Insert a RSS feed into the database"""
        feed = feedparser.parse(url)
        name = feed.feed.title
        description = feed.feed.description
        query = "INSERT INTO rss_feeds (url, name, description) VALUES (?,?,?)"
        self.cursor.execute(query, (url, name, description))
        self.conn.commit()

    def insert_rss_item(self, title, link, description, feed_url, pub_date):
        """Insert a RSS item into the database"""
        query = "INSERT INTO rss_items (title, link, description, feed_url, pub_date) VALUES (?,?,?,?,?)"
        self.cursor.execute(query, (title, link, description, feed_url, pub_date))
        self.conn.commit()

    def read_rss_feeds(self):
        """Read all RSS feeds from the database"""
        query = "SELECT * FROM rss_feeds"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def read_rss_entries(self, feed_url):
        """Read all RSS items from a specific feed in the database"""
        query = "SELECT * FROM rss_items WHERE feed_url = ?"
        self.cursor.execute(query, (feed_url,))
        return self.cursor.fetchall()

    def delete_rss_feed(self, feed_url):
        query = "DELETE FROM rss_feeds WHERE url = ?"
        self.cursor.execute(query, (feed_url,))
        self.conn.commit()
        print(f"RSS feed {feed_url} deleted from the database.")

    def close_connection(self):
        """Close the database connection"""
        self.conn.close()
