# 消费者

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


# 回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 确定监听队列
channel.basic_consume(queue='hello',
                      auto_ack=True,  # 默认应答
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()