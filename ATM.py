class ATM(object):
    def __init__(self,user,atm_card_number,pin_number):
        self.user = user
        self.atm_card_number =atm_card_number
        self.pin_number = pin_number
    
    def CashWithDraw(self):
        print("With draw completed")
    
    def BalanceEnquiry(self):
        print("Your current balance is 50000 USD")

Lisa=ATM("Lisa","1592bk",17958352 )

print(Lisa.CashWithDraw())