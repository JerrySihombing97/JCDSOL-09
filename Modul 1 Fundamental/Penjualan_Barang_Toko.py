# Capstone Project 1
# Case Study: Penjualan Barang Toko
# By Yeremia Sihombing

import sys

shop = [
    {
        'col1': 'Indeks',
        'col2': 'Nama Barang',
        'col3': 'Stok',
        'col4': 'Harga'
    },
    {
        'id': 0,
        'name': "Televisi",
        'stck': 10,
        'prc': 10000000
    },
    {
        'id': 1,
        'name': "Kulkas",
        'stck': 20,
        'prc': 15000000
    }
]

def main(title: str = 'Data Toko Barang Purwadhika') -> str:
    while(True):
        #Show title and menu
        rowformat(symb = "=", sent = title)
        print("""
        List Menu:
        1. Menampilkan Daftar Barang
        2. Menambah Jenis Barang
        3. Mengubah Stok dan Harga barang
        4. Menghapus Jenis Barang
        5. Exit Program
        """)

        menu = int(input('Silahkan Pilih Main_Menu[1-5]: '))
        print("\n")

        #Open the choosen menu
        if (menu == 1):
            menu_read(shop)
        elif (menu == 2):
            menu_create(shop)
        elif (menu == 3):
            menu_update(shop)
        elif (menu == 4):
            menu_delete(shop)
        elif (menu == 5):
            sys.exit()
        else:
            rowformat(symb = "*", sent = "Pilihan yang anda Masukkan Salah")

def menu_read(l1: list[dict],title: str = 'Daftar Barang Toko Purwadhika') -> str:
    while True:
        #Show title and sub-menu
        rowformat(symb = "+", sent = title)
        print(""" 
        List Sub-Menu:
        1. Daftar Seluruh Barang
        2. Daftar Barang Tertentu
        3. Kembali Ke Menu Utama
        """)
        submenu_read = int(input('Silahkan Pilih Sub Menu Read Data[1-3]: '))
        print("\n")
        
        # Open the choosen sub-menu
        sub_title = "Daftar Barang"
        
        if (submenu_read == 1):
            print(sub_title + ": ")
            if len(l1) > 1:
                show_table(l1)
            else:
                rowformat(symb = "*", sent = "Tidak Ada Data")
        elif (submenu_read == 2):
            idx_read = int(input('Masukkan indeks barang: '))
            print(sub_title + " dengan index " + str(idx_read))
            if len(l1) > idx_read + 1:
                #Show table
                list_chos = [l1[0], l1[idx_read+1]]
                show_table(list_chos)
            else:
                rowformat(symb = "*", sent = "Tidak Ada Data")
        elif (submenu_read == 3):
            return
        else:
            rowformat(symb = "*", sent = "Pilihan yang anda Masukkan Salah")


def menu_create(l1: list[dict],title: str = 'Menambah Jenis Barang') -> str:
    while True:
        #Show title and sub-menu
        rowformat(symb = "+", sent = title)
        print(""" 
        List Sub-Menu:
        1. Tambah Jenis Barang 
        2. Kembali Ke Menu Utama
        """)
        submenu_create = int(input('Silahkan Pilih Sub Menu Create Data[1-2]: '))
        print('\n')
        
        if (submenu_create == 1):
            name = str(input('Masukkan Jenis Barang: ')).capitalize()
            # Cek Ketersediaan Data
            n = 0
            for i in l1:
                if name in i.values():
                    rowformat(symb = "*", sent = "Data Sudah Ada")
                    break
                else: 
                    n+=1
                    # Input Data Baru
                    if n == len(l1):
                        count = int(input('Masukkan Stok Barang: '))
                        price = int(input('Masukkan Harga Barang: '))
                        
                        choose_save = str(input('Apakah Data Akan Disimpan? (Y/N) :')).capitalize()

                        if choose_save == 'Y':
                            # Simpan Data
                            shop.append(
                                {
                                    'id': len(l1) - 1,
                                    'name': name,
                                    'stck': count,
                                    'prc': price,
                                }   
                            )
                            print('Data Tersimpan\n')
                        show_table(l1)
                        break
        elif (submenu_create == 2):
            return
        else:
            rowformat(symb = "*", sent = "Pilihan yang anda Masukkan Salah")

def menu_update(l1: list[dict],title: str = 'Mengubah Data Barang') -> str:
    while True:
        #Show title and sub-menu
        rowformat(symb = "+", sent = title)
        print(""" 
        List Sub-Menu:
        1. Mengubah Stok dan Harga Barang
        2. Kembali Ke Menu Utama
        """)
        submenu_update = int(input('Silahkan Pilih Sub Menu Update Data[1-2]: '))
        print('\n')
        
        if (submenu_update == 1):
            idx_upd = int(input('Masukkan Indeks Barang: '))
            #Show table
            i = 0
            while i < len(l1)-1:
                if idx_upd == l1[i+1]['id']:
                    list_chos = [l1[0], l1[idx_upd+1]]
                    show_table(list_chos)
                    
                    chs_upd = str(input('Tekan Y Jika Ingin Update Data dan Tekan N Jika Tidak (Y/N): ')).capitalize()
                    
                    if chs_upd == 'Y':
                        chs_col = str(input('Masukkan Kolom/ Keterangan Yang Ingin Diedit: '))

                        if chs_col in l1[0].values():
                            if chs_col == 'Stok':
                                count = int(input('Masukkan Tambahan Stok Barang Baru: '))
                                # Update Stok ke Daftar Barang
                                chs_save = str(input('Apakah Data Akan Diupdate (Y/N): ')).capitalize()
                                if chs_save == 'Y':
                                    l1[i+1].update({'stck': l1[i + 1]['stck'] + count})
                            elif chs_col == 'Harga':
                                price = int(input('Masukkan Harga Barang Terbaru: '))
                                # Update Harga ke Daftar Barang
                                chs_save = str(input('Apakah Data Akan Diupdate (Y/N): ')).capitalize()
                                if chs_save == 'Y':
                                    l1[i+1].update({'prc': price })
                            print('Data Terupdate')
                            print('\n')
                            show_table(l1)
                            break
                        else:
                            rowformat(symb = "*", sent = "Kolom Tidak Tersedia")
                    break

                else:
                    i += 1
                    if i == len(l1)-1:
                        rowformat(symb = "*", sent = "Data Yang Anda Cari Tidak Ada")
                        break
            
        elif (submenu_update == 2):
            return
        else:
            rowformat(symb = "*", sent = "Pilihan yang anda Masukkan Salah")
        


def menu_delete(l1: list[dict],title: str = 'Menghapus Data Barang') -> str:
    while True:
        #Show title and sub-menu
        rowformat(symb = "+", sent = title)
        print(""" 
        List Sub-Menu:
        1. Menghapus Data Barang
        2. Kembali Ke Menu Utama
        """)
        sub_del = int(input('Silahkan Pilih Sub Menu Delete Data[1-2]: '))
        print('\n')
        
        if (sub_del == 1):
            idx_del = int(input('Masukkan Indeks Barang: '))
            #Show table
            i = 0
            while i < len(l1)-1:
                if idx_del == l1[i+1]['id']:
                    list_chos = [l1[0], l1[idx_del+1]]
                    show_table(list_chos)
                    
                    chs_del = str(input('Apakah Data Akan Dihapus (Y/N): ')).capitalize()
                    
                    if chs_del == 'Y':
                        # Menghapus Barang
                        del l1[idx_del+1]
                        print('Data Telah Dihapus \n')
                        show_table(l1)
                    break
                
                else:
                    i += 1
                    if i == len(l1)-1:
                        rowformat(symb = "*", sent = "Data Yang Anda Cari Tidak Ada")
           
            
        elif (submenu_update == 2):
            return
        else:
            rowformat(symb = "*", sent = "Pilihan yang anda Masukkan Salah")



def rowformat(symb : str, sent : str) -> str:
    space = round((50-len(sent))/2)
    return print(symb*space, sent, symb*space, '\n')

def show_table(lt : list[dict]) -> str:
    # Set print format 
    prntfor_head = "{:<10}" + "{:<15}" * (len(lt[0])-1)
    prntfor_dat = "{:<10}" + "{:<15}" + "{:<15,}" * (len(lt[0])-2)
    n=0 
    for i in lt:
        listd_row = list(i.values())
        if n == 0:
            print(prntfor_head.format(listd_row[0], *listd_row[1:]))
        else:
            print(prntfor_dat.format(listd_row[0], listd_row[1], *listd_row[2:]))
        n+=1
    print("\n")

main()

