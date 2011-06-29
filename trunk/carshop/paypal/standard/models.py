#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from paypal.standard.helpers import duplicate_txn_id, check_secret
from paypal.standard.conf import RECEIVER_EMAIL, POSTBACK_ENDPOINT, SANDBOX_POSTBACK_ENDPOINT


class PayPalStandardBase(models.Model):
    """Meta class for common variables shared by IPN and PDT: http://tinyurl.com/cuq6sj"""

    business = models.CharField(max_length=127, blank=True, help_text="Email where the money was sent.")
    charset=models.CharField(max_length=32, blank=True)
    custom = models.CharField(max_length=255, blank=True)
    notify_version = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)

    receiver_email = models.EmailField(max_length=127, blank=True)
    receiver_id = models.CharField(max_length=127, blank=True)  # 258DLEHY2BDK6
    residence_country = models.CharField(max_length=2, blank=True)
    test_ipn = models.BooleanField(default=False, blank=True)
    txn_id = models.CharField("Transaction ID", max_length=19, blank=True, help_text="PayPal transaction ID.")
    txn_type = models.CharField("Transaction Type", max_length=128, blank=True, help_text="PayPal transaction type.")
    verify_sign = models.CharField(max_length=255, blank=True)    
    
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    payer_email = models.CharField(max_length=127, blank=True)
    payer_id = models.CharField(max_length=13, blank=True)
    
    invoice = models.CharField(max_length=127, blank=True)
    item_name = models.CharField(max_length=127, blank=True)
    item_number = models.CharField(max_length=127, blank=True)
    mc_currency = models.CharField(max_length=32, default="USD", blank=True)
    mc_fee = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    mc_gross = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)

    payer_status = models.CharField(max_length=10, blank=True)
    payment_date = models.DateTimeField(blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    payment_fee = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    payment_gross = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    payment_status = models.CharField(max_length=9, blank=True)
    payment_type = models.CharField(max_length=7, blank=True)
    pending_reason = models.CharField(max_length=14, blank=True)
    protection_eligibility=models.CharField(max_length=32, blank=True)
    quantity = models.IntegerField(blank=True, default=1, null=True)
    shipping = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    tax = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    handling_amount = models.DecimalField(max_digits=64, decimal_places=2, default=0, blank=True, null=True)
    transaction_subject = models.CharField(max_length=255, blank=True)
    
    CONTEXT = models.CharField(max_length=62, blank=True)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        if self.is_transaction():
            return self.format % ("Transaction", self.txn_id)
        else:
            return self.format % ("Recurring", self.recurring_payment_id)
        
    def is_transaction(self):
        return len(self.txn_id) > 0

    def is_recurring(self):
        return len(self.recurring_payment_id) > 0
    
    def is_subscription_cancellation(self):
        return self.txn_type == "subscr_cancel"
    
    def is_subscription_end_of_term(self):
        return self.txn_type == "subscr_eot"
    
    def is_subscription_modified(self):
        return self.txn_type == "subscr_modify"
    
    def is_subscription_signup(self):
        return self.txn_type == "subscr_signup"
    
    def set_flag(self, info, code=None):
        """Sets a flag on the transaction and also sets a reason."""
        self.flag = True
        self.flag_info += info
        if code is not None:
            self.flag_code = code
        
    def verify(self, item_check_callable=None):
        """
        Verifies an IPN and a PDT.
        Checks for obvious signs of weirdness in the payment and flags appropriately.
        
        Provide a callable that takes an instance of this class as a parameter and returns
        a tuple (False, None) if the item is valid. Should return (True, "reason") if the
        item isn't valid. Strange but backward compatible :) This function should check 
        that `mc_gross`, `mc_currency` `item_name` and `item_number` are all correct.

        """
        self.response = self._postback()
        self._verify_postback()  
        if not self.flag:
            if self.is_transaction():
                if self.payment_status != "Completed":
                    self.set_flag("Invalid payment_status. (%s)" % self.payment_status)
                if duplicate_txn_id(self):
                    self.set_flag("Duplicate txn_id. (%s)" % self.txn_id)
                if self.receiver_email != RECEIVER_EMAIL:
                    self.set_flag("Invalid receiver_email. (%s)" % self.receiver_email)
                if callable(item_check_callable):
                    flag, reason = item_check_callable(self)
                    if flag:
                        self.set_flag(reason)
            else:
                # @@@ Run a different series of checks on recurring payments.
                pass
        
        self.save()
        self.send_signals()

    def verify_secret(self, form_instance, secret):
        """Verifies an IPN payment over SSL using EWP."""
        if not check_secret(form_instance, secret):
            self.set_flag("Invalid secret. (%s)") % secret
        self.save()
        self.send_signals()

    def get_endpoint(self):
        """Set Sandbox endpoint if the test variable is present."""
        if self.test_ipn:
            return SANDBOX_POSTBACK_ENDPOINT
        else:
            return POSTBACK_ENDPOINT

    def initialize(self, request):
        """Store the data we'll need to make the postback from the request object."""
        self.query = getattr(request, request.method).urlencode()
        self.ipaddress = request.META.get('REMOTE_ADDR', '')

    def send_signals(self):
        """After a transaction is completed use this to send success/fail signals"""
        raise NotImplementedError
        
    def _postback(self):
        """Perform postback to PayPal and store the response in self.response."""
        raise NotImplementedError
        
    def _verify_postback(self):
        """Check self.response is valid andcall self.set_flag if there is an error."""
        raise NotImplementedError