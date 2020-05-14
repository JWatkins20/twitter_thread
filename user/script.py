import twitter

access_token = "1259561263321006080-ij0GgVG6IQObBtOnZboFvYN0BQy2rF"
access_token_secret = "VK0MM7iBlfyRsPIgwgJoFQzi8xUzKZNkBiCupaMS3gPCX"
text = "ll legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives. Section 2 The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature. No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State in which he shall be chosen. Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons. The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to choose three, Massachusetts eight, Rhode Island and Providence Plantations one, Connecticut five, New York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five and Georgia three. When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue Writs of Election to fill such Vacancies. The House of Representatives shall choose their Speaker and other Officers; and shall have the sole Power of Impeachment."
def posttweets(user, text):
	api = twitter.Api(consumer_key='ThbUXe9Wlk5ipSfPSDfZ6Fs7G',
					  consumer_secret='xE9saubR7fXfWtVDtup7eKsA8dldyH553t9ocHtyojDsKcj9O7',
					  access_token_key=access_token,
					  access_token_secret=access_token_secret)

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

posttweets("bruh", text)
# text = "The brown fox jumped over the moon"
# api = twitter.Api(consumer_key='ThbUXe9Wlk5ipSfPSDfZ6Fs7G',
# 					  consumer_secret='xE9saubR7fXfWtVDtup7eKsA8dldyH553t9ocHtyojDsKcj9O7',
# 					  access_token_key=access_token,
# 					  access_token_secret=access_token_secret)
# print(api.PostUpdate(text))