import stripe
stripe.api_key = "sk_test_51OlWIPH7oiewvnTBVQDI6gsybpaqeFCLVYcIbQDroJhm11QHxqAgthPxApZJBFLojK6UwCBtQZgY1iWCVO5Y6F4K00kjNVHkNg"

stripe.PaymentIntent.search(query="amount>1000")