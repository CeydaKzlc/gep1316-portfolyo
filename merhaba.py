from datetime import datetime


def main():
    guncel_yil = datetime.now().year

    # İsim alma ve boş bırakılmasını önleme
    while True:
        ad = input("Lütfen adınızı girin: ").strip()
        if ad:
            break
        print("Uyarı: İsim alanı boş bırakılamaz. Lütfen tekrar deneyin.\n")

    # Doğum yılı alma ve doğrulama
    while True:
        giris = input("Lütfen doğum yılınızı girin (Örn: 2006): ").strip()

        try:
            dogum_yili = int(giris)

            if dogum_yili > guncel_yil:
                print(
                    f"Uyarı: Gelecek bir yıl ({dogum_yili}) giremezsiniz. Lütfen geçerli bir yıl girin.\n"
                )
            elif dogum_yili < 1900:
                print(
                    "Uyarı: 1900 yılından küçük bir tarih girdiniz. Lütfen geçerli bir doğum yılı girin.\n"
                )
            else:
                yas = guncel_yil - dogum_yili
                break

        except ValueError:
            print(
                "Uyarı: Hatalı giriş! Lütfen doğum yılınızı yalnızca rakamlarla yazın.\n"
            )

    # Kişiye özel karşılama mesajı
    print("-" * 45)
    print(f"Hoş geldin, {ad.capitalize()}!")
    print(f"{guncel_yil} yılı itibarıyla {yas} yaşındasın. Harika bir gün dilerim!")
    print("-" * 45)


if __name__ == "__main__":
    main()
