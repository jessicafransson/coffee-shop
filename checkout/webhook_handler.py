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
