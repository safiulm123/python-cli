import  argparse


parser = argparse.ArgumentParser()
# This provides the Channel Name for the data to transfer on
parser.add_argument("--channel",help="Channel name is required")



# This provides the JsonFile for the data 
parser.add_argument("--JsonFile",help="Provide the link for JSON File")


#parser.add_argument("--byte",help="Provide basic data to send")


args = parser.parse_args()

if args.channel:
    if args.JsonFile:
        print(args.channel + args.JsonFile)
