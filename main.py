#!/usr/bin/env python3

import sys
import time

from typing import List

from git import Repo, Git


def main(args: List[str]) -> int:
    repo = Repo(args[0])

    origin = repo.remotes.origin

    last_commit = None
    while True:
        origin.pull()
        commit = repo.head.commit
        commit_id = str(commit)
        if last_commit is None or last_commit == commit_id:
            last_commit = commit_id
            continue
        last_commit = commit_id

        author = commit.author
        message = commit.message.strip()
        print(f"{author} committed {commit_id}: {message}")
        time.sleep(10)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
