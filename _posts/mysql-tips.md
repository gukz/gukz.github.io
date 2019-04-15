# 关于mysql你需要知道的
## 数据库的事物的使用场景
```python
with pwdb.database.transaction():
    referrer_open_id = get_user_open_id(er_user_id)
    referral = Referral.create(
        referee_user_id=ee_user_id,
        referee_open_id=ee_openid,
        referrer_user_id=er_user_id,
        referrer_open_id=referrer_open_id
    )
    ReferralLock.create(referee_open_id=ee_openid,
                        referral_id=referral.id)
    ReferralRank.get_or_create(referrer_user_id=er_user_id)
    push_accept_message_to_referee.delay(ee_openid, er_user_id)
    push_accept_message_to_referrer.delay(
        referrer_open_id, ee_user_id)
    if ee_user_id:
        send_reward_to_referee.delay(referral.id, ee_user_id)
```
## sharding的表的数据迁移方法
1, 模拟用户查询，遍历所有用户id
2, 获取所有的数据库，遍历每一个数据库
### 需要注意的问题
1, 如何保证幂等性
2, 对效率的需求如何

## 高性能mysql书籍

[mysql逻辑架构](IMG1)

- B-Tree

- B+Tree
