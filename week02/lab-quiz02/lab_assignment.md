# lab02_purchase_quote.py

# 1. Ürün bilgilerini alma
item1_name = input("1. ürünün adı: ")
item1_qty = int(input("1. ürünün adedi: "))
item1_price = float(input("1. ürünün birim fiyatı (TRY): "))

# 2. Ürün bilgilerini alma
item2_name = input("2. ürünün adı: ")
item2_qty = int(input("2. ürünün adedi: "))
item2_price = float(input("2. ürünün birim fiyatı (TRY): "))

# Kargo ve vergi bilgilerini alma
delivery_fee = float(input("Kargo ücreti (TRY): "))
tax_percentage = float(input("Vergi oranı (%): "))

# Hesaplamalar
line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price
subtotal = line1_total + line2_total
tax_amount = subtotal * (tax_percentage / 100)
final_total = subtotal + tax_amount + delivery_fee

# Çıktıyı iki ondalık basamakla yazdırma
print("\n--- FİYAT TEKLİFİ ÖZETİ ---")
print(f"{item1_name} ({item1_qty} x {item1_price:.2f} TRY): {line1_total:.2f} TRY")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f} TRY): {line2_total:.2f} TRY")
print(f"Ara Toplam (Subtotal): {subtotal:.2f} TRY")
print(f"Vergi (%{tax_percentage:.0f}): {tax_amount:.2f} TRY")
print(f"Kargo Ücreti: {delivery_fee:.2f} TRY")
print(f"Genel Toplam (Final Total): {final_total:.2f} TRY")

