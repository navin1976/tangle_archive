from iota.commands.extended.send_transfer import SendTransferCommand 
from iota.commands import FilterCommand, RequestFilter
from iota.crypto.types import Seed
from iota.filters import Trytes
from iota import Address, Bundle, Iota, ProposedTransaction, \
  TransactionTrytes, TryteString

class transaction():
    
    def send_transfers():
        

        transfer1 =\
            ProposedTransaction(
                address =
                Address(
                    b'TESTVALUEFIVE9DONTUSEINPRODUCTION99999MG'
                    b'AAAHJDZ9BBG9U9R9XEOHCBVCLCWCCCCBQCQGG9WHK'
                ),

                value = 30,
            )

        transfer2 =\
            ProposedTransaction(
                address =
                Address(
                    b'TESTVALUESIX9DONTUSEINPRODUCTION99999GGT'
                    b'FODSHHELBDERDCDRBCINDCGQEI9NAWDJBC9TGPFME'
                ),

                value = 40,
            )
        transfer_list=[transfer1,transfer2]
        

        request={'changeAddress':"", #optional 
            'depth':3,
            'inputs':None,          #it is optional
            'minWeightMagnitude':18,
            'seed':"ZCTFPRYGEAC9MGFLYLOQVGZBHDLEULMZKIXRAZPPJCAJPANAUSL9BVVAPZSVYLLWNPEYKZQEVO9A9YYP",
            'transfers':transfer_list
            }



        A=SendTransferCommand(request)

        print(A._execute(request))



 