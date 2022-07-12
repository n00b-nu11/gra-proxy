#!/usr/bin/python3

from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow) -> None:
    if flow.request.method == "POST" and flow.request.pretty_url == "https://api.gravity.place/gravity/inbox/addFootprint":
        ctx.log.info("addFootprint is trapped")
        flow.kill()
