#--*--coding=utf-8--*--
#use:  http://127.0.0.1:8010/?ip=116.211.92.56
#res: 
""""""
{
"country_name": "China",
"city": "Wuhan",
"region_code": "12",
"longitude": 114.27339999999998,
"latitude": 30.580099999999987
}
""""""

import pygeoip,re,json
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from urlparse import urlparse
__version__='1.0'
gi = pygeoip.GeoIP('GeoLiteCity.dat')

class GeoHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.do_GET()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=UTF-8")

        if '?' in self.path:
            self.getip(self.path)
        else:
            content="{'status':'OK'}"
            self.send_header("Content-Length", len(str(content)))
            self.end_headers()
            self.wfile.write(content)

    def version_string(self):
        """Return the server software version string."""
        return "GeoServer/" + __version__

    def getip(self,path):
        try:
            ip=""
            url = urlparse(path)
            print url.query
            ip=url.query.replace("ip=","")
            if ipFormatChk(ip)==False:
                content="{'status':'invalid ip address'}"
                self.send_header("Content-Length", len(str(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            # 指定返回编码
            enc = "UTF-8"
            #tgt = '183.141.110.72'
            return_data=printRecord(ip)
            content=json.dumps(return_data)
            content = content.encode(enc)
            self.send_header("Content-Length", len(str(content)))
            self.end_headers()
            self.wfile.write(content)
        except SyntaxError as e:
            pass


def ipFormatChk(ip_str):
   pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
   if re.match(pattern, ip_str):
      return True
   else:
      return False

def printRecord(tgt):
    rec = gi.record_by_addr(tgt)

    data={}

    city =data['city']= rec['city']
    region =data['region_code']= rec['region_code']
    country =data['country_name']= rec['country_name']
    long =data['longitude']= rec['longitude']
    lat =data['latitude']= rec['latitude']

    print '[*] 主机: ' + tgt + ' Geo-located.'
    print '[+] ' + str(city) + ', ' +str(region)+', '+str(country)
    print '[+] 经度: '+str(lat)+', 维度: '+ str(long)

    return data


if __name__=="__main__":

    PORT = 8010
    Handler = GeoHTTPRequestHandler
    httpd = HTTPServer(("localhost", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()
