import sys
import watchdog.observers
from watchdog.observers import polling

# Force PollingObserver to bypass inotify issues in VMs
watchdog.observers.Observer = polling.PollingObserver

from mkdocs.__main__ import cli

if __name__ == '__main__':
    # Set arguments to 'serve'
    sys.argv = ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
    try:
        cli()
    except SystemExit:
        pass
