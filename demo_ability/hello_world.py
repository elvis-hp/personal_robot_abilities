#!/usr/bin/env python
from sdk import send_json
import json

data_send = {"action": "t2s", "text": "hello world"}

#send data to brain:
package = {"type": "t2s", "data": json.dumps(data_send), "source": "", "protocol": ""}
send_json(json.dumps(package))