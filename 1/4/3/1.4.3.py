#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tx

# Exercice 1.4.3
tx = tx.Tx("010000000"+"1941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d010000006b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed48a81Feffffff")

# Exercice 1.4.4
# tx = tx.Tx("0100000001f129de033c57582efb464e94ad438fff493cc4de4481729b85971236858275c2010000006a4730440220155a2ea4a702cadf37052c87bfe46f0bd24809759acff8d8a7206979610e46f6022052b688b784fa1dcb1cffeef89e7486344b814b0c578133a7b0bce5be978a9208012103915170b588170cbcf6380ef701d19bd18a526611c0c69c62d2c29ff6863d501affffffff02ccaec817000000001976a9142527ce7f0300330012d6f97672d9acb5130ec4f888ac18411a000000000017a9140b8372dffcb39943c7bfca84f9c40763b8fa9a068700000000")

tx.parcours()
print(tx)
