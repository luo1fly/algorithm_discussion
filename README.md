# redis安装 #
下载：[官方压缩包](http://download.redis.io/releases/redis-3.2.3.tar.gz)，拷贝配置文件和启动脚本，配置文件简单修改
# 登录到redis的命令行 #
## 确保redis-server服务已经启动的情况下，执行： ##

    redis-cli -h host -p port
# 简单命令介绍 #
## SET命令插入一组键值对 ##
    127.0.0.1:6379> SET hello hehe
    OK
## GET命令获取某个key对应的value ##
    127.0.0.1:6379> GET hello
    "hehe"
## EXISTS命令查看是否存在对应key ##
    127.0.0.1:6379> EXISTS hello
    (integer) 1
    127.0.0.1:6379> EXISTS shabi
    (integer) 0
## KEYS命令获取对应名称的key，注意通配符的用法 ##
    127.0.0.1:6379> KEYS *
    1) "hello2"
    2) "hello"
    3) "hello1"
    127.0.0.1:6379> KEYS hello
    1) "hello"
    127.0.0.1:6379> KEYS hello?
    1) "hello2"
    2) "hello1"
    127.0.0.1:6379> KEYS hello*
    1) "hello2"
    2) "hello"
    3) "hello1"
## DEL命令删除一组键值对 ##
    127.0.0.1:6379> DEL hello
    (integer) 1
    127.0.0.1:6379> KEYS *
    1) "hello2"
    2) "hello1"
## TYPE命令查看对应key的value类型 ##
    127.0.0.1:6379> TYPE hello2
    string
### 由此可见，SET命令存放到redis空间的对象类型一定是字符串 ###

## INFO命令查看redis服务器信息 ##
    127.0.0.1:6379> INFO
    # Server
    redis_version:3.2.3
    redis_git_sha1:00000000
    redis_git_dirty:0
    redis_build_id:204fce05f9bdf18d
    redis_mode:standalone
	...

附件