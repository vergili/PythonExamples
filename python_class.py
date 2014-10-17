class Restaurant(object):
    bankrupt = False
    
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()

print x.bankrupt

y = Restaurant()

y.bankrupt = True

print y.bankrupt

