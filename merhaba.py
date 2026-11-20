# Yaş Hesaplayıcı ve Kişisel Karşılama Programı

Kullanıcıdan adını ve doğum yılını alarak güncel yaşını hesaplayan, hatalı veri girişlerine karşı doğrulama (validation) mekanizmasına sahip konsol tabanlı bir Python uygulamasıdır.

## Özellikler

- **Dinamik Yıl Hesaplama:** Python `datetime` modülü sayesinde güncel yılı otomatik olarak algılar.
- **Giriş Doğrulama (Hata Yönetimi):**
  - Sayısal olmayan karakter girişlerini (`abc`, boşluk vb.) yakalar ve uyarır.
  - Gelecek yılların girilmesini engeller.
  - 1900 yılından önceki gerçekçi olmayan tarihleri reddeder.
  - İsim alanının boş bırakılmasını önler.
- **Kişiselleştirilmiş Çıktı:** Kullanıcının adını baş harfi büyük olacak şekilde düzenleyerek özel bir karşılama mesajı sunar.

## Gereksinimler

- Python 3.6 veya üzeri (Harici bir kütüphane kurulumu gerektirmez).

## Kurulum ve Çalıştırma

1. Proje dosyalarını bilgisayarınıza indirin veya `yas_hesaplayici.py` dosyasını oluşturun.
2. Terminali (veya komut istemcisini) açarak dosyanın bulunduğu klasöre gidin.
3. Aşağıdaki komutu çalıştırın:

```bash
python3 yas_hesaplayici.py
