

def get_query(args):
    if len(args) > 1 and len(args[1]) > 0:
        return args[1]
    else:
        print("\nNo proper string argument given\n")
        return None