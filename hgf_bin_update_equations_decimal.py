# update equations #

from decimal import *
getcontext().prec = 8

from math import *
# List of Terms #

def s(mu_2):

        if (mu_2 > 400): 
                mu_2 = 400
        elif (mu_2 < (-400)):
                mu_2 = -400

                
                
        mu_2 = Decimal(mu_2)
        #print ("mu_2 is")
        #print (mu_2)
        ans = ( 1/ (1+exp(-(mu_2))) )
        #print ("s")
        #print (ans)
        return ans

def sig_hat_1_k_calc(mu_hat_1_k_min_1):

        
        mu_hat_1_k_min_1 = Decimal(mu_hat_1_k_min_1)
        sig_hat_1 = (mu_hat_1_k_min_1)*(1- mu_hat_1_k_min_1)
        # double check subtraction, 2 or 1?  #
        return sig_hat_1


def sig_hat_2_k_calc (sig_2_k_min_1,  mu_3_k_min_1, ka, om):


        sig_2_k_min_1   = Decimal(sig_2_k_min_1)
        mu_3_k_min_1    = Decimal(mu_3_k_min_1)
        ka              = Decimal(ka)
        om              = Decimal(om)

        if ((ka*mu_3_k_min_1 + om) > 400):  # to deal with math range overflow error
                kludge = 400
        elif ((ka*mu_3_k_min_1 + om) < (-400)):
                kludge = -400
        else:
                kludge = (ka*mu_3_k_min_1 + om)
        
        sig_hat_2 = sig_2_k_min_1 + Decimal(exp(kludge))

        #print ("mu_3_k_min_1 is")
        #print (mu_3_k_min_1)
        #print ("sig_2_k_min_1 is")
        #print (sig_2_k_min_1)
        #print ("sig_hat_2 is ")
        #print (sig_hat_2)
        #print ("\n \n")

        sig_hat_2 = Decimal(sig_hat_2)
        return sig_hat_2

    

def sig_2_k_calc(sig_hat_2_k, sig_hat_1_k):

        sig_hat_2_k = Decimal(sig_hat_2_k)
        sig_hat_1_k = Decimal(sig_hat_1_k)

        
        sig_2 = 1/((1/sig_hat_2_k) + sig_hat_1_k)

        sig_2 = Decimal(sig_2)
        return sig_2



def update_mu_2 (mu_2_k_min_1, sig_2_k, mu_1_k):  #mu_1_k is actual observation"

        mu_2_k_min_1    = Decimal(mu_2_k_min_1)
        sig_2_k         = Decimal(sig_2_k)
        mu_1_k          = Decimal(mu_1_k)
        
        mu_2_k = mu_2_k_min_1 +  ( sig_2_k * (mu_1_k - Decimal(s(mu_2_k_min_1))  ) )

        mu_2_k = Decimal(mu_2_k)
        
        return mu_2_k


def update_mu_3 (mu_3_k_min_1, sig_3_k, sig_2_k_min_1, ka, om, sig_2_k, mu_2_k,
                 mu_2_k_min_1):


        mu_3_k_min_1    = Decimal(mu_3_k_min_1)
        sig_3_k         = Decimal(sig_3_k )
        sig_2_k_min_1   = Decimal(sig_2_k_min_1)
        ka              = Decimal(ka )
        om              = Decimal(om )
        sig_2_k         = Decimal(sig_2_k)
        mu_2_k          = Decimal( mu_2_k )
        mu_2_k_min_1    = Decimal(mu_2_k_min_1)


        if ((ka*mu_3_k_min_1 + om) > 400):   # to deal with math range overflow error
                kludge = 400
        elif ((ka*mu_3_k_min_1 + om) < (-400)):
                kludge = -400
                
        else:
                kludge = (ka*mu_3_k_min_1 + om)
    
        pred_k_min_1 = mu_3_k_min_1
        
        rate = (sig_3_k *
                         Decimal((ka/2))*
                        ( Decimal(exp(kludge))/
                                (  sig_2_k_min_1 +
                                   Decimal(exp(kludge))    ))
                          )                



        pred_error = (
                        (
                        (sig_2_k + Decimal((mu_2_k - mu_2_k_min_1)**2)  )  )
                        /
                        (sig_2_k_min_1 + Decimal(exp(kludge) ) ) -
                        Decimal(1)     )

        mu_3_k = pred_k_min_1 + (rate * pred_error)

        mu_3_k = Decimal(mu_3_k)

        return mu_3_k
    



#use the update equations to derive new estimates for mu3 and mu2?
#Either plug mu2 directly into sig to generate prediction
# or somehow plug ino original generative model? (Not really)
# equation 27 connects level three to level 2 by way of estimating sig_2

#check division, ints v. floats etc.


