# kube-config
### 本地配置 ~/.kube/config
```yml
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority: /Users/guk/gitstore/usercsrs/shanbay-it.crt
        server: https://106.15.162.76:6443
      name: it
    
    - cluster:
        certificate-authority: /Users/guk/gitstore/usercsrs/shanbay-stag.crt
        server: https://47.99.2.221:6443
      name: stag
    
    - cluster:
        certificate-authority: /Users/guk/gitstore/usercsrs/shanbay-pro.crt
        server: https://101.37.113.69:6443
      name: pro
    
    contexts:
    - context:
        cluster: it
        user: wanggang-it
        namespace: cuckoo
      name: it
    - context:
        cluster: stag
        user: wanggang-stag
        namespace: cuckoo
      name: stag
    - context:
        cluster: pro
        user: wanggang
        namespace: cuckoo
      name: pro
    
    current-context: pro
    kind: Config
    preferences: {}
    
    users:
    - name: wanggang
      user:
        client-certificate: /Users/guk/gitstore/usercsrs/pro-cuckoo.crt
        client-key: /Users/guk/gitstore/usercsrs/my.key
    - name: wanggang-stag
      user:
        client-certificate: /Users/guk/gitstore/usercsrs/stag-cuckoo.crt
        client-key: /Users/guk/gitstore/usercsrs/my.key
    - name: wanggang-it
      user:
        client-certificate: /Users/guk/gitstore/usercsrs/it-cuckoo.crt
        client-key: /Users/guk/gitstore/usercsrs/my.key
```
其中crt生成方式：`echo -n '秘钥字符串'|base64 -D > target.crt`

### kubectl 常用指令
+ kubectl delete pod xxxxxx --force --grace-period 0 
作用: 当前pod状态异常, 删除当前pod并且依照replicats规则创建
+ kubectl config get-contexts
作用: 获取所有集群
+ kubectl config use-context xxxxxx
作用: 切换集群
+ kubectl scale --replicas=1 deploy xxxxxx
作用: 修改某个deploy的数量(在线修改pod的数量)
+ kubectl exec xxxxxx -ti sh
作用: 建立一个新的命令行与当前pod进行交互
