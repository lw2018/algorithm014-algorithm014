学习笔记

双向BFS


front = {start}
    back = {end}
    visited = set()
    while front and back:
        #后面要搜索的值放在里面
        next_front = set()
        #根据front里面的结点推算出下一层的结点
        new_node = generate_realted_nodes(front)
        if new_node in back:
            return # 2边相遇 搜索结束
        #否则继续搜索 
        next_front.add(new_node)
        visited.add(new_node)

        front = next_front

        #总是从结点数更少的一边开始搜索  这一边总是指向变量front
        if len(front) > len(back):
            front , back = back ,front