#Code a chatbot that uses tensorflow and learn to converse in python

import tensorflow as tf
from sklearn.model_selection import train_test_split



# Define the parameters for the chatbot
learning_rate = 0.01
training_epochs = 100
display_step = 1

# Define the size of the training data
train_x, train_y = train_x.shape

# Define the size of the test data
test_x, test_y = test_x.shape

# Define the placeholders for the inputs and labels
x = tf.placeholder(tf.float32, [None, train_x])
y = tf.placeholder(tf.float32, [None, train_y])

# Define the weights and biases
W = tf.Variable(tf.zeros([train_x, train_y]))
b = tf.Variable(tf.zeros([train_y]))

# Construct the model
pred = tf.nn.softmax(tf.matmul(x, W) + b)

# Minimize the error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))

# Use gradient descent to optimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Train the model
    for epoch in range(training_epochs):
        avg_cost = 0.
        _, c = sess.run([optimizer, cost], feed_dict={x: train_x, y: train_y})
        # Compute the average loss
        avg_cost += c/train_x
        # Display the progress
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Training complete!")

    # Test the model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate the accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({x: test_x, y: test_y}))