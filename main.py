# main.py
import database
import feedparser
import command
import datetime
import handler
import findfeed
import logging

# Set up the logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler()]
)
# Parse the command line arguments
args = command.parser.parse_args()

# Connect to the database
db = database.Database("rss_feeds.db")

# Create an instance of the CommandHandler class
handler = handler.CommandHandler(db)

# Handle the "add" command
if args.command == "add":
    logging.debug("Handling add command")
    handler.handle_add_command(args)

# Handle the "parse" command
elif args.command == "parse":
    logging.debug("Handling parse command")
    handler.handle_parse_command(args)

# Handle the "view all" command
elif args.command == "view_all":
    logging.debug("Handling view all command")
    handler.handle_view_all_command(args)

# Handle the "read" command
elif args.command == "read":
    logging.debug("Handling read command")
    handler.handle_read_command(args)

# Handle the "find_feed" command
elif args.command == "findfeed":
    logging.debug("Handling findfeed command")
    handler.handle_findfeed_command(args)

# Handle the "delete" command
elif args.command == "delete":
    logging.debug("Handling delete command")
    handler.handle_delete_command(args)

# Handle the "classify" command
elif args.command == "classify":
    logging.debug("Handling classify command")
    handler.handle_classify_command(args)
    
# Close the database connection
db.close_connection()
