from typing import List, Union, Optional

##################################################################################
# Instruction for Students:
# 1. จงเขียน Class Diagram เพื่อออกแบบ Class ต่างๆ ให้รองรับการทำงานของ Code ส่วนล่าง
# 2. จงเขียน Class Definition (Bank, User, Account, ATM_Card, ATM_machine, Transaction)
#    เพื่อให้สามารถรัน Function run_test() ได้โดยไม่เกิด Error
# 3. ห้ามแก้ไข Code ในส่วนของ create_bank_system() และ run_test() โดยเด็ดขาด
# 4. ต้องมีการ Validate ข้อมูลตามเงื่อนไขที่กำหนดในเอกสาร Lab (เช่น เงินไม่พอ, PIN ผิด)
#    และทำการ Raise Exception เมื่อเกิดข้อผิดพลาด
##################################################################################

# --- พื้นที่สำหรับเขียน Class ของนักศึกษา (เขียนต่อจากตรงนี้) ---

class Bank:
    def __init__(self, name):
        self.__name = name
        self.__user = []
        self.__ATM = []
    
    def add_user(self, user):
        if isinstance(user,User):
            self.__user.append(user)
            
    def add_atm_machine(self, atm_machine):
        if isinstance(atm_machine, ATM_machine):
            self.__ATM.append(atm_machine)
            

    def get_atm_by_id(self, atm_ID):
        for index, item in enumerate(self.__ATM):
            if atm_ID == item.get_ATM_ID():
                return item
        
    
    def search_account_from_atm(self, atmNum):
        for index1, item1 in enumerate(self.__user):
            for index2, item2 in enumerate(item1.get_account()):
                if atmNum == item2.atm_card.get_cardNum():
                    return item2
        return False
                
    

class User:
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name
        self.__account = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.__account.append(account)
    
    def get_account(self):
        return self.__account
    
    def get_name(self):
        return self.__name
        

class Account:
    def __init__(self, account_no, user, amount):
        self.__account_no = account_no
        self.__user = user
        self.__balance = amount
        self.__atm_card = None
        self.__transaction = []
        self.__daily = 0


    def add_atm_card(self, atm_card):
        if isinstance(atm_card, ATM_Card):
            self.__atm_card = atm_card
            
    @property
    def atm_card(self):
        return self.__atm_card
    
    @property
    def amount(self):
        return self.__balance
    
    @amount.setter
    def transferIn(self, amountIn):
        self.__balance += amountIn
    
    @property
    def account_no(self):
        return self.__account_no
    
    @property
    def user(self):
        return self.__user
    
    def transaction(self):
        return self.__transaction
    
    def fee(self):
        if self.__balance < 150:
            raise Exception("Does not enough balance for charging yearly fee.")
        else:
            self.__balance -= 150
        
    
        
    def deposit(self, atm, amount):
        if isinstance(atm, ATM_machine):
            if not isinstance(amount, str):
                if amount < 0 :
                    raise Exception("Error : Invalid amount of money")
                if atm.isInsert:
                    if atm.cardAcc == self.__atm_card:
                        self.__balance += amount
                        atm.cash = amount
                        self.__transaction.append(Transaction(atm.get_ATM_ID(), "D", amount, self.__balance, None))
                else:
                    raise Exception("Wrong ATM card or account")
            else:
                raise Exception("Error : Amount must be number not str")
            
    def withdraw(self, atm, amount):
        if isinstance(atm, ATM_machine):
            if not isinstance(amount, str):
                if amount < 0:
                    raise Exception("Error : Invalid amount of money")
                if atm.isInsert:
                    if atm.cardAcc == self.__atm_card:
                        if self.__daily + amount > 40000:
                            raise Exception("Error : Exceed amount of daily limit")
                        elif atm.cash < amount:
                            raise Exception("Error : Not enough cash")
                        elif self.__balance < amount:
                            raise Exception("Error : Not enough balance")
                        else:
                            self.__balance -= amount
                            atm.cash = -amount
                            self.__daily += amount
                            self.__transaction.append(Transaction(atm.get_ATM_ID(), "W", amount, self.__balance, None))
                else:
                    raise Exception("Wrong ATM card or account")
            else:
                raise Exception("Error : Amount must be number not str")

            
    def transfer(self, atm, amount, payee):
        
        if isinstance(atm, ATM_machine) and isinstance(payee, Account):
            if not isinstance(amount, str):
                if amount < 0 or self.__daily >= 40000:
                    raise Exception("Error : Invalid amount of money  or Exceed amount of daily limit")
                if atm.isInsert :
                    if atm.cardAcc == self.__atm_card:
                        if self.__balance < amount:
                            raise Exception("Error : Not enough balance")
                        elif self.__daily >= 40000:
                            raise Exception("Error : Exceed amount of daily limit")
                        else:
                            self.__balance -= amount
                            self.__daily += amount
                            payee.transferIn = amount
                            self.__transaction.append(Transaction(atm.get_ATM_ID(), "TW", amount, self.__balance, payee.user.get_name()))
                            payee.transaction().append((Transaction(atm.get_ATM_ID(), "TD", amount, payee.amount, self.__user.get_name())))
                else:
                    raise Exception("Wrong ATM card or account")

            else :
                raise Exception("Error : Amount must be number not str")
            
    def print_transactions(self):
        for __, item in enumerate(self.__transaction):
            item.Print()
            
    

class ATM_Card:
    def __init__(self, cardNum, accNum, PIN):
        self.__cardNum = cardNum
        self.__accNUm = accNum
        self.__PIN = PIN
    
    def check_PIN(self, pin):
        if pin == self.__PIN:
            return True
        else: return False

    def get_cardNum(self):
        return self.__cardNum
        

class ATM_machine:
    def __init__(self, ATM_ID, cash):
        self.__ATM_ID = ATM_ID
        self.__cash = cash
        self.__isInsert = False
        self.__card = None

    def get_ATM_ID(self):
        return self.__ATM_ID

    def insert_card(self, atm_card, pin):
        if isinstance(atm_card, ATM_Card):
            if atm_card.check_PIN(pin):
                self.__card = atm_card
                self.__isInsert = True
                return True
            else: return False

    @property
    def cardAcc(self):
        return self.__card

    @property
    def isInsert(self):
        return self.__isInsert
    
    @property
    def cash(self):
        return self.__cash

    @cash.setter
    def cash(self, cashIn):
        self.__cash += cashIn



class Transaction:
    def __init__(self, atmID, type, amount, balance, payee):
        self.__atm_ID = atmID
        self.__type = type
        self.__amount = amount
        self.__balance = balance
        self.__payee = payee

    def Print(self):
        print(f"ATM ID : {self.__atm_ID}")
        print(f"Transaction Type : {self.__type}")
        print(f"Amount : {self.__amount}")
        print(f"Balance : {self.__balance}")
        if self.__payee != None:
            print(f"Payee : {self.__payee}")
        print("--------------------------------------------")

    


##################################################################################
# Test Case & Setup : ห้ามแก้ไข Code ส่วนนี้
# ใช้สำหรับตรวจสอบว่า Class ที่ออกแบบมาถูกต้องตาม Requirement หรือไม่
##################################################################################

def create_bank_system() -> Bank:
    print("--- Setting up Bank System ---")
    
    # 1. กำหนดชื่อธนาคาร
    scb = Bank("SCB")
    
    # 2. สร้าง User, Account, ATM_Card
    # Data format: CitizenID: [Name, AccountNo, ATM Card No, Balance]
    user_data = {
       '1-1101-12345-12-0': ['Harry Potter', '1000000001', '12345', 20000],
       '1-1101-12345-13-0': ['Hermione Jean Granger', '1000000002', '12346', 1000]
    }
    
    for citizen_id, detail in user_data.items():
        name, account_no, atm_no, amount = detail
        
        user_instance = User(citizen_id, name)
        user_account = Account(account_no, user_instance, amount)
        atm_card = ATM_Card(atm_no, account_no, '1234')
        
        user_account.add_atm_card(atm_card)
        user_instance.add_account(user_account)
        scb.add_user(user_instance)

    # 3. สร้างตู้ ATM
    scb.add_atm_machine(ATM_machine('1001', 1000000))
    scb.add_atm_machine(ATM_machine('1002', 200000))

    return scb

def run_test():
    scb = create_bank_system()
    
    atm_machine1 = scb.get_atm_by_id('1001')
    atm_machine2 = scb.get_atm_by_id('1002')
    
    harry_account = scb.search_account_from_atm('12345')
    hermione_account = scb.search_account_from_atm('12346')
    
    # ตรวจสอบว่าหา Account เจอหรือไม่
    if not harry_account or not hermione_account:
        print("Error: Could not find accounts. Check your search_account_from_atm method.")
        return

    harry_card = harry_account.atm_card
    
    print("\n--- Test Case #1 : Insert Card (Harry) ---")
    print(f"Harry's Account No : {harry_account.account_no}")

    if atm_machine1.insert_card(harry_card, "1234"):
        print("Success: ATM accepted valid card and PIN")
    else:
        print("Error: ATM rejected valid card")

    print("\n--- Test Case #2 : Deposit 1000 to Hermione ---")
    print(f"Before: {hermione_account.amount}")

    try:
        hermione_account.deposit(atm_machine2, 1000)
        print(f"After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #3 : Deposit -1 (Expect Error) ---")
    try:
        hermione_account.deposit(atm_machine2, -1)
        print("Error: Failed to catch negative deposit")
    except ValueError as e: # คาดหวัง ValueError หรือ Exception ที่เหมาะสม
        print(f"Pass: System correctly raised error -> {e}")
    except Exception as e:
        print(f"Pass: System raised error -> {e}")

    print("\n--- Test Case #4 : Withdraw 500 from Hermione ---")
    print(f"Before: {hermione_account.amount}")

    try:
        hermione_account.withdraw(atm_machine2, 500)
        print(f"After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #5 : Withdraw Excess Balance (Expect Error) ---")
    try:
        hermione_account.withdraw(atm_machine2, 30000)
        print("Error: Failed to catch overdraft")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

    print("\n--- Test Case #6 : Transfer 10000 from Harry to Hermione ---")
    print(f"Harry Before: {harry_account.amount}")
    print(f"Hermione Before: {hermione_account.amount}")

    try:
        harry_account.transfer(atm_machine2, 10000, hermione_account)
        print(f"Harry After: {harry_account.amount}")
        print(f"Hermione After: {hermione_account.amount}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Test Case #7 : Transaction History ---")

    print("Harry Transactions:")
    harry_account.print_transactions()
    print("Hermione Transactions:")
    hermione_account.print_transactions()

    print("\n--- Test Case #8 : Wrong PIN (Expect Error) ---")
    if not atm_machine1.insert_card(harry_card, "9999"):
        print("Pass: ATM correctly rejected wrong PIN")
    else:
        print("Error: ATM accepted wrong PIN")
        
    print("\n--- Test Case #9 : Exceed Daily Limit (Expect Error) ---")
    # Harry ถอนไปแล้ว 0, โอน 10000 (นับรวม) = ใช้ไป 10000
    # Limit = 40000. ลองถอนอีก 35000 (รวมเป็น 45000) ต้อง Error
    try:
        print("Attempting to withdraw 35,000 (Total daily: 45,000)...")
        harry_account.withdraw(atm_machine1, 35000)
        print("Error: Daily limit exceeded but not caught")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

    print("\n--- Test Case #10 : ATM Insufficient Cash (Expect Error) ---")
 
    poor_atm = ATM_machine('9999', 100) 
    scb.add_atm_machine(poor_atm)
    try:
        print("Attempting to withdraw 500 from ATM with 100 THB...")
        harry_account.withdraw(poor_atm, 500)
        print("Error: ATM insufficient cash but not caught")
    except Exception as e:
        print(f"Pass: System correctly raised error -> {e}")

if __name__ == "__main__":
    run_test()