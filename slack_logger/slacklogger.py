from typing import Optional,List,Any,Dict,Union
import aiohttp
import asyncio
import requests
class SlackLogger:
    def __init__(self,webhook:Optional[str]=None,token:Optional[str]=None) -> None:
        """:param pass the webhook url
            token support will come soon"""
        self._webhook = webhook
        self._token = token
    def sync_post_slack(self,message:str) -> int:
        """
        :param message you need to send in string format
        :response status code for your request
        """
        
        
    