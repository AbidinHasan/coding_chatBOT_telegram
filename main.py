from config import TOKENS
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import time
import threading
from telebot import types
import os
from datetime import datetime 

bot = telebot.TeleBot(token=TOKENS)



#Pesan Broadcast auto
#GUNAKAN TREADHING UNTUK MENYALAKAN  (hapus #)
def kirim_ke_semua():
    print("pesan broadcase berhasil")
    try:
        with open("ID_SHARE.txt", "r") as f:
            semua_id = f.read().splitlines()
        for chat_id in semua_id:
            bot.send_message(chat_id, "INFO!!!! \nREPORT MINGGUAN SUDAH UPDATE pindah akses ke channel :\nhttps://t.me/+Dahmhv0ZRq4wMWNl") #Isi pesan disini
            return
    except Exception as e:
        print("Gagal Kirim cuyyy iki alasane :", e)

threading.Thread(target=kirim_ke_semua, daemon=True).start()    #untuk aktifkan


#membuat Tombol
def gen_markup(): 
    print("menampilkan tombol")
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Tentang IPAL", callback_data="cb1"),
            InlineKeyboardButton("Foto IPAL", callback_data="cb2"))

    markup.add(InlineKeyboardButton("Video IPAL", callback_data="cb3"), 
            InlineKeyboardButton("REPORT MINGGUAN", callback_data="cb4"))
    
    markup.add(InlineKeyboardButton("(WI) WORK INSTRUCTION", callback_data="cb6"))
    markup.add(InlineKeyboardButton("Hasil LAB 🔬", callback_data="cb5"))
    markup.add(InlineKeyboardButton("UPLOAD 🚀", callback_data="cb7"))
    return markup

#Tombol WI
# pilih WI

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb6")
def tombolWI(call):
    bot.answer_callback_query(call.id)
    print("mencari WI")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("BAK EQUALISASI",callback_data="wi1"),
            types.InlineKeyboardButton("BAK NETRALISATOR",callback_data="wi2"))
    
    markup.add(types.InlineKeyboardButton("BAK FLOKULATOR 1",callback_data="wi3"),
            types.InlineKeyboardButton("BAK KOAGULATOR 1",callback_data="wi4"))
    
    markup.add(types.InlineKeyboardButton("BAK AN AEROB",callback_data="wi5"),
            types.InlineKeyboardButton("BAK AEROB",callback_data="wi6"))
    
    markup.add(types.InlineKeyboardButton("BAK KOAGULATOR 2",callback_data="wi7"),
            types.InlineKeyboardButton("BAK FLOKULATOR 2",callback_data="wi8"))
    
    markup.add(types.InlineKeyboardButton("BAK THIKENER",callback_data="wi9"),
            types.InlineKeyboardButton("FILTER PRESS",callback_data="wi10"))
    
    markup.add(types.InlineKeyboardButton("POLIMER ANION",callback_data="wi11"),
            types.InlineKeyboardButton("POLIMER CATION",callback_data="wi12"))
    markup.add(types.InlineKeyboardButton("Kembali ↩️", callback_data="wi13"))
    
    kata = "PILIH WORK INSTRUCTION :"
    bot.send_message(call.message.chat.id, kata, reply_markup=markup )

    
    bot.delete_message(call.message.chat.id, call.message.message_id)




#Masukkan saran
@bot.message_handler(func=lambda msg: not msg.text.startswith('/'), content_types=['text'])
def simpan_text_user(message):
    print("user memberi pesan")
    user = message.from_user
    with open("log_pesan.txt", "a") as file:
        file.write(f"{user.id} ({user.first_name}): {message.text}\n")

    bot.reply_to(message, "Masukkan diterima bolo ✅")



#Simpan Dokumen yg dikirim
@bot.message_handler(content_types=['document'])
def handle_document(message):
    print("Kirim dokumen")
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    filename = message.document.file_name
    with open("/home/bidin/Desktop/RunTerminal/dokumen/" + f"file_dari_user_{filename}", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, f"File '{filename}' tersimpan")



#Save foto yg dikirim
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    print("Kirim foto")
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Ambil waktu sekarang dan ID user
    jam = datetime.now()
    cetakjam = jam.strftime("%H-%M-%S")
    timestamp = int(time.time())
    user_id = message.from_user.id
    nama = message.from_user.first_name

    # Buat nama file unik
    filename = f"foto_{message.caption}_{cetakjam}_{nama}_{user_id}_{timestamp}.jpg"

    # Simpan file
    with open("/home/bidin/Desktop/RunTerminal/foto/" + filename, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Foto tersimpan")







@bot.callback_query_handler(func=lambda call: call.data == "wi13")
def tombolWI(call):
    bot.answer_callback_query(call.id)
    print("GAK SIDO, menampilkan tombol kembali")
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("Tentang IPAL", callback_data="cb1"),
            types.InlineKeyboardButton("Foto IPAL", callback_data="cb2"))

    markup.add(types.InlineKeyboardButton("Video IPAL", callback_data="cb3"), 
            types.InlineKeyboardButton("REPORT MINGGUAN", callback_data="cb4"))
    
    markup.add(types.InlineKeyboardButton("(WI) WORK INSTRUCTION", callback_data="cb6"))
    markup.add(types.InlineKeyboardButton("Hasil LAB 🔬", callback_data="cb5"))
    markup.add(types.InlineKeyboardButton("UPLOAD 🚀", callback_data="cb7"))
    
    kata = "MENU AWAL :"
    bot.send_message(call.message.chat.id, kata, reply_markup=markup)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    

#def hapus_tombol_otomatis(chat_id, message_id, delay=100):
#    time.sleep(delay)
#    try:
#        bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
#    except Exception as e:
#        print(f"tomboL wes dipencet gak sido dihapus")

#Awal mulai
@bot.message_handler(commands=['start'])
def welcome(message):
    p = message.from_user
    userid = message.from_user.id
    nama=message.from_user.first_name
    namaet = p.username if p.username else "(Tidak ada usename)"

    try:
        with open("ID_LOGIN.txt", "r") as f:
            semua_id = f.read().splitlines()
    except FileNotFoundError:
        semua_id = []

    data_user = f"{userid}_({namaet})_{nama}"

    if data_user not in semua_id:
        with open("ID_LOGIN.txt", "a") as f:
            f.write(data_user + "\n")
        print("User baru login")
    else:
        print("User lama")

    welcome_text = f'Halo {nama} Selamat datang di IPAL'
    bot.send_message(message.chat.id, welcome_text, reply_markup=gen_markup())
    bot.delete_message(message.chat.id, message.message_id)
    
    print(f"Siapa yg login : ({nama}) id : ({userid}) username : ({namaet})")
    #threading.Thread(target=hapus_tombol_otomatis, args=(sent.chat.id, sent.message_id, 100)).start()
    

#Tampilkan Tombol
@bot.message_handler(commands=['pilihan'])  
def tampilkan_opsi(message):
    nama = message.from_user.first_name
    noid = message.from_user.id
    p = message.from_user
    namaet = p.username if p.username else "(Tidak punya username)"
    print(f"({namaet}) id: ({noid}) jalok tombol")

    try:
        with open("ID_LOGIN.txt", "r") as f:
            semua_id = f.read().splitlines()
    except FileNotFoundError:
        semua_id = []

    data_user = f"{noid}_({namaet})_{nama}"

    if data_user not in semua_id:
        with open("ID_LOGIN.txt", "a") as f:
            f.write(data_user + "\n")
        print("User baru login")
    else:
        print("User lama")

    surat = "Monggo dipilih :"
    bot.send_message(message.chat.id, surat, reply_markup=gen_markup())
    bot.delete_message(message.chat.id, message.message_id)
    #threading.Thread(target=hapus_tombol_otomatis, args=(sent.chat.id, sent.message_id, 100)).start()

#===========================Class Execution===================================================
#Foto
# iki data ne utk diisi konten
def tampilkan_foto(chat_id):
    print('Akses gambar')
    url_panel = "https://i.ibb.co/0y6WLG5V/6161168442409993667.jpg"
    url_ekual = "https://ik.imagekit.io/galleryBiden/6194777167091582216.jpg?updatedAt=1748950785098"
    url_Aerob = "https://ik.imagekit.io/galleryBiden/6194777167091582224.jpg?updatedAt=1748950778079"
    url_aerasiDnCf = "https://ik.imagekit.io/galleryBiden/6194777167091582215.jpg?updatedAt=1748950785307"
    url_kimia2 = "https://ik.imagekit.io/galleryBiden/6194777167091582221.jpg?updatedAt=1748950778108"
    url_ikan = "https://ik.imagekit.io/galleryBiden/6194777167091582218.jpg?updatedAt=1748950778075"
    url_filter = "https://ik.imagekit.io/galleryBiden/6194777167091582223.jpg?updatedAt=1748950778073"
    url_thikener = "https://ik.imagekit.io/galleryBiden/6194777167091582220.jpg?updatedAt=1748950778013"
    url_rootBlow = "https://ik.imagekit.io/galleryBiden/6194777167091582217.jpg?updatedAt=1748950777928"
    url_PrepKimia = "https://ik.imagekit.io/galleryBiden/6194777167091582225.jpg?updatedAt=1748950777931"
    url_ipalroom = "https://ik.imagekit.io/galleryBiden/6194777167091582222.jpg?updatedAt=1748950777713"
    url_fishpond = "https://ik.imagekit.io/galleryBiden/6194777167091582219.jpg?updatedAt=1748950777681"
    url_cf = "https://ik.imagekit.io/galleryBiden/6260361356356207840.jpg?updatedAt=1748954947599"

    kata = f"Equalisasi \nTempat balancing material limbah agar tercampur rata"
    kata2 = f"Root Blower \nMengaduk atau pelarutan oksigen yang ada pada air limbah"
    kata3 = f"Clarifier \nTempat sedimentasi lumpur, memastikan lumpur tidak ikut overflow ke tahap selanjutnya"
    kata4 = f"Bak Aerasi atau Aerob \nPengolahan limbah menggunakan mikro organisme,yang membutuhkan oksigen"
    kata5 = f"Pengolahan aerasi melalui clarifier biologi, bak kimia, dan clarifier kimia"
    kata6 = f"Air hasil pengolahan masuk ke bak fishpond"
    kata7 = f"Ikan sebagai monitoring parameter lingkungan"
    kata8 = f"Ruangan IPAL dan Gudang persediaan IPAL"
    kata9 = f"Tempat untuk preparation bahan kimia untuk pengolahan WWTP"
    kata10 = f"Filter Sand & Carbon"
    kata11 = f"Thikener \nPenampungan sludge dari clarifier"
    kata12 = f"Clarifier biologi"
    kata13 = f"Panel WWTP & STP"

    delay = (5)
    bot.send_photo(chat_id, photo=url_ekual, caption=kata)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_rootBlow, caption=kata2)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_cf, caption=kata3)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_Aerob, caption=kata4)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_aerasiDnCf, caption=kata5)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_fishpond, caption=kata6)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_ikan, caption=kata7)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_ipalroom, caption=kata8)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_PrepKimia, caption=kata9)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_filter, caption=kata10)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_thikener, caption=kata11)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_kimia2, caption=kata12)
    time.sleep(delay)
    bot.send_photo(chat_id, photo=url_panel, caption=kata13)

    

# Trigger dari command
@bot.message_handler(commands=['foto'])
def handle_lihat_foto_command(message):
    nama = message.from_username
    
    noid = message.from_user.id
    print(f"{nama},id: {noid} mengakses lewat command")
    tampilkan_foto(message.chat.id)

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb2")
def handle_lihat_foto_callback(call):
    bot.answer_callback_query(call.id)
    

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Tunggu sek kawan", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )

    tampilkan_foto(call.message.chat.id)
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    


#Tentang ipal

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb1")
def handle_lihat_tentang_callback(call):
    print("Tentang IPAL")
    bot.answer_callback_query(call.id)
    

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Tunggu sek kawan", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    welcome_text = (f"*IPAL* adalah singkatan dari Instalasi Pengolahan Air Limbah. Ini adalah sistem atau fasilitas yang dirancang untuk mengolah air limbah (baik dari rumah tangga, industri, maupun komersial) sebelum air tersebut dibuang ke lingkungan, seperti sungai, danau, atau laut, agar tidak mencemari lingkungan.\n\n*Fungsi Utama IPAL :*\n\n1. Mengurangi pencemaran lingkungan \n– Limbah yang dibuang langsung tanpa diolah bisa mencemari air tanah dan perairan.\n2. Melindungi kesehatan manusia dan hewan \n– Air limbah sering mengandung bakteri, virus, bahan kimia beracun, dan logam berat.\nMemenuhi standar baku mutu air limbah \n– Agar sesuai dengan peraturan pemerintah sebelum dibuang ke lingkungan.\n\n*Jenis-jenis IPAL :*\n\n*IPAL Domestik:* Untuk limbah rumah tangga (seperti dari toilet, dapur, kamar mandi).\n\n*IPAL Industri:* Untuk limbah dari pabrik atau kegiatan industri (yang biasanya lebih kompleks dan mengandung bahan kimia khusus).\n\n*Proses dalam IPAL biasanya melibatkan :*\n\nProses fisik (penyaringan, pengendapan)\nProses kimia (netralisasi, koagulasi, flokulasi)\nProses biologi (menggunakan mikroorganisme untuk mengurai zat organik)")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Kembali ↩️", callback_data="wi13"))
    
    
    bot.send_message(call.message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown" )


    bot.delete_message(call.message.chat.id, call.message.message_id)
    


# Video
def tampilkan_video(chat_id):
    print("sedang akses video")
    url = "https://ik.imagekit.io/galleryBiden/aerob.mp4?updatedAt=1748960489775"
    bot.send_video(chat_id, video=url)

# Trigger dari command
@bot.message_handler(commands=['video'])
def handle_lihat_video_command(message):
    tampilkan_video(message.chat.id)

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb3")
def handle_lihat_video_callback(call):
    bot.answer_callback_query(call.id)
    

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Tunggu sek kawan", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )

    tampilkan_video(call.message.chat.id)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    



# Laporan
def tampilkan_laporan(chat_id):
    print("Kirim file Laporan")
    filenya = "/home/bidin/Desktop/RunTerminal/REPORT MINGGUAN IPAL.xlsx"
    with open (filenya, "rb" ) as Laporan_xsl:
        bot.send_document(chat_id, document=Laporan_xsl)
    file2 = "/home/bidin/Desktop/RunTerminal/Data Loging IPAL.xlsx"
    with open (file2, "rb") as Laporan2 :
        bot.send_document(chat_id, Laporan2)

# Trigger dari command
@bot.message_handler(commands=['lapor'])
def handle_lihat_laporan_command(message):
    tampilkan_laporan(message.chat.id)

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb4")
def handle_lihat_laporan_callback(call):
    bot.answer_callback_query(call.id)


    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Tunggu sek kawan", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )

    tampilkan_laporan(call.message.chat.id)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    


# Laporan LAB
def tampilkan_hasillab(chat_id):
    print("info LAB resmi")
    url = "https://ik.imagekit.io/galleryBiden/dokumen/HASIL%20LAB%20IPAL%20APRIL%202025.pdf?updatedAt=1749008361205"
    bot.send_document(chat_id, document=url)

# Trigger dari command
@bot.message_handler(commands=['lab'])
def handle_lihat_lab_command(message):
    tampilkan_hasillab(message.chat.id)

# Trigger dari callback
@bot.callback_query_handler(func=lambda call: call.data == "cb5")
def handle_lihat_lab_callback(call):
    bot.answer_callback_query(call.id)
    

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Cari hasil LAB terbaru", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    kata = "Halis LAB terbaru :"
    bot.send_message(call.message.chat.id, kata)
    tampilkan_hasillab(call.message.chat.id,)
    
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "cb7")
def upload(call):
    print("uplod")
    bot.answer_callback_query(call.id)
    

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Sek bos", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    kata = "Saran atau masukan\nUpload dokumen\nUpload foto\nGaskeunnn!!!"
    
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Kembali ↩️", callback_data="wi13"))
    
    
    bot.send_message(call.message.chat.id, kata, reply_markup=markup )
    
    bot.delete_message(call.message.chat.id, call.message.message_id)




# WI EQUAL
@bot.callback_query_handler(func=lambda call: call.data == "wi1")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_082%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Ekualisasi.pdf?updatedAt=1749008427848"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI NETRALISATOR
@bot.callback_query_handler(func=lambda call: call.data == "wi2")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "ttps://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_083%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Netralisasi.pdf?updatedAt=1749008427260"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI FLOKULATOR 1
@bot.callback_query_handler(func=lambda call: call.data == "wi3")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_085%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Flokulator-1.pdf?updatedAt=1749008422600"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)

    

# WI KOAGULATOR 1
@bot.callback_query_handler(func=lambda call: call.data == "wi4")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_084%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Koagulator-1.pdf?updatedAt=1749008977528"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI ANAEROB
@bot.callback_query_handler(func=lambda call: call.data == "wi5")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_086%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20AnAerob.pdf?updatedAt=1749008421821"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI AEROB
@bot.callback_query_handler(func=lambda call: call.data == "wi6")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_087%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Aerob.pdf?updatedAt=1749008421451"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    


# WI KOAGULATOR 2
@bot.callback_query_handler(func=lambda call: call.data == "wi7")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_088%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Koagulator-2.pdf?updatedAt=1749008422032"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI FLOKULATOR 2
@bot.callback_query_handler(func=lambda call: call.data == "wi8")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_089%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Flokulator-2.pdf?updatedAt=1749008422136"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI THIKENER
@bot.callback_query_handler(func=lambda call: call.data == "wi9")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_090%20Pengeporasian%20IPAL%20WWTP%20-%20Bak%20Thickener.pdf?updatedAt=1749008422393"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI FILTER PRESS
@bot.callback_query_handler(func=lambda call: call.data == "wi10")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_091%20Pengeporasian%20IPAL%20WWTP%20-%20Filter%20Press.pdf?updatedAt=1749008422299"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI POLIMER ANION
@bot.callback_query_handler(func=lambda call: call.data == "wi11")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_092%20Pengeporasian%20IPAL%20WWTP%20-%20Polimer%20Anion.pdf?updatedAt=1749008422324"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)



# WI POLIMER CATION
@bot.callback_query_handler(func=lambda call: call.data == "wi12")
def wi(call):
    bot.answer_callback_query(call.id)
    print("golek WI")

    loading_markup = InlineKeyboardMarkup()
    loading_markup.add(InlineKeyboardButton("⏳ Mencari data WI", callback_data="disabled"))
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=loading_markup
    )
    
    link = "https://ik.imagekit.io/galleryBiden/dokumen/BPK_WI_093%20Pengeporasian%20IPAL%20WWTP%20-%20Polimer%20Cation.pdf?updatedAt=1749008422488"
    bot.send_document(call.message.chat.id, link)

    bot.delete_message(call.message.chat.id, call.message.message_id)
    

# Folder tempat dokumen disimpan
FOLDER_PATH = "/home/bidin/Desktop/RunTerminal/dokumen"
FOLDER_FOTO = "/home/bidin/Desktop/RunTerminal/foto"

# Command untuk kirim semua dokumen
@bot.message_handler(commands=['bidin'])
def kirim_semua_dokumen(message):
    print("Ambil file tersembunyi")
    chat_id = message.chat.id

    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        if os.path.isfile(file_path) and any(file_name):
            try:
                with open(file_path, 'rb') as doc:
                    bot.send_document(chat_id, doc)
            
            except Exception as e:
                bot.send_message(chat_id, f"Gagal mengirim {file_name}: {str(e)}")
    bot.send_message(chat_id, "Komplit")


# Command untuk kirim semua foto
@bot.message_handler(commands=['bidinfoto'])
def kirim_semua_dokumen(message):
    print("Ambil foto tersembunyi")
    chat_id = message.chat.id
    nama = message.from_user.username
    print ("username : @",nama)



    for file_name in os.listdir(FOLDER_FOTO):
        file_path = os.path.join(FOLDER_FOTO, file_name)

        if os.path.isfile(file_path) and any(file_name):
            try:
                with open(file_path, 'rb') as photo:
                    bot.send_document(chat_id, photo)
    
                    
            except Exception as e:
                bot.send_message(chat_id, f"Gagal mengirim {file_name}: {str(e)}")
    bot.send_message(chat_id, "Komplit")


#files = os.listdir(FOLDER_PATH)
#for file in files:
#    if os.path.isfile(os.path.join(FOLDER_PATH, file)):
#        print(file)

print("Bot berjalan.....")
bot.infinity_polling()

