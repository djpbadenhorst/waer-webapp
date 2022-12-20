import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import waer_utils

if __name__ == '__main__':
    waer_utils.call_user_id_api()
