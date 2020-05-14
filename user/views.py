from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from .models import *
from django.conf import settings
import oauth2 as oauth
import urllib.parse
import twitter

@login_required
def home(request):
	current_user = request.user

	form = ThreadForm(request.POST)
	if not request.user.post_permissions:
		return render(request, 'core/permissions.html')
	if request.method == 'POST':
		if form.is_valid():
			text = form.cleaned_data['text']
			new_thread = Thread(text=text)
			posttweets(current_user, text)
			new_thread.save()
			current_user.threads.add(new_thread)

			return HttpResponseRedirect('/',  RequestContext(request))
	else:
		form = ThreadForm()

	return render(request, 'core/home.html', {'form': form})

@login_required
def threeleggedauth1(request):
	request_token_url = 'https://api.twitter.com/oauth/request_token'
	authorize_url = 'https://api.twitter.com/oauth/authorize'
	callback = settings.BASE_URL + "posting-approved"

	consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
	client = oauth.Client(consumer)

	resp, content = client.request(request_token_url, "POST", body=urllib.parse.urlencode({'oauth_callback': callback}))

	request_token = dict(urllib.parse.parse_qsl(content.decode("utf-8")))

	request.user.request_token = request_token['oauth_token']
	request.user.request_token_secret = request_token['oauth_token_secret']
	request.user.save()

	user_auth_url = "{0}?oauth_token={1}".format(authorize_url, request_token['oauth_token'])

	return HttpResponseRedirect(user_auth_url)

@login_required
def threeleggedauth2(request):

	oauth_verifier = request.GET.get('oauth_verifier')
	access_token_url = 'https://api.twitter.com/oauth/access_token'

	request_token = request.user.request_token
	request_token_secret =  request.user.request_token_secret
	consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
	token = oauth.Token(request_token, request_token_secret)
	token.set_verifier(oauth_verifier)
	client = oauth.Client(consumer, token)

	resp, content = client.request(access_token_url, "POST")
	access_token = dict(urllib.parse.parse_qsl(content.decode("utf-8")))

	request.user.access_token = access_token['oauth_token']
	request.user.access_token_secret = access_token['oauth_token_secret']
	request.user.post_permissions = True
	request.user.save()

	return HttpResponseRedirect('/', RequestContext(request))





def posttweets(user, text):
	messages = []
	api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
					  consumer_secret=settings.TWITTER_CONSUMER_SECRET,
					  access_token_key=user.access_token,
					  access_token_secret=user.access_token_secret)

	if len(text) > 280:
		last_id = -1
		while 280 < len(text):
			if(280 >= len(text)):
				break

			end = text[277:281]
			resp = api.PostUpdate(text[:277] + '...', in_reply_to_status_id=last_id)
			last_id = resp.id
			text = end + text[281:]

		api.PostUpdate(text, in_reply_to_status_id=last_id)
	else:
		api.PostUpdate(text)

	return messages
