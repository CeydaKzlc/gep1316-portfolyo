# Kullanıcıdan adını alıyoruz
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını alıyoruz ve yaş hesaplayabilmek için tam sayıya (int) çeviriyoruz
dogum_yili = int(input("Doğum yılınız nedir? "))

# İçinde bulunduğumuz yılı baz alarak yaşı hesaplıyoruz
guncel_yil = 2026
yas = guncel_yil - dogum_yili

# Kişiye özel karşılama mesajını ekrana yazdırıyoruz
print(f"Merhabalar {ad}! Yaşınız: {yas}")
