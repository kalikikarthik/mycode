# configuration helper script.
#
# 1) Loads 'config.json' from current directory.
# 2) Walks the keys and updates the values when a) values are blank and b) environment variable is set with a permitted value.
# 3) If changes are applies, write 'config.json' back to current directory.
#

import sys
import os
import os.path
import json

# The values that can be updated via environment variables.
ENV_VALUES=('user', 'api_key', 'conn_string', 'ip_address')

# Config filename.
CONF_FILE=os.path.join(os.path.dirname(__file__), 'config.json')

# Read and parse the current config.file.
conf = file(CONF_FILE, 'rb')
data = json.load(conf)
conf.close()

changed = False
# Walk the keys in the current configuration.
for key, value in data.items():
    if (value == ''):
        # Check that this is an allowed value and that it exists.
        if (key.lower() in ENV_VALUES and os.environ.get(key)):
            # Update the value and set the changed flag.
            data[key] = os.environ.get(key)
            changed = True

# If things have changed, re-write the config file.
if changed:
    conf = file(CONF_FILE, 'wb')
    json.dump(data, conf)
    conf.close()
