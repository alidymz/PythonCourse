#!/usr/bin/env python
# coding: utf-8

# In[773]:


## HW1 ## 
import numpy as np


# In[778]:


class Portfolio():
    
    def __init__(self, owner = 'Ali DUYMAZ'):
        self.owner = owner
        self.stock={}
        self.mutualFund={}
        self.cash=0.0
        self.allTransactions=  ['\n**ALL TRANSACTIONS**\n']

        
    def history(self):
        
        for transaction in self.allTransactions:
            print(transaction) 
    
        
    
    def addCash(self,amount):
        self.cash+=amount
        self.allTransactions.append('Added Cash Amount is $'+str(amount)+' '+'Total cash is $'+str(round(self.cash,2)))
        
    def withdrawCash(self,amount):
        self.cash-=amount
        self.allTransactions.append('Withdrew Cash Amount is $'+str(amount)+' '+'Total cash is $'+str(round(self.cash,2)))
    
    def buyStock(self,numShares,stock_instance):
        self.cash -= stock_instance.buyShare(numShares)*stock_instance.stockPrice
        self.stock[stock_instance.stockName] = stock_instance.numShares
        ##self.allTransactions.append('Total Cash Amount is $'+str(self.cash))
        self.allTransactions.append("# of shares {} purchased is {} ".format(stock_instance.stockName,numShares)
                                    +' '+'Total cash is $'+str(round(self.cash,2)))
    
    def sellStock(self,stock_instance,numShares):
        if stock_instance == "HFH":
            self.cash += s.sellShare(numShares)*s.stockPrice*np.random.uniform(0.5,1.5)
            self.stock[s.stockName] -= numShares
            ##self.allTransactions.append('Total Cash Amount is $'+str(self.cash))
            self.allTransactions.append("# of shares {} sold is {} ".format(stock_instance,numShares)
                                        +' '+'Total cash is $'+str(round(self.cash,2)))
        
        
    def buyMutualFund(self,numShares,fundInstance):
        self.cash-=fundInstance.buyFund(numShares)
        self.mutualFund[fundInstance.fundName] = fundInstance.numFunds
        ##self.actionsLog.append('Total Cash Amount is $'+str(self.cash))
        self.allTransactions.append("# of mutual fund {} purchased is {} ".format(fundInstance.fundName,numShares)
                                    +' '+'Total cash is $'+str(round(self.cash,2)))
        
    def sellMutualFund(self,any_fund,numofFund):
        
        if any_fund == "BRT":
            self.cash+=mf1.sellFund(numofFund)
            self.mutualFund[mf1.fundName] -= numofFund
            self.allTransactions.append("# of mutual fund {} sold is {} ".format(mf1.fundName,numofFund)+' '
                                        +'Total cash is $'+str(round(self.cash,2)))
    
        if any_fund == "GHT":
            self.cash+=mf2.sellFund(numofFund)
            self.mutualFund[mf2.fundName] -= numofFund
            self.allTransactions.append("# of mutual fund {} sold is {} ".format(mf2.fundName,numofFund)+' '
                                        +'Total cash is $'+str(round(self.cash,2)))
             
    def __str__(self):

        portfolio1 = '**Ali DUYMAZ Portfolio**\ncash:                 '+'$'+' '+str(self.cash)+'\n'

        for index,item in self.stock.items():
            portfolio1 += 'stock:                '+str(item)+' '+str(index)+'\n'

        portfolio1 += 'mutual funds:         '

        for index,item in self.mutualFund.items():
            portfolio1 +=str(item)+' '+str(index)+'\n'+'                      '

        return portfolio1


# In[779]:


class Stock(Portfolio):
    
    def __init__(self,stockPrice,stockName):
        
        self.stockPrice=stockPrice
        self.stockName=stockName
        self.numShares=0
        self.numSellShares = 0
    
    def buyShare(self,numShare):
        self.numShares+=numShare
        return self.numShares
    
    def sellShare(self,numShare):
        self.numSellShares+=numShare
        return self.numSellShares
        
    


# In[780]:


class MutualFund(Portfolio):
    
    def __init__(self,fundName):
        self.fundName = fundName
        self.numFunds = 0.0
        self.numSellFunds = 0.0
        
    def buyFund(self,numFund):
        self.numFunds += numFund
        return self.numFunds
    
    def sellFund(self,numFund):
        self.numSellFunds+=numFund*np.random.uniform(0.9,1.2)
        return self.numSellFunds
    


# In[781]:


portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
#              2 GHT
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions
#ordered by time


# In[782]:


portfolio.owner

