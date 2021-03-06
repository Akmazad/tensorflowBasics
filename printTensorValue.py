import tensorflow as tf
sess = tf.InteractiveSession()
sess = tf.Session()

y_true = np.array([0, 0, 1, 1])
y_true1 = np.array([1, 0, 1, 1])

y_true = np.array([y_true,y_true1])
y_true = tf.cast(y_true, dtype = tf.float64)
y_true = tf.Variable(y_true)  
# print(y_true) doesn't show any value, only the type and shape

y_scores = np.array([0.1, 0.4, 0.35, 0.8])
y_scores = np.array([y_scores,y_scores])
y_scores = tf.cast(y_scores, dtype = tf.float64)
y_scores = tf.Variable(y_scores)
# print(y_scores) doesn't show any value, only the type and shape

_auc, _ = tf.metrics.auc(y_true, y_scores, updates_collections='update_ops')
_auc = tf.Variable(_auc)

sess.run(tf.global_variables_initializer())

print(sess.run(y_true))
print(sess.run(y_scores))
print(sess.run(_auc))
