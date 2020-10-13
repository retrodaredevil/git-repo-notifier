#!/usr/bin/env python3

import sys
import time
from datetime import datetime
from traceback import print_exc

from typing import List

from git import Repo, GitCommandError
from slack import WebClient


def main(args: List[str]) -> int:
    repo = Repo(args[0])

    slack_token = args[1]
    slack_channel = args[2]

    client = WebClient(token=slack_token)

    origin = repo.remotes.origin

    last_commit = None
    while True:
        try:
            origin.pull()
        except GitCommandError as e:
            print(datetime.now())
            print_exc(e)
            print(f"Got error. Going to continue after waiting 30 seconds")
            print()
            time.sleep(30)
            continue

        commit = repo.head.commit
        commit_id = str(commit)
        if last_commit is None or last_commit == commit_id:
            last_commit = commit_id
            continue
        last_commit = commit_id

        author = commit.author
        message = commit.message.strip()
        text = f"{author} committed {commit_id}: {message}"
        print(datetime.now())
        print(text)
        print()
        client.chat_postMessage(channel=slack_channel, text=text)
        time.sleep(30)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
