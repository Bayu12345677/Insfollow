import instaloader as ig

import sys, os

try:
    args = sys.argv[1]
except:
    pass

try:
    setup = ig.Instaloader()
    profile = ig.Profile.from_username(setup.context, args)
    print(profile.userid)
except:
    exit("failed")
