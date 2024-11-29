import json
import random
from pprint import pprint

import redis


class RedisCient():
    def __init__(self,type,website):
        try:
            # 连接到 Redis 服务
            self.db = redis.StrictRedis(host='localhost', port=6379, db=0)

            # 执行 PING 命令检查连接
            if self.db.ping():
                print("连接成功！")
            else:
                print("连接失败！")
        except Exception as e:
            print(f"连接 Redis 时出错: {e}")

        self.type = type
        self.website = website

    def h_name(self):
        return f'{self.type}:{self.website}'

    def h_set(self, username, value):
        self.db.hset(self.h_name(), username, value)

    def h_get(self, username):
        return self.db.hget(self.h_name(), username)

    def h_random(self):
        return random.choice(self.db.hvals(self.h_name()))

    def h_all(self):
        """

        :return: all key-values
        """
        return self.db.hgetall(self.h_name())
if __name__ == '__main__':
    redisClinet = RedisCient('account','antispider6')
    print(redisClinet.h_name())
    redisClinet.h_set('admin1', 'password1')
    redisClinet.h_set('admin2', 'password2')
    redisClinet.h_set('admin3', 'password3')
    redisClinet.h_set('admin4', 'password4')
    print(type(redisClinet.h_get('admin')))
    print(redisClinet.h_get('admin').decode())

    print(redisClinet.h_random().decode())

    pprint(redisClinet.h_all())

