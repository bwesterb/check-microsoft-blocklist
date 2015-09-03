import lockfile
import yaml

import os.path
import urllib
import json
import csv

def main():
    # Load settings
    with open('settings.yaml') as f:
        settings = yaml.load(f)

    # Fetch spam status
    raw_csv = urllib.urlopen(settings['url'].strip())

    with lockfile.FileLock('state.json'):
        # Load state
        try:
            if not os.path.exists('state.json'):
                raise ValueError
            with open('state.json') as f:
                state = json.load(f)
        except ValueError:
            state = {}

        # Check for changes
        seen = set()
        changes = []
        for row in csv.reader(raw_csv):
            if len(row) != 4:
                continue
            ip_from, ip_until, blocked, reason = row
            if ip_from == ip_until:
                key = ip_from
            else:
                key = ip_from + '-' + ip_until
            seen.add(key)
            value = [blocked, reason]
            if key in state and state[key] == value:
                continue
            changes.append((key, value))
            state[key] = value

        for key in state:
            if key in seen:
                continue
            value = [False, '']
            if state[key] == value:
                continue
            state[key] = value
            changes.append((key, value))

        # Save changes
        if not changes:
            return

        with open('state.json', 'w') as f:
            json.dump(state, f)

        # Print output
        body = ('There were changes in your Microsoft Junk '+
                    'Reporting Program Feed:\n'+
                '\n')
        for key, value in changes:
            body += (key + ': ' +
                     ('BLOCKED' if bool(value[0]) else 'ok') + ' ' + value[1]
                    + "\n")
        print body

if __name__ == '__main__':
    main()

# vim: ts=4 sw=4 et
