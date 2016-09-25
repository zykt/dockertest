import pymongo
import redis

# set up database clients
m = pymongo.MongoClient('mongo', 27017)
mdb = m.db
r = redis.StrictRedis(host='redis', port=6379)

# check for first launch
if not mdb.posts.find_one({'FirstLaunch': True}):
    print('first time detected: creating data')
    mdb.posts.insert_one({'FirstLaunch': True})
    mdb.posts.insert_one({'action': 'Hello',
                          'result': 'World'})
    r.set('Hello', 'World')

mongo_res = mdb.posts.find_one({'action': 'Hello'})
redis_res = r.get('Hello')

print('data found:')
print('mongodb says\n    {}'.format(mongo_res))
print('resdis says\n    {}'.format(redis_res))
