import requests
# url='http://123.60.30.21:3000/rest/user/login'
# json_data={"email":"wang@qq.com","password":"123456"}
# res = requests.post(url,json=json_data)
# token=res.json()['authentication']['token']
#
# bask_url='http://123.60.30.21:3000/api/BasketItems/'
# bask_data={"ProductId":67,"BasketId":"18","quantity":1}
# headers={
#     'Authorization': 'Bearer '+token,
# }
# res_bask=requests.request(method='POST',url=bask_url,json=bask_data,headers=headers)
# print(res_bask.text)
def test_login_addbask_session():
    s=requests.session()
    url = 'http://123.60.30.21:3000/rest/user/login'
    json_data = {"email": "wang@qq.com", "password": "123456"}
    res=s.request(method='POST', url=url, json=json_data)
    token = res.json()['authentication']['token']
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    bask_url = 'http://123.60.30.21:3000/api/BasketItems/'
    bask_data = {"ProductId": 9, "BasketId": "18", "quantity": 1}
    res_bask = s.request(method='POST', url=bask_url, json=bask_data,headers=headers)
    print(res_bask.text)





