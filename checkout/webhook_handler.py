from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handling the stripe webooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Here to handle generic, unknown or unexpected webhook events
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Here to handle payment intent success webhook
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Here to handle payment intent failed webhook
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
