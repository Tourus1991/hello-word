# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()

with tf.Session() as sess:
    with tf.device("/gpu:0"):
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.],[2.]])
        product = tf.matmul(matrix1, matrix2)
        print sess.run(product)
state = tf.Variable(0, name="counter")
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)
    print sess.run(state)
# 运行 op, 更新 'state', 并打印 'state'
    for _ in range(3):
        sess.run(update)
        print sess.run(state)