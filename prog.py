import  argparse


parser = argparse.ArgumentParser()

parser.add_argument("--channel",help="Channel name is required")
parser.add_argument("--JsonFile",help="Provide the link for JSON File")
parser.add_argument("--byte",help="Provide basic data to send")


args = parser.parse_args()
print(args.echo)
