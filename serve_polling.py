#!/usr/bin/env python3
"""
MkDocs serve with forced polling observer for VM environments.
This bypasses inotify issues by using polling instead.
"""
import sys
import os

# Force polling observer BEFORE importing mkdocs
import watchdog.observers
from watchdog.observers import polling

# Replace the default Observer with PollingObserver
watchdog.observers.Observer = polling.PollingObserver

# Now import and run mkdocs normally
from mkdocs.__main__ import cli

if __name__ == '__main__':
    # Run mkdocs serve
    sys.argv = ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8000"]
    cli()
