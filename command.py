import argparse

# Set up the command line argument parser
parser = argparse.ArgumentParser(description="RSS Feed Database")
subparsers = parser.add_subparsers(dest="command")

# Create the "add" command
add_parser = subparsers.add_parser("add")
add_parser.add_argument("feed_url", type=str, help="URL of the RSS feed to add to the database")

# Create the "parse" command
parse_parser = subparsers.add_parser("parse")
parse_parser.add_argument("feed_url", type=str, help="URL of the RSS feed to parse and add to the database")

# Create the "view all" command
view_all_parser = subparsers.add_parser("view_all")

# Create the "read" command
read_parser = subparsers.add_parser("read")
read_parser.add_argument("feed_url", type=str, help="URL of the RSS feed to read from the database")

# Create the "findfeed" command
findfeed_parser = subparsers.add_parser("findfeed")
findfeed_parser.add_argument("website_url", type=str, help="URL of the website to find RSS feeds on")

# Create the "delete" command
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("feed_url", type=str, help="URL of the RSS feed to delete from the database")

# Create the "classify" command
classify_parser = subparsers.add_parser("classify")
classify_parser.add_argument("feed_url", type=str, help="URL of the RSS feed to classify the entries of")