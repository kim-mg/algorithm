import sys
input = sys.stdin.readline

###########################################################
# time out
headers = {
	'Accept': 'text/plain',
	'Content-Length': 348,
	'Host': 'http//mingrammer.com'
}

def pre_process(**headers):
	content_length = headers['Content-Length']
	print('content_length: ', content_length)

	host = headers['Host']
	if 'https' not in host:
		raise ValueError('You must use SSL for http communication')

if __name__ == "__main__":
	# print(**headers)
	pre_process(headers)