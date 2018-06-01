TOKEN = 'TOKEN'
use_proxy = False
proxy = 'https://localhost:1080/'
# proxy with auth is not tested
proxy_username, proxy_password = None, None
if use_proxy:
    request_kw = { 'proxy_url': proxy }
    if proxy_username != None:
        from telegram.vendor.ptb_urllib3.urllib3 import make_headers
        request_kw['urllib3_proxy_kwargs'] = { 'headers':make_headers(proxy_basic_auth=proxy_username+':'+proxy_password)}
else:
    request_kw = None