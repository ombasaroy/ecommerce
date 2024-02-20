from .cart import Cart


# Create a context processor so that our cart can work on all pages
def cart(request):
    # return all the default data from our cart
    return {'cart': Cart()}

#The next step is telling django that our context_processors exists, We
# do that in the settings.py file in our project

