# Learning Log - Python Crash Course
​
Bu proje, Eric Matthes'in "Python Crash Course" kitabındaki "Learning Log" projesine dayanmaktadır. Proje, Python programlama dilini ve web geliştirmeyi öğrenmek isteyenler için tasarlanmıştır.
​
## Proje Açıklaması
Learning Log, kullanıcıların öğrenme günlüklerini oluşturabileceği bir web uygulamasıdır. Kullanıcılar, her gün öğrendikleri konuları kaydedebilir, kategorize edebilir ve detaylı açıklamalar ekleyebilirler.

## Kurulum
Proje yerel bir ortamda çalıştırılmak isteniyorsa, aşağıdaki adımları izleyin:
1. Projeyi klonlayın: `git clone https://github.com/salimunlu/learning_log1.git`
2. Proje dizinine gidin: `cd learning-log`
3. Sanal bir ortam oluşturun: `python -m venv venv`
4. Sanal ortamı etkinleştirin:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Gerekli paketleri yükleyin: `pip install -r requirements.txt`
6. Veritabanını oluşturun: `python manage.py migrate`
7. Uygulamayı başlatın: `python manage.py runserver`
​
Uygulama şimdi [http://localhost:8000/](http://localhost:8000/) adresinde çalışacaktır.
​
## Kullanım
1. Tarayıcıda [http://localhost:8000/](http://localhost:8000/) adresine gidin.
2. Yeni bir hesap oluşturun veya mevcut bir hesapla giriş yapın.
3. Learning Log'unuzu oluşturun, günlük öğrenmelerinizi kaydedin.
​
## Katkılar ve Geri Bildirim
Bu proje açık kaynaklıdır. Her türlü katkı ve geri bildirim beklenmektedir. Lütfen GitHub repo'suna katkıda bulunun veya sorunları rapor edin.
