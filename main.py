# main.py

import database
import feedparser
import command
import datetime
import handler
import findfeed

# Parse the command line arguments
args = command.parser.parse_args()

# Connect to the database
db = database.Database("rss_feeds.db")

# Create an instance of the CommandHandler class
handler = handler.CommandHandler(db)

# Handle the "add" command
if args.command == "add":
    handler.handle_add_command(args)

# Handle the "parse" command
elif args.command == "parse":
    handler.handle_parse_command(args)

# Handle the "view all" command
elif args.command == "view_all":
    handler.handle_view_all_command(args)

# Handle the "read" command
elif args.command == "read":
    handler.handle_read_command(args)

# Handle the "find_feed" command
elif args.command == "findfeed":
    handler.handle_findfeed_command(args)

# Handle the "delete" command
elif args.command == "delete":
    handler.handle_delete_command(args)

# Handle the "classify" command
elif args.command == "classify":
    handler.handle_classify_command(args)
    
# Close the database connection
db.close_connection()
