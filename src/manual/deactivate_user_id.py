import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import waer_utils

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR - Please provider user_id')
    else:
        waer_utils.call_deactivate_api(sys.argv[1])
