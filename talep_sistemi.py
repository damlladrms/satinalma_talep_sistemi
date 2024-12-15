import json
import os

# Talep verilerini kaydetmek için dosya adı
data_file = "talepler.json"

def load_talepler():
    """Talepleri JSON dosyasından yükler."""
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_talepler(talepler):
    """Talepleri JSON dosyasına kaydeder."""
    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(talepler, file, ensure_ascii=False, indent=4)

def yeni_talep():
    """Yeni talep oluşturur."""
    print("\nYeni Talep Oluştur")
    talep = {
        "talep_no": len(talepler) + 1,
        "talep_eden": input("Talep Eden Kişi: "),
        "urun_adi": input("Ürün Adı: "),
        "miktar": int(input("Miktar: ")),
        "gerekce": input("Gerekçe: "),
        "durum": "Beklemede"
    }
    talepler.append(talep)
    save_talepler(talepler)
    print("\nTalep başarıyla oluşturuldu!\n")

def talepleri_listele():
    """Mevcut talepleri listeler."""
    print("\nMevcut Talepler")
    for talep in talepler:
        print(f"\nTalep No: {talep['talep_no']}")
        print(f"Talep Eden: {talep['talep_eden']}")
        print(f"Ürün Adı: {talep['urun_adi']}")
        print(f"Miktar: {talep['miktar']}")
        print(f"Gerekçe: {talep['gerekce']}")
        print(f"Durum: {talep['durum']}")

def talep_onayla_reddet():
    """Talebi onaylar veya reddeder."""
    talep_no = int(input("\nİşlem yapmak istediğiniz talep numarasını girin: "))
    talep = next((t for t in talepler if t["talep_no"] == talep_no), None)
    if not talep:
        print("Geçersiz talep numarası!\n")
        return

    print(f"\nTalep No: {talep['talep_no']}")
    print(f"Talep Eden: {talep['talep_eden']}")
    print(f"Ürün Adı: {talep['urun_adi']}")
    print(f"Miktar: {talep['miktar']}")
    print(f"Gerekçe: {talep['gerekce']}")
    print(f"Durum: {talep['durum']}")

    yeni_durum = input("Talep durumunu güncelleyin (Onaylandı/Reddedildi): ")
    if yeni_durum in ["Onaylandı", "Reddedildi"]:
        talep["durum"] = yeni_durum
        save_talepler(talepler)
        print("Talep durumu başarıyla güncellendi!\n")
    else:
        print("Geçersiz durum girdiniz!\n")

def menu():
    """Ana menüyü gösterir."""
    while True:
        print("\nSatın Alma Talep Sistemi")
        print("1. Yeni Talep Oluştur")
        print("2. Talepleri Listele")
        print("3. Talep Onayla/Reddet")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")
        if secim == "1":
            yeni_talep()
        elif secim == "2":
            talepleri_listele()
        elif secim == "3":
            talep_onayla_reddet()
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin!\n")

# Program başlangıcı
talepler = load_talepler()
menu()
