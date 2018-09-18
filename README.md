# GeoLite-City

This is the Maxmind Geo Lite City data and stored as the file GeoLiteCity.dat. It is intended for testing purposes with packages like geoip-stream and so the data may become stale and hence it is recommended fresh data be obtained from [Maxmind GeoLiteCity](https://dev.maxmind.com/zh-hans/geoip/legacy/geolite/).

GeoLite 数据库是我们的免费数据库. 数据库在每个月的第一个星期二更新。 免费数据库的格式与收费数据库相同。 任何可以读取GeoIP付费数据库的代码都可以读取我们的免费数据库。

我们将从 2018 年 4 月 1 日起停止更新 GeoLite Legacy 数据库。直到 2019 年 1 月 2 日为止，您都可以继续下载 2018 年 4 月发布的版本。GeoLite Legacy 用户需要更新他们的集成，以便在 2018 年 4 月之前转到免费的 GeoLite2 数据库或商用的 GeoIP 数据库。

此外，GeoLite2 数据库中的经纬度坐标信息将在 2019 年删除。*GeoIP2 数据库则会继续提供经纬度坐标信息。

Pure Python GeoIP API  https://github.com/appliedsec/pygeoip  不过不在更新维护了

数据库下载   https://dev.maxmind.com/zh-hans/geoip/geoip2/geolite2/

最新的python api geoip https://github.com/maxmind/GeoIP2-python  提供python接口，以及示例

c版本的 使用  https://github.com/maxmind/libmaxminddb
