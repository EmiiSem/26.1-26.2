import stripe
stripe.api_key = "sk_test_51OlWIPH7oiewvnTBVQDI6gsybpaqeFCLVYcIbQDroJhm11QHxqAgthPxApZJBFLojK6UwCBtQZgY1iWCVO5Y6F4K00kjNVHkNg"

stripe.PaymentIntent.modify(
  "pi_3MtwBwLkdIwHu7ix28a3tqPa",
  metadata={"order_id": "6735"},
)