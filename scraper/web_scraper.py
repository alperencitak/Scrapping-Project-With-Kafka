from bs4 import BeautifulSoup
import requests, json, time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def scrape_page():
    try:
        response = requests.get("https://scrapeme.live/shop/")
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for product in soup.select('li.product'):
            data = {
                "name": product.find('h2').text.strip(),
                "price": product.find('span', class_='price').text.strip(),
                "image": product.find('img')['src']
            }
            products.append(data)
            producer.send('scraped_products', value=data)
            print(f"Sent: {data}")

        return products
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return []
    finally:
        producer.flush()
        producer.close()


if __name__ == "__main__":
    scrape_page()
