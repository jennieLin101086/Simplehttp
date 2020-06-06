from urllib.parse import urlparse,urlunparse
import sys,traceback,json



response = {'args':{}}

#更新回傳的response
def update_response(key='',value='', data={}):    
    if key != '' or value != '':
        response['args'].update({key:value})
    if len(data) > 0:
        response['json'] = json.dumps(data)
    return response  


#分解query字串
def split_query(url):     
        query = urlparse(url).query.split('=')
        query_key = query[0]
        query_value = query[1]
        return update_response(query_key, query_value)
    
#分解參數
def split_params(params={},data={}):
    if len(data) > 0:
        update_response(data=data) 
    if len(params) > 0:
        for key,value in params.items():
            update_response(key, value)

    return response


#判斷是否有參數
def parse(url,params):
    if urlparse(url).query != '':
        split_query(url)
    if params != None:
        split_params(params)
    return response


def get_json(url, params):
    if '?' not in url:
        return response
    else:
        return parse(url,params)
    
def post_json(url, params, data):
    if params != None:
        split_params(params=params)
    if len(data) > 0:
        split_params(data=data)
    return response


