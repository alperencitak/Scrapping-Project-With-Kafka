from kafka import KafkaConsumer
import json
import os


# Kafkadaki topicleri çekip json formatında bir dosyaya yazan fonksiyon
def consume_and_save():
    os.makedirs('/app/data', exist_ok=True)

    consumer = KafkaConsumer(
        'scraped_products',
        bootstrap_servers='kafka-server:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')), # json olarak çekiyoruz
        auto_offset_reset='earliest' # en başından beri almak için
    )

    products = []

    try:
        # Her bir mesaj products listesine atılıyor. Liste 16 elemana ulaşınca json dosyasına yazıyoruz.
        for message in consumer:
            products.append(message.value)

            if len(products) % 16 == 0:
                with open('/app/data/products.json', 'w') as f:
                    json.dump(products, f, indent=2)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Verilerin yazılıp yazılmadığı son kez kontrol ediliyor.
        with open('/app/data/products.json', 'w') as f:
            json.dump(products, f, indent=2)
        consumer.close() # Consumeri kapatıyoruz.


if __name__ == "__main__":
    consume_and_save()
