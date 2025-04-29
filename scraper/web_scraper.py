from bs4 import BeautifulSoup
import requests, json, time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka-server:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


# Verilen siteden ilk sayfadaki listeyi çeken fonksiyon
def scrape_page():
    try:
        # requests ve beautifulsoap ile sitenin ilk sayfasını alıyoruz.
        response = requests.get("https://scrapeme.live/shop/")
        soup = BeautifulSoup(response.text, 'html.parser')

        # listenin içine girip verileri 1 saniye aralıklarla mesaj olarak yolluyoruz.
        for product in soup.select('li.product'):
            data = {
                "name": product.find('h2').text.strip(),
                "price": product.find('span', class_='price').text.strip(),
                "stock": product.find('p', class_='stock').text.strip() if product.find('p', class_='stock') else "Stok Yok",
                "image": product.find('img')['src']
            }

            producer.send('scraped_products', value=data)
            time.sleep(1)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        producer.flush() # Tüm mesajları kafkaya yolluyor.


if __name__ == "__main__":
    scrape_page()
