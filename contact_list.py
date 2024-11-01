# Inisialisasi daftar kontak sebagai list of dictionaries
contact_list = []

# Fungsi untuk menampilkan semua kontak
def show_contacts():
    if not contact_list:
        print("Daftar kontak kosong.")
    else:
        print("ID\tNama\t\tNomor Telepon")
        for contact in contact_list:
            print(f"{contact['id']}\t{contact['name']}\t\t{contact['phone']}")

# Fungsi untuk menambahkan kontak baru
def add_contact(id, name, phone):
    contact = {
        'id': id,
        'name': name,
        'phone': phone
    }
    contact_list.append(contact)
    print("Kontak berhasil ditambahkan.")

# Fungsi untuk mengubah kontak berdasarkan ID
def update_contact(id, new_name=None, new_phone=None):
    for contact in contact_list:
        if contact['id'] == id:
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            print("Kontak berhasil diubah.")
            return
    print("Kontak dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus kontak berdasarkan ID
def delete_contact(id):
    for contact in contact_list:
        if contact['id'] == id:
            contact_list.remove(contact)
            print("Kontak berhasil dihapus.")
            return
    print("Kontak dengan ID tersebut tidak ditemukan.")

# Main program
while True:
    print("\n--- Contact List ---")
    print("1. Tampilkan Kontak")
    print("2. Tambah Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    
    choice = input("Pilih menu (1-5): ")
    
    if choice == '1':
        show_contacts()
    elif choice == '2':
        id = input("Masukkan ID: ")
        name = input("Masukkan Nama: ")
        phone = input("Masukkan Nomor Telepon: ")
        add_contact(id, name, phone)
    elif choice == '3':
        id = input("Masukkan ID kontak yang akan diubah: ")
        new_name = input("Masukkan Nama baru (tekan Enter jika tidak ingin mengubah): ")
        new_phone = input("Masukkan Nomor Telepon baru (tekan Enter jika tidak ingin mengubah): ")
        update_contact(id, new_name or None, new_phone or None)
    elif choice == '4':
        id = input("Masukkan ID kontak yang akan dihapus: ")
        delete_contact(id)
    elif choice == '5':
        print("Terima kasih telah menggunakan aplikasi Contact List.")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia.")
