#!/usr/bin/env python3
# Copyright (c) 2014-2016 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Test the abandontransaction RPC.

 The abandontransaction RPC marks a transaction and all its in-wallet
 descendants as abandoned which allows their inputs to be respent. It can be
 used to replace "stuck" or evicted transactions. It only works on transactions
 which are not included in a block and are not currently in the mempool. It has
 no effect on transactions which are already abandoned.
"""
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import *


class TXConflictTest(BitcoinTestFramework):
    def set_test_params(self):
        self.num_nodes = 2
        self.setup_clean_chain = True
        
    def run_test(self):
        connect_nodes(self.nodes[0], 1)
        self.nodes[0].generate(100)
        self.sync_all()
        self.log.info("Blocks %s"% self.nodes[0].getblockcount())
        self.nodes[0].generate(100)
        self.sync_all()
        self.log.info("Blocks %s"% self.nodes[0].getblockcount())
        self.nodes[0].generate(100)
        self.sync_all()
        self.log.info("Blocks %s"% self.nodes[0].getblockcount())
        self.nodes[0].generate(100)
        self.sync_all()
        self.log.info("Blocks %s"% self.nodes[0].getblockcount())
if __name__ == '__main__':
    TXConflictTest().main()