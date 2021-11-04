import stripe
from stripe.api_resources.account import Account
stripe.api_key = "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"

account = stripe.Account.create(
  country='CA',
  type='express',
  capabilities={
    'transfers': {
      'requested': True,
    },
  },
  tos_acceptance={
    'service_agreement': 'recipient',
  },
 
  )
