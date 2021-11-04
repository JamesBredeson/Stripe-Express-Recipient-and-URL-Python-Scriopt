import stripe
stripe.api_key = "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"

account_links = stripe.AccountLink.create(
  account='acct_1JqTeZ2RoRUZKxEC',
  refresh_url='https://mox-technologies.com/reauth',
  return_url='https://mox-technologies.com.com/return',
  type='account_onboarding',
)

print (account_links)