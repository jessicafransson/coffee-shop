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
            content=f'Webhook recieved: {event["type"]}',
        status=200)
