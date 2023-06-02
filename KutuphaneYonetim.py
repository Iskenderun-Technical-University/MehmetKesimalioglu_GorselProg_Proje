import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

# Veritabanına bağlanma
connector = sqlite3.connect('kutuphane.db')
cursor = connector.cursor()

connector.execute(
    'CREATE TABLE IF NOT EXISTS Kutuphane (BK_ISIM TEXT, BK_ID TEXT PRIMARY KEY NOT NULL, YAZAR_ISIM TEXT, BK_DURUMU TEXT, KART_ID TEXT)'
)

# Fonksiyonlar
def veren_kart():
    Cid = sd.askstring('Veren Kart ID', 'Verenin Kart ID\'sini girin:\t\t\t')

    if not Cid:
        mb.showerror('Veren ID\'si boş olamaz!', 'Veren ID\'si boş bırakılamaz, bir değere sahip olmalıdır')
    else:
        return Cid


def kayitlari_goster():
    global connector, cursor
    global tree

    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM Kutuphane')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)


def alanlari_temizle():
    global bk_durumu, bk_id, bk_isim, yazar_isim, kart_id

    bk_durumu.set('Mevcut')
    for i in ['bk_id', 'bk_isim', 'yazar_isim', 'kart_id']:
        exec(f"{i}.set('')")
    bk_id_entry.config(state='normal')
    try:
        tree.selection_remove(tree.selection()[0])
    except:
        pass


def temizle_ve_goster():
    alanlari_temizle()
    kayitlari_goster()


def kayit_ekle():
    global connector
    global bk_isim, bk_id, yazar_isim, bk_durumu

    if bk_durumu.get() == 'Verildi':
        kart_id.set(veren_kart())
    else:
        kart_id.set('Yok')

    surety = mb.askyesno('Emin misiniz?',
                        'Bu veriyi girmek istediğinize emin misiniz?\nLütfen unutmayın, Kitap ID\'si gelecekte değiştirilemez')

    if surety:
        try:
            connector.execute(
                'INSERT INTO Kutuphane (BK_ISIM, BK_ID, YAZAR_ISIM, BK_DURUMU, KART_ID) VALUES (?, ?, ?, ?, ?)',
                (bk_isim.get(), bk_id.get(), yazar_isim.get(), bk_durumu.get(), kart_id.get()))
            connector.commit()

            temizle_ve_goster()

            mb.showinfo('Kayıt eklendi', 'Yeni kayıt başarıyla veritabanınıza eklendi')
        except sqlite3.IntegrityError:
            mb.showerror('Kitap ID zaten kullanımda!',
                         'Girmeye çalıştığınız Kitap ID veritabanında zaten bulunuyor, lütfen o kitabın kaydını değiştirin veya tarafınızda herhangi bir uyuşmazlık kontrol edin')


def kaydi_goster():
    global bk_isim, bk_id, bk_durumu, yazar_isim, kart_id
    global tree

    if not tree.focus():
        mb.showerror('Bir satır seçin!', 'Bir kaydı görüntülemek için önce tabloda seçmelisiniz. Devam etmeden önce lütfen bunu yapın.')
        return

    current_item_selected = tree.focus()
    values_in_selected_item = tree.item(current_item_selected)
    selection = values_in_selected_item['values']

    bk_isim.set(selection[0])
    bk_id.set(selection[1])
    bk_durumu.set(selection[3])
    yazar_isim.set(selection[2])
    try:
        kart_id.set(selection[4])
    except:
        kart_id.set('')


def kaydi_guncelle():
    def guncelle():
        global bk_durumu, bk_isim, bk_id, yazar_isim, kart_id
        global connector, tree

        if bk_durumu.get() == 'Verildi':
            kart_id.set(veren_kart())
        else:
            kart_id.set('Yok')

        cursor.execute('UPDATE Kutuphane SET BK_ISIM=?, BK_DURUMU=?, YAZAR_ISIM=?, KART_ID=? WHERE BK_ID=?',
                       (bk_isim.get(), bk_durumu.get(), yazar_isim.get(), kart_id.get(), bk_id.get()))
        connector.commit()

        temizle_ve_goster()

        edit.destroy()
        bk_id_entry.config(state='normal')

    kaydi_goster()

    bk_id_entry.config(state='disable')

    edit = Button(left_frame, text='Kaydı Güncelle', font=btn_font, bg=btn_hlb_bg, width=20, command=guncelle)
    edit.place(x=50, y=375)


def kaydi_sil():
    if not tree.selection():
        mb.showerror('Hata!', 'Lütfen veritabanından bir öğe seçin')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    cursor.execute('DELETE FROM Kutuphane WHERE BK_ID=?', (selection[1], ))
    connector.commit()

    tree.delete(current_item)

    mb.showinfo('Tamamlandı', 'Silmek istediğiniz kayıt başarıyla silindi.')

    temizle_ve_goster()


def envanteri_sil():
    if mb.askyesno('Emin misiniz?', 'Tüm envanteri silmek istediğinizden emin misiniz?\n\nBu komut geri alınamaz'):
        tree.delete(*tree.get_children())

        cursor.execute('DELETE FROM Kutuphane')
        connector.commit()
    else:
        return


def durumu_degistir():
    global kart_id, tree, connector

    if not tree.selection():
        mb.showerror('Hata!', 'Lütfen veritabanından bir kitap seçin')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    BK_id = values['values'][1]
    BK_durumu = values["values"][3]

    if BK_durumu == 'Verildi':
        surety = mb.askyesno('Dönüş onaylandı mı?', 'Kitap size geri döndü mü?')
        if surety:
            cursor.execute('UPDATE Kutuphane SET bk_durumu=?, kart_id=? WHERE bk_id=?', ('Mevcut', 'Yok', BK_id))
            connector.commit()
        else:
            mb.showinfo('Dönüş yapılamadı', 'Kitap durumu; kitap size geri dönmediyse Mevcut olarak ayarlanamaz')
    else:
        cursor.execute('UPDATE Kutuphane SET bk_durumu=?, kart_id=? where bk_id=?', ('Verildi', veren_kart(), BK_id))
        connector.commit()

    temizle_ve_goster()


# Değişkenler
lf_bg = 'LemonChiffon'  # Sol Frame Arkaplan Rengi
rtf_bg = 'Lavender'  # Sağ Üst Frame Arkaplan Rengi
rbf_bg = 'LightSalmon'  # Sağ Alt Frame Arkaplan Rengi
btn_hlb_bg = 'LightCoral'  # Başlık Etiketleri ve Düğmeler için Arka Plan rengi

lbl_font = ('Georgia', 13)  # Tüm etiketler için yazı tipi
entry_font = ('Times New Roman', 12)  # Tüm Giriş widgetları için yazı tipi
btn_font = ('Gill Sans MT', 13)

# Ana GUI penceresini başlatma
root = Tk()
root.title('Kütüphane Yönetim Sistemi Mehmet Kesimalioğlu')
root.geometry('1010x530')
root.resizable(0, 0)

Label(root, text='KÜTÜPHANE YÖNETİM SİSTEMİ', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg, fg='White').pack(side=TOP, fill=X)

# StringVars
bk_durumu = StringVar()
bk_isim = StringVar()
bk_id = StringVar()
yazar_isim = StringVar()
kart_id = StringVar()

# Frame'ler
left_frame = Frame(root, bg=lf_bg)
left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

RT_frame = Frame(root, bg=rtf_bg)
RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

RB_frame = Frame(root)
RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

# Sol Frame
Label(left_frame, text='Kitap İsmi', bg=lf_bg, font=lbl_font).place(x=98, y=25)
Entry(left_frame, width=25, font=entry_font, text=bk_isim).place(x=45, y=55)

Label(left_frame, text='Kitap ID', bg=lf_bg, font=lbl_font).place(x=110, y=105)
bk_id_entry = Entry(left_frame, width=25, font=entry_font, text=bk_id)
bk_id_entry.place(x=45, y=135)

Label(left_frame, text='Yazar İsmi', bg=lf_bg, font=lbl_font).place(x=90, y=185)
Entry(left_frame, width=25, font=entry_font, text=yazar_isim).place(x=45, y=215)

Label(left_frame, text='Kitap Durumu', bg=lf_bg, font=lbl_font).place(x=75, y=265)
dd = OptionMenu(left_frame, bk_durumu, *['Mevcut', 'Verildi'])
dd.configure(font=entry_font, width=12)
dd.place(x=75, y=300)

submit = Button(left_frame, text='Yeni kayıt ekle', font=btn_font, bg=btn_hlb_bg, width=20, command=kayit_ekle)
submit.place(x=50, y=375)

clear = Button(left_frame, text='Alanları temizle', font=btn_font, bg=btn_hlb_bg, width=20, command=alanlari_temizle)
clear.place(x=50, y=435)

# Sağ Üst Frame
Button(RT_frame, text='Kitap kaydını sil', font=btn_font, bg=btn_hlb_bg, width=17, command=kaydi_sil).place(x=8, y=30)
Button(RT_frame, text='Tüm envanteri sil', font=btn_font, bg=btn_hlb_bg, width=17, command=envanteri_sil).place(x=178, y=30)
Button(RT_frame, text='Kitap bilgilerini güncelle', font=btn_font, bg=btn_hlb_bg, width=17,
       command=kaydi_guncelle).place(x=348, y=30)
Button(RT_frame, text='Kitap Durumunu Değiştir', font=btn_font, bg=btn_hlb_bg, width=19,
       command=durumu_degistir).place(x=518, y=30)

# Sağ Alt Frame
Label(RB_frame, text='KİTAP ENVANTERİ', bg=rbf_bg, font=("Noto Sans CJK TC", 15, 'bold')).pack(side=TOP, fill=X)

tree = ttk.Treeview(RB_frame, selectmode=BROWSE, columns=('Kitap İsmi', 'Kitap ID', 'Yazar', 'Durum', 'Veren Kart ID'))

XScrollbar = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
YScrollbar = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
XScrollbar.pack(side=BOTTOM, fill=X)
YScrollbar.pack(side=RIGHT, fill=Y)

tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

tree.heading('Kitap İsmi', text='Kitap İsmi', anchor=CENTER)
tree.heading('Kitap ID', text='Kitap ID', anchor=CENTER)
tree.heading('Yazar', text='Yazar', anchor=CENTER)
tree.heading('Durum', text='Kitap Durumu', anchor=CENTER)
tree.heading('Veren Kart ID', text='Verenin Kart ID\'si', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=225, stretch=NO)
tree.column('#2', width=70, stretch=NO)
tree.column('#3', width=150, stretch=NO)
tree.column('#4', width=105, stretch=NO)
tree.column('#5', width=132, stretch=NO)

tree.place(y=30, x=0, relheight=0.9, relwidth=1)

temizle_ve_goster()

# Pencereyi tamamlama
root.update()
root.mainloop()

