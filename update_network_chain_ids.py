"""
Script that syncs Network ChainId constants in eth_typing/networks.py
with the current list of networks from chainid.network.

To run the script:

.. code-block:: shell

    $ python update_network_chain_ids.py

After running the command, check the output in eth_typing/networks.py

If all looks good, open a PR with the changes.
"""

import json
import os
import urllib.request

networks_file = "eth_typing/networks.py"

# Just replace the file entirely
os.remove(networks_file)

# Open and begin writing the Networks python module
f = open(networks_file, "w")
f.write(
    "from enum import (\n" + "    IntEnum,\n" + ")\n\n\n" + "class ChainId(IntEnum):\n"
)

# Load the latest JSON from chainid.network and loop over each Network.
# Each constant consists of the Network shortName and chainId, where the
# shortName is capitalized and used as the constant name and the chainId is
# the value. i.e. for name "eth" and chainId "1", the constant would be ETH = 1
with urllib.request.urlopen("https://chainid.network/chains_mini.json") as url:
    data = json.load(url)
    for d in data:
        name, chainId = d["shortName"], d["chainId"]
        if name[0].isdigit():
            name = "_" + name

        enum = (
            "".join(["_" if i == "-" else i.upper() for i in name]).lstrip("-")
            + " = "
            + str(chainId)
            + "\n"
        )
        enum = f"    {enum}"
        f.write(enum)

f.close()
