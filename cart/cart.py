def Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current key if it exixts
        cart = self.session.get('session_key')

        # if the user is new, create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Always make sure that the shopping cart works on all pages of the website using the code below
        self.cart = cart
