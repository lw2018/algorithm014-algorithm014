学习笔记
关于hashMap 对java语言不熟悉，凭着其它语言的了解 大概看了其结构

Node有4种属性 key value就存在其中。所以hashMap的put get 应该是基于Node的这种结构来操作
static class Node<K,V> implements Map.Entry<K,V> 
        final int hash;
        final K key;
        V value;
        Node<K,V> next;


put()方法用到的一个实现函数
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab; Node<K,V> p; int n, i;

        如果存放的table表不存在或为空 则初始化一个
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;

        如果最后一个索引位置上为NULL.则直接调用newNode()把 key value放进去
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
           
            hash相同 key相同
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;


            p 为treeNode的处理
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {

                hash相同 key不同的处理 将其放在next w为Null的位置
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            key hash相同 更新其value
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
